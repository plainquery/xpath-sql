
## nodejs

Aby zarządzać zapytaniami przychodzącymi do backendu z frontendu, można wykorzystać kolejkowanie zapytań. Jest to szczególnie przydatne, gdy chcesz uniknąć przeciążenia serwera i zapewnić płynną obsługę wielu jednoczesnych żądań. Oto ogólny przepływ pracy dla kolejkowania zapytań:

1. **Frontend wysyła żądanie**: Użytkownik wykonuje akcję na stronie internetowej, która generuje żądanie HTTP do backendu.
2. **Kolejkowanie żądań**: Backend odbiera żądanie i umieszcza je w kolejce. Można do tego użyć specjalistycznych systemów kolejkowania, takich jak RabbitMQ, Redis lub Kafka.
3. **Przetwarzanie żądań**: Żądania są przetwarzane sekwencyjnie lub równolegle, w zależności od konfiguracji systemu kolejkowania.
4. **Backend zwraca odpowiedź**: Po przetworzeniu żądania, backend generuje odpowiedź i wysyła ją z powrotem do frontendu.
5. **Frontend odbiera odpowiedź**: Frontend odbiera odpowiedź i aktualizuje interfejs użytkownika zgodnie z otrzymanymi danymi.

(1) Connecting the frontend and the backend. https://www.youtube.com/watch?v=ACI8EDbaXzo.
(2) Backend - Podstawy w Node.js i Express. https://www.youtube.com/watch?v=Oc9hbOL0_nk.
(3) Frontend vs Backend 🔥 πroman #1 🔥 hello roman. https://www.youtube.com/watch?v=QxJPo60jKF8.
(4) Czym się różni backend i frontend? Poznaj 7 różnic.. https://perfectone.pl/biznes_blog/czym-sie-rozni-backend-i-frontend-poznaj-7-roznic/.
(5) Przegląd sposobów komunikacji frontend-backend: REST vs GraphQL. https://boringowl.io/blog/porownanie-sposobow-komunikacji-miedzy-aplikacja-frontendowa-rest-vs-graphql.
(6) Jaka jest różnica między frontendem a backendem. https://jakajest.pl/jaka-jest-roznica-miedzy-frontendem-a-backendem/.
(7) undefined. https://zaczynamyprogramowac.pl/.
(8) undefined. https://www.facebook.com/groups/zaczynamy.programowac.
(9) undefined. https://www.youtube.com/channel/UCF4jzVCa2J45NXnNtf6XBoA?sub_confirmation.


## python

Aby stworzyć kolejkę do wykonywania skryptów bash, zapytań SQL oraz wywołań API zgodnie ze standardem OpenAPI, możesz wykorzystać kombinację różnych narzędzi i technologii. Oto przykładowy przepływ pracy:

1. **Kolejkowanie**: Użyj systemu kolejkowania, takiego jak RabbitMQ, aby zarządzać zadaniami i zapewnić ich sekwencyjne lub równoległe przetwarzanie.

2. **Skrypty Bash**: Skrypty Bash mogą być wykonywane przez workery, które nasłuchują na zadania w kolejce. Każde zadanie może zawierać informacje potrzebne do wykonania skryptu.

3. **Zapytania SQL**: Zapytania mogą być przekazywane do workera, który ma dostęp do bazy danych. Worker może używać narzędzi takich jak `sqlplus` dla Oracle lub odpowiednich klientów dla innych systemów baz danych.

4. **API OpenAPI**: Możesz zdefiniować swoje API przy użyciu specyfikacji OpenAPI i użyć automatycznie generowanych klientów API do komunikacji z backendem.

5. **Worker**: Stwórz workera, który będzie obsługiwał zadania z kolejki i wykonywał odpowiednie skrypty bash, zapytania SQL lub wywołania API.

6. 
7. (1) How do you execute SQL from within a bash script?. https://stackoverflow.com/questions/1467846/how-do-you-execute-sql-from-within-a-bash-script.
(2) Bash: Jak zrobić skrypt wykonywalny | Desde Linux. https://bing.com/search?q=jak+stworzy%c4%87+kolejk%c4%99+do+wykonywania+skrypt%c3%b3w+bash%2c+zapyta%c5%84+sql%2c+api+przez+standard+openapi.
(3) Podstawowe komendy i zapytania SQL. Wytłumaczenie, opis i tabela z .... https://webporadnik.pl/podstawowe-komendy-i-zapytania-sql-wytlumaczenie-opis-i-tabela-z-opisem-komend-zapytan-do-bazy-danych-sql/.
(4) Tworzenie i używanie skryptów Bash: kompletny przewodnik - ICHI.PRO. https://ichi.pro/pl/tworzenie-i-uzywanie-skryptow-bash-kompletny-przewodnik-262876754103329.
(5) undefined. http://jdbcsql.sourceforge.net/.
(6) undefined. https://bing.com/search?q=.
(7) en.wikipedia.org. https://en.wikipedia.org/wiki/Bash_(Unix_shell).
