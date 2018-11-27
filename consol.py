import xml.etree.ElementTree as ET
import os
from pynput import keyboard


class Application:
    print('\nУкажите путь до xml файла: ')
    docum = input()
    # C:\\Users\\Conficker\\PycharmProjects\\praktika\\items.xml

    XML_FILE = os.path.join(os.environ['USERPROFILE'], docum)
    try:
        d = []
        notes = ""
        tree = ET.ElementTree(file=XML_FILE)
        root = tree.getroot()

        count = len(root)

        for i in range(count):
            for j in range(len(root[i])):
                notes += root[i][j].text + "\t"
            d.append(notes)
            notes = ""

        print('\nTodo list:')
        for i in range(len(d)):
            print(d[i])

    except IOError as e:
        print('\nERROR - cant find file: %sn' % e)
        exit()
    finally:
        print('\nПроверка окончена!')


class Editor():
    def get_action(self):
        key = input()
        if len(key) > 0:
            try:
                code = ord(key)
                """работает"""
                if code == b"e"[0]:
                    print('\nВыбрана функция изменение списка заметок')
                    print('\nВведите имя заметки:')
                    name = input()
                    print('\nВведите содержимое заметки:')
                    content = input()
                    note = name + "\t" + content + "\tFalse"
                    print('\nСоздать новую заметку? y(да), n(нет):')

                    key2 = input()
                    code2 = ord(key2)
                    if code2 == b"y"[0]:
                        Application.d.append(note)
                        print('\nЗапись добавлена!')
                    elif code2 == b"n"[0]:
                        self.get_action()

                """работает"""
                if code == b"d"[0]:
                    print('\nВыбрана функция удаления заметки')
                    print('\nВведите номер заметки:')
                    number = int(input())
                    Application.d.pop(number - 1)
                    print('\nЗаметка была удалена!')
                    print('\nИзмененный список заметок')
                    for i in range(len(Application.d)):
                        print(Application.d[i])

                """надо подумать"""
                if code == b"t"[0]:
                    print('\nВыбрана функция изменения состояния выполнения')

                """работает"""
                if code == b"x"[0]:
                    print('\nCохраняем и выходим из программы')
                    file = open('Notes.txt', 'w')
                    for i in range(len(Application.d)):
                        file.writelines(Application.d[i] + " ")
                        file.write("\n")
                    file.close()
                    print('Bye, bye')
                    exit()

                """работает"""
                if code == b"b"[0]:
                    print('Bye, bye')
                    exit()
                print('\ne-edit, d-delete, t-toggle complete state, x-exit and save, b-exit without save')
                print('\nВведите следующюю команду:')
                self.get_action()
            except TypeError:
                print('\nТакой команды нет!')
                self.get_action()

        else:
            self.get_action()

    print('\ne-edit, d-delete, t-toggle complete state, x-exit and save, b-exit without save')

Editor().get_action()
