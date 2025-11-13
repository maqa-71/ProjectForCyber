import json

# Открываем и читаем JSON-файл
with open("info.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Выводим данные в читаемом виде
print("Данные из файла:")
print(json.dumps(data, indent=4, ensure_ascii=False))
