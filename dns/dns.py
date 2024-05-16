import os
from paramiko import SSHClient
from dotenv import load_dotenv
import sys

# Sprawdzenie, czy podano odpowiednią liczbę argumentów
if len(sys.argv) != 3:
    print("Użycie: python skrypt.py ścieżka_do_folderu_1 ścieżka_do_folderu_2")
    sys.exit(1)

# Ścieżki do folderów z plikami .env
folder_path_1 = sys.argv[1]
folder_path_2 = sys.argv[2]

# Funkcja do wczytywania zmiennych środowiskowych z określonego folderu
def load_env_variables(folder_path):
    env_file_path = os.path.join(folder_path, '.env')
    if os.path.exists(env_file_path):
        load_dotenv(dotenv_path=env_file_path)
    else:
        print(f"Nie znaleziono pliku .env w folderze: {folder_path}")
        sys.exit(1)

# Funkcja do połączenia z serwerem
def connect_ssh(host, port, username, key_path):
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, port=int(port), username=username, key_filename=key_path)
        # Tutaj możesz wykonać komendy, np.:
        stdin, stdout, stderr = client.exec_command('echo "Połączono z serwerem"')
        print(stdout.read().decode('utf-8'))
    except Exception as e:
        print(f"Wystąpił błąd podczas łączenia z {host}: {e}")
    finally:
        client.close()

# Wczytanie zmiennych środowiskowych dla pierwszego serwera
load_env_variables(folder_path_1)
host1 = os.getenv('SSH_HOST')
port1 = os.getenv('SSH_PORT')
user1 = os.getenv('SSH_USER')
private_key_path1 = os.getenv('PRIVATE_KEY_PATH')

# Połączenie z pierwszym serwerem
connect_ssh(host1, port1, user1, private_key_path1)

# Wczytanie zmiennych środowiskowych dla drugiego serwera
load_env_variables(folder_path_2)
host2 = os.getenv('SSH_HOST')
port2 = os.getenv('SSH_PORT')
user2 = os.getenv('SSH_USER')
private_key_path2 = os.getenv('PRIVATE_KEY_PATH')

# Połączenie z drugim serwerem
connect_ssh(host2, port2, user2, private_key_path2)
