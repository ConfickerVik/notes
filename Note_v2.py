import sys, os, re
import xml.etree.ElementTree as ET


class Functionality(object):
    def edit(self, dict_notes):
        print('\nВыбрана функция изменения списка заметок')
        dict_edit = {}
        print('\nВведите имя заметки:')
        name_notes = input()
        print('\nВведите содержимое заметки:')
        content_notes = input()
        print('\nСоздать новую заметку? y(да), n(нет):')
        confirmation_key = input()
        if re.findall("\w", name_notes) != [] and re.findall("\w", content_notes) != [] and confirmation_key == 'y':
            dict_edit[0] = name_notes
            dict_edit[1] = content_notes
            dict_edit[2] = "False"
            dict_notes[len(dict_notes)] = dict_edit
        elif confirmation_key == 'n':
            print('\nДобавлние заявки отклонено.')
        else:
            print('\nДобавлние заявки отклонено.')

    def rewrite_dict(self, dict_notes):
        new_dict = []
        for key in dict_notes:
            new_dict.append(dict_notes[key])
        dict_notes.clear()
        for num in range(len(new_dict)):
            dict_notes[num] = new_dict[num]
        return dict_notes

    def delete(self, dict_notes):
        print('\nВыбрана функция удаления заметки')
        print('\nВведите номер заметки:')
        number_notes = input()
        if re.findall("\d", number_notes) != [] and int(number_notes) > 0 and int(number_notes) <= len(dict_notes):
            dict_notes.pop(int(number_notes)-1)
            Functionality.rewrite_dict(self, dict_notes)
            print('\nЗаметка была удалена!')
        else:
            print('\nОперация была отклонена')

    def toggle(self, dict_notes):
        print('\nВыбрана функция изменения состояния выполнения')
        print('\nВведите номер заметки:')
        number_notes = input()
        if re.findall("\d", number_notes) != [] and int(number_notes) > 0 and int(number_notes) <= len(dict_notes):
            number_notes = int(number_notes) - 1
            dict_notes[number_notes][2] = "True"
            print('\nСостояние заметки было изменено')
        else:
            print('\nОперация была отклонена')

    def save_and_exit(self, dict_notes):
        main_tag = ET.Element("todo-list")
        tags = {0: "name", 1: "description", 2: "completed"}

        for i in range(len(dict_notes)):
            internal_tag = ET.Element("todo-item")
            main_tag.append(internal_tag)
            for j in range(len(dict_notes[i])):
                begin = ET.SubElement(internal_tag, tags[j])
                begin.text = dict_notes[i][j]

        tree = ET.ElementTree(main_tag)
        tree.write(sys.argv[1])
        print("Сохранение прошло успешно!")
        exit(0)

    def exit_without_save(self, dict_notes):
        print('Bye, bye')
        exit(0)


class Verify(object):
    def verifyXml(document, dict_notes):
        try:
            tree = ET.parse(document)
            courses = tree.findall('todo-item')
            num = 0
            help = {}
            for c in courses:
                help[0] = c.find('name').text
                help[1] = c.find('description').text
                help[2] = c.find('completed').text
                dict_notes[num] = help.copy()
                num += 1
        except:
            return False
        return print('Успешная проверка файла')


if __name__ == "__main__":
    # Принимает файл из командной строки
    document = sys.argv[1]
    dict_notes = {}
    root = Verify.verifyXml(document, dict_notes)

    if root is not False:
        print('\nTodo list:')
        for key, value in dict_notes.items():
            print(str(key + 1), '. ', '\t'.join(str(dict_notes[key][num]) for num in value), sep='')
    else:
        print('\nERROR - check file: %s' % document)
        exit()

    obj = Functionality()
    dict_functions = {
        'e': obj.edit,
        'd': obj.delete,
        't': obj.toggle,
        'x': obj.save_and_exit,
        'b': obj.exit_without_save
    }

    while True:
        print('e-edit, d-delete, t-toggle complete state, x-exit and save, b-exit without save')
        print('\nВведите команду:')
        command = input()

        if command in dict_functions:
            run = dict_functions[command]
            run(dict_notes)
        else:
            print('Введите корректную команду!')

        os.system('cls')

        print('\nTodo list:')
        for key, value in dict_notes.items():
            print(str(key + 1), '. ', '\t'.join(str(dict_notes[key][num]) for num in value), sep='')
