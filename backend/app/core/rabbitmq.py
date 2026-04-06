import pika
import json

# Função para criar conexao com Rabbitmq
def get_connection():
    return pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )

# Função para publicar eventos
def publish_event(queue: str, message: dict):
    connection = get_connection()
    channel = connection.channel()

    # Garante que a fila existe
    channel.basic_publish(
        exchange="",
        routing_key=queue,
        body=json.dumps(message)
    )

    # Fecha conexão
    connection.close()