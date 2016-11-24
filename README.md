# TrattenTracker
Training attendance tracker with the option to calculate attendance-based monthly fees and provide it online for all students.

Autorzy: Łukasz Hejnak, Łukasz Malinowski

## Instalacja (za pierwszym razem, potem tylko kroki 2, 4, 7 i 8):
0. Upewnij się, że masz python3 (3.4.3) oraz pip 7.1.0 zainstalowany (i skonfigurowany by używał python3)
1. sudo pip install virtualenv
2. git clone git@github.com:LeHack/TrattenTracker
3. cd TrattenTracker
4. virtualenv .
5. source bin/activate
6. pip install Django==1.10.3
7. dodaj nową domenę (np. trattentracker.pl) w /etc/hosts wskazującą na 127.0.0.100, np.
        sudo echo "127.0.0.100   trattentracker.pl" >> /etc/hosts
8. python manage.py migrate
9. python manage.py runserver trattentracker.pl:8000
10. wejdź na trattentracker.pl:8000
11. ???
12. profit $$$
