import os
from paramiko import SSHClient, RSAKey
from paramiko.ssh_exception import NoValidConnectionsError
from dotenv import load_dotenv
from io import StringIO

# Wczytanie zmiennych środowiskowych z pliku .env
load_dotenv()

# Dane do połączenia SSH
host = os.getenv('SSH_HOST')
port = os.getenv('SSH_PORT')
username = os.getenv('SSH_USERNAME')
password = os.getenv('SSH_PASSWORD')

# Generowanie kluczy RSA
private_key = RSAKey.generate(bits=2048)
public_key = private_key.get_base64()

# Zapis klucza prywatnego do pliku
private_key_file = 'id_rsa'
private_key.write_private_key_file(private_key_file)

# Wysyłanie klucza publicznego na serwer
try:
    with SSHClient() as client:
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, port=int(port), username=username, password=password)

        # Dodanie klucza publicznego do autoryzowanych kluczy na serwerze
        command = f'echo {public_key} >> ~/.ssh/authorized_keys'
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode('utf-8'))

except NoValidConnectionsError as e:
    print(f"Nie można nawiązać połączenia: {e}")
except Exception as e:
    print(f"Wystąpił błąd: {e}")
