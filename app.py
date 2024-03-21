from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pika
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/project'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20))
    item = db.Column(db.String(20))


def send_to_rabbitmq(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='items_queue', durable=True)
    channel.basic_publish(exchange='', routing_key='items_queue', body=json.dumps(data).encode("utf-8"))
    connection.close()


@app.route('/api/items', methods=['POST'])
def create_item():
    if request.method == 'POST':
        data = request.get_json()
        item = data.get('item')

        if item is None:
            return jsonify({'error': 'Item is required'}), 400

        new_item = Item(status='pending', item=item)
        db.session.add(new_item)
        db.session.commit()

        # Send data to RabbitMQ
        send_to_rabbitmq(data)

        return '', 202


if __name__ == '__main__':
    app.run(debug=True)
