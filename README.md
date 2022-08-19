# cli_city
Реализовать функционал получения информации о городе посредством Python.

User Story: При запуске файла пользователь вводит название города, система возвращает название города, страну, валюту и количество населения

Tech Requirements:

Ввод реализовать с помощью CLI интерфейса. Выбор WEB-API для получения информации - на усмотрение разработчика.
Код должен быть читаемым, с комментариями и соответствовать принципам DRY, KISS, YAGNI.
Кд должен быть загружен на GitHub или GitLab как отдельный проект с публичным доступом.
Формат вывода только такой как в примере

% python3 task.py Kyiv
>
--------------
Kyiv

Ukraine
UAH
4250000
==============

Если таких городов существует несколько то информация возвращается о каждом из них отдельно

% python3 task.py Odessa
>
--------------
Odessa

Ukraine
UAH
1300000
==============
--------------
Odessa

Unated States
USD
245000
==============

Ввод не должен быть регистрочувтвительным

% python3 task.py kYiV
>
--------------
Kyiv

Ukraine
UAH
4250000
==============


если введенный город не существует - возвращается Invalid city name

% python3 task.py asdasdasd
>
--------------
asdasdasd

Invalid city name: asdasdasd
==============

если в процессе выполнения произошла ошибка - возвращается System Error


% python3 task.py Tel Aviv
>
--------------
System Error
==============
 

api для прикладу!
реестрація на https://api-ninjas.com/profile
show api
import requests
resp = requests.get(
    "https://api.api-ninjas.com/v1/city?name=london",
    headers={"X-Api-Key": "ВАШАПІ"},
).json()
