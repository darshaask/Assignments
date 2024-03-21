from celery import Celery
import pika
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from models import Base, Item

app = Celery('tasks')
app.config_from_object('celeryconfig')

# Setup SQLAlchemy database connection for MySQL
engine = create_engine('mysql://root:root@localhost/db_name', pool_pre_ping=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

@app.task
def process_item():
    # Establish connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='items_queue',durable=True)

    def callback(ch, method, properties, body):
        item_data = json.loads(body)
        item_name = item_data.get('item')

        # Connect to the database session
        session = DBSession()

        try:
            # Attempt to add or update the item in the database
            db_item = session.query(Item).filter_by(item=item_name).first()

            if db_item:
                # Item already exists, update its status to 'completed'
                db_item.status = 'completed'
            else:
                # Item doesn't exist, add it to the database
                new_item = Item(item=item_name, status='completed')
                session.add(new_item)

            # Commit changes to the database
            session.commit()

        except IntegrityError:
            # Handle integrity errors, such as duplicate item names
            session.rollback()
            print(f"Integrity error occurred for item: {item_name}")

        finally:
            # Close the database session
            session.close()

        # Acknowledge the message
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Consume messages from the queue
    channel.basic_consume(queue='items_queue', on_message_callback=callback)

    # Start consuming
    channel.start_consuming()

    # Close the RabbitMQ connection
    connection.close()
