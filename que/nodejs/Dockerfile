# Wybierz obraz bazowy
FROM node:14

# Ustaw katalog roboczy w kontenerze
WORKDIR /usr/src/app

# Skopiuj plik package.json i zainstaluj zależności
COPY package.json ./
RUN npm install

# Skopiuj pozostałe pliki źródłowe
COPY . .

# Zdefiniuj port, na którym będzie nasłuchiwała aplikacja
EXPOSE 8080

# Uruchom aplikację
#CMD ["npm", "start"]
# Uruchom workera
CMD ["node", "./worker.js"]



