Форматирование json
===================

О программе
-----------

Программа принимает на вход json файл и выводит его содержимое в консоль в удобном формате.
Пример:
-------

     [
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10", 
            "AdmArea": "Западный административный округ", 
            "ClarificationOfWorkingHours": null, 
            "District": "район Кунцево", 
            "IsNetObject": "да", 
            "Name": "Ароматный Мир", 
            "OperatingCompany": "Ароматный Мир", 
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ], 
            "TypeService": "реализация продовольственных товаров", 
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "вторник", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "среда", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "четверг", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "пятница", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "суббота", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "воскресенье", 
                    "Hours": "09:30-22:30"
                }
            ], 
            "geoData": {
                "coordinates": [
                    37.39703804817934, 
                    55.740999719549094
                ], 
                "type": "Point"
            }, 
            "global_id": 14371450
        }, 
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18", 
        "Number": 1
    }, 
    
    
Установка 
---------

1. Если у Вас еще не установлен Python, Вы можете загрузить версию Python 3.0 и выше на [официальном сайте](http://python.org).
2. Скачайте или скопируйте содержимое файла `pprint_json.py` в папку.
2. Поместите json-файл в папку с программой.

Работа с программой
-------------------

1. Запустите программу
2. Укажите имя json файла
3. Программа выведет содержимое файла в удобном формате
