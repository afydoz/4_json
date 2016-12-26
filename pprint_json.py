import json, pprint
"""
Модуль pprint позволяет выводить
содержимое файла в удобном формате
"""

def load_data(filepath):
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as bars:
            return json.load(bars)

def pretty_print_json(data):
    #Вывод содержимого файла в удобном формате
    pprint.pprint(data)

if __name__ == '__main__':

    list_of_bars = load_data(input("Укажите имя файла:"))
    pretty_print_json(list_of_bars)
