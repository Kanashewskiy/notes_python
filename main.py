import json
import time


notes = {}

def show_notes():
    print('Текущий список заметок: ')
    for key, value in notes.items():
        print(key, value)

def add_notes():
    id = input('Введите идентификатор заметки: ')

    while not id.isdigit() or id == '0':
        print('Ошибка ввода! Введите число!')
        id = input('Введите идентификатор заметки: ')

    id = int(id)

    name = input('Введите название заметки: ')
    body = input('Введите основную заметки: ')
    t_save = time.asctime()

    notes[id] = {
        "Время сохранения": t_save,
        "Название": name,
        "Основная часть": body
    }

    print('Заметка успешно добавлена!')

def save_notes():
    with open("notes.json", "w", encoding="utf-8") as fw:
        fw.writelines(json.dumps(notes, ensure_ascii=False, indent=4))
    print("Список заметок успешно сохранён!")

def import_notes():
    with open("notes.json", "r", encoding="utf-8") as fr:
        notes = json.load(fr)
    print("Список заметок успешно загружен!")
    return notes

def search_notes():
    key = input('Введите идентификатор заметки, которую необходимо найти: ')
    value = notes.get(key)

    if key in notes:
        print('Результат поиска: ', value)
    else:
        print('Заметка не найдена')

def delete_notes():
    delete = input('Введите идентификатор заметки, которую необходимо удалить: ')
    try:
        notes.pop(delete)
        print('Заметка успешно удалена!')
    except:
        print('Заметка не найдена!')

def change_notes():
    key = input('Введите идентификатор заметки, которую необходимо изменить: ')
    value = notes.get(key)

    if key in notes:
        print('Изменяемая заметка: ', value)
        id = input('Введите новый идентификатор: ')
        while not id.isdigit() or id == '0':
            print('Ошибка ввода! Введите число!')
            id = input('Введите идентификатор заметки: ')
        id = int(id)
        name = input('Введите новое имя заметки: ')
        body = input('Введите новую основную часть заметки: ')
        t_save = time.asctime()
        notes[id] = {
            "Время изменения": t_save,
            "Название": name,
            "Основная часть": body
        }
        print('Заметка успешно изменена!')
        try:
            notes.pop(key)
        except:
            False
    else:
        print('Заметка не найдена!')

print("Добро пожаловать в приложение 'Заметки'.\nДля запуска программы введите '/start'")
while True:
    command = input("Введите команду: ")
    if command == '/start':
        print('Приложение "Заметки" запущено!\nДля просмотра списка команд введите: /help.')
    elif command == '/help':
        print('Просмотр всего списка команд: /help' + '\n'
        +'Просмотр всех заметок: /show' + '\n'
        +'Добавить новую заметку: /add' + '\n'
        +'Импорт заметок: /import' + '\n'
        +'Поиск заметки: /search' + '\n'
        +'Удалить заметку: /delete' + '\n'
        +'Изменить заметку: /change' + '\n'
        +'Сохранить текущий список заметок: /save' + '\n'
        +'Сохранить текущий список заметок и выйти: /save and exit' + '\n'
        +'Закрыть список заметок: /exit')
    elif command == '/show':
        show_notes()
    elif command == '/add':
        add_notes()
    elif command == '/import':
        notes = import_notes()
    elif command == '/search':
        search_notes()
    elif command == '/delete':
        delete_notes()
    elif command == '/change':
        change_notes()
    elif command == '/save':
        save_notes()
    elif command == '/save and exit':
        save_notes()
        print('Приложение "Заметки" закрыто!')
        break
    elif command == '/exit':
        command_save = input('Приложение "Заметки" будет закрыто, сохранить текущие изменения ? (да/нет): ')
        if command_save == 'да':
            save_notes()
            print('Приложение "Заметки" закрыто!')
            break
        elif command_save == 'нет':
            print('Приложение "Заметки" закрыто!')
            break
    else:
        print('Неопознанная команда. Посмотреть все команды /help')