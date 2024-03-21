import pika

# RabbitMQ connection parameters
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = 'your_username'
RABBITMQ_PASSWORD = 'your_password'
RABBITMQ_QUEUE = 'items_queue'

# Establish RabbitMQ connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)))
channel = connection.channel()

# Declare the queue to ensure it exists
channel.queue_declare(queue=RABBITMQ_QUEUE,durable=True)

# Get a single message from the queue
method_frame, header_frame, body = channel.basic_get(queue=RABBITMQ_QUEUE)

if method_frame:
    print("Message exists in the queue. Message content:")
    print(body.decode('utf-8'))
else:
    print("No message found in the queue.")
