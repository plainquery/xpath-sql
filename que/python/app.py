
import pika
import subprocess
import os

# Konfiguracja połączenia z RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Deklaracja kolejki
channel.queue_declare(queue='task_queue')

# Funkcja do wykonywania skryptów bash
def execute_bash_script(script_path):
    subprocess.run(['bash', script_path])

# Funkcja do wykonywania zapytań SQL
def execute_sql_query(sql_query):
    # Tutaj dodaj logikę do wykonania zapytania SQL
    pass

# Funkcja do wykonywania wywołań API
def execute_api_call(api_endpoint):
    # Tutaj dodaj logikę do wykonania wywołania API
    pass

# Callback obsługujący zadania
def callback(ch, method, properties, body):
    task_data = body.decode()
    # Rozpoznaj typ zadania i wykonaj odpowiednią akcję
    if task_data.startswith('bash'):
        execute_bash_script(task_data.split(' ')[1])
    elif task_data.startswith('sql'):
        execute_sql_query(task_data.split(' ')[1])
    elif task_data.startswith('api'):
        execute_api_call(task_data.split(' ')[1])
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Konsumowanie zadań z kolejki
channel.basic_consume(queue='task_queue', on_message_callback=callback)

print('Worker is started. Waiting for tasks.')
channel.start_consuming()
