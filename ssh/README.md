# ssh

## install dependencies

```bash
pip install --no-cache-dir -r requirements.txt
```

## init rights to run file

```bash
pwd
chmod +rwx ssh.py
```

## start
Aby uruchomić ten skrypt, użyj polecenia w terminalu podając ścieżki do odpowiednich folderów, na przykład:

```bash
./ssh.py .
```

Upewnij się, że w każdym folderze znajduje się plik `.env` zawierający odpowiednie zmienne środowiskowe dla danego serwera. Skrypt używa biblioteki `paramiko` do nawiązania połączenia SSH oraz `python-dotenv` do wczytania zmiennych środowiskowych. Zainstaluj te pakiety używając `pip` przed uruchomieniem skryptu.
