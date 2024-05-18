# Wybierz obraz bazowy Pythona z preinstalowanym PIP
FROM python:3.8-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /usr/src/app

# Skopiuj pliki wymagań i zainstaluj zależności
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj pozostałe pliki źródłowe aplikacji
COPY . .

# Zdefiniuj port, na którym będzie nasłuchiwała aplikacja
EXPOSE 5672

# Uruchom aplikację
CMD ["python", "./app.py"]
