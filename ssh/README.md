# ssh


## python

Zainstaluj biblioteki Pythona, jeśli jeszcze tego nie zrobiłeś. Możesz to zrobić używając `pip`:

```bash
py -m pip install --upgrade pip
py -m pip install --upgrade setuptools
py -m pip install --upgrade wheel
py -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

```bash
python3 -m pip install --upgrade build
python3 -m build
```


```bash
python3 -m pip install --upgrade twine
python3 -m twine upload dist/*
pip install "paramiko[all]"
pip install asyncssh
py -m pip install asyncssh
py -m pip install -r requirements.txt
```

## install dependencies

```bash
py -m pip install --no-cache-dir -r requirements.txt
```

## init rights to run file

```bash
pwd
chmod +rwx ssh.py
```

## start
Aby uruchomić ten skrypt, użyj polecenia w terminalu podając ścieżki do odpowiednich folderów, na przykład:

```bash
py ssh.py .
```

```bash
./ssh.py .
```

Upewnij się, że w każdym folderze znajduje się plik `.env` zawierający odpowiednie zmienne środowiskowe dla danego serwera. Skrypt używa biblioteki `paramiko` do nawiązania połączenia SSH oraz `python-dotenv` do wczytania zmiennych środowiskowych. Zainstaluj te pakiety używając `pip` przed uruchomieniem skryptu.
