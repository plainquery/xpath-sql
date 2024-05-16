#!/usr/bin/env python3
# python ssh.py 1

import os
import asyncssh
import asyncio
from dotenv import load_dotenv
import os
import sys

filename = sys.argv[1]

# Sprawdzenie, czy podano odpowiednią liczbę argumentów
if len(sys.argv) != 2:
    print(f"Użycie: python ${filename} nazwa_folderu")
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


# Funkcja do generowania kluczy RSA i zapisu do pliku
async def generate_and_save_rsa_keys(folder):
    private_key = asyncssh.generate_private_key('ssh-rsa')
    public_key = private_key.export_public_key()

    private_key_path = os.path.join(folder, 'id_rsa')
    public_key_path = os.path.join(folder, 'id_rsa.pub')

    with open(private_key_path, 'w') as private_file:
        private_file.write(private_key.export_private_key())
    os.chmod(private_key_path, 0o600)

    with open(public_key_path, 'w') as public_file:
        public_file.write(public_key)
    os.chmod(public_key_path, 0o644)

    return private_key_path, public_key_path


# Funkcja do wysyłania klucza publicznego na serwer
async def send_public_key_to_server(host, port, username, password, public_key_path):
    async with asyncssh.connect(host, port=int(port), username=username, password=password) as conn:
        with open(public_key_path, 'r') as public_file:
            public_key = public_file.read()
        await conn.run(f'echo {public_key} >> ~/.ssh/authorized_keys', check=True)

# Główna funkcja asynchroniczna
async def main(folder_name):
    private_key_path, public_key_path = await generate_and_save_rsa_keys(folder_name)
    await send_public_key_to_server(host, port, username, password, public_key_path)
    print("Klucze RSA zostały wygenerowane i klucz publiczny został wysłany na serwer.")


# Uruchomienie głównej pętli asynchronicznej
loop = asyncio.get_event_loop()
loop.run_until_complete(main(folder_name))
