import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', default="Аноним", help="Имя пользователя")
parser.add_argument('-p', '--path', help="Путь к файлу, который нужно удалить")
parser.add_argument('-nQ', '--noQuest', action="store_true", help="Подавление вопросов пользователю")
args = parser.parse_args()
print(f"Здравствуй, {args.name}!")
if os.path.exists(args.path):
    if args.noQuest:
        os.remove(args.path)
        print("Файл удалён")
    else:
        answer = input("Вы действительно хотите удалить данный файл? ( Y / N )")
        if answer == 'Y':
            os.remove(args.path)
            print("Файл удалён")
        else:
            print("Файл не удалён")
else:
    print("Извините, данный файл не существует")