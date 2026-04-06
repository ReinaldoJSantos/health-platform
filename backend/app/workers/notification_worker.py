import pika
import json

def callback(ch, method, properties, body):
    # Converte mensagem
    message = json.loads(body)

    print("📩 Evento recebido:", message)

    # Aqui você pode colocar:
    # - envio de email
    # - log
    # - integração externa

    print(f"🔔 Notificando paciente {message['patient_id']}")

    def start_consumer():
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        channel = connection.channel()

        channel.queue_declare(queue="appointment_created")

        # Consome mensagens da fila
        channel.basic_consume(
            queue="appointment_created",
            on_message_callback=callback,
            auto_ack=True
        )

        print("🚀 Worker rodando...")
        channel.start_consuming()


    if __name__ == "__main__":
        start_consumer()