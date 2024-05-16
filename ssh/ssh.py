#!/usr/bin/env python3

import os
from paramiko import SSHClient, RSAKey
from dotenv import load_dotenv
import sys

# Sprawdzenie, czy podano odpowiednią liczbę argumentów
if len(sys.argv) != 2:
    print("Użycie: python skrypt.py nazwa_folderu")
    sys.exit(1)

# Nazwa folderu z argumentu
folder_name = sys.argv[1]

# Wczytanie zmiennych środowiskowych z pliku .env
load_dotenv()

# Lista wymaganych zmiennych środowiskowych
required_env_vars = ['SSH_HOST', 'SSH_PORT', 'SSH_USER', 'SSH_PASS']

# Sprawdzenie, czy wszystkie wymagane zmienne są ustawione
missing_vars = [var for var in required_env_vars if not os.getenv(var)]
if missing_vars:
    for var in missing_vars:
        # Prośba o podanie brakującej zmiennej
        os.environ[var] = input(f"Proszę podać wartość dla '{var}': ")

# Dane do połączenia SSH
host = os.getenv('SSH_HOST')
port = os.getenv('SSH_PORT')
username = os.getenv('SSH_USER')
password = os.getenv('SSH_PASS')

# Generowanie kluczy RSA
private_key = RSAKey.generate(bits=2048)
public_key = private_key.get_base64()

# Zapis klucza prywatnego do pliku w określonym folderze
private_key_file = os.path.join(folder_name, 'id_rsa')
private_key.write_private_key_file(private_key_file)

# Zapis klucza publicznego do pliku w określonym folderze
public_key_file = os.path.join(folder_name, 'id_rsa.pub')
with open(public_key_file, 'w') as pub_file:
    pub_file.write(f"{public_key}\n")

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

except Exception as e:
    print(f"Wystąpił błąd: {e}")
