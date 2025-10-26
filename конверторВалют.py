import pprint
import requests

from termcolor import colored


def final_translate():
    sure = colored("Вы точно хотите выйти?", "white", "on_yellow")
    yes = colored("[1] Да", "green")
    no = colored("[2] Нет", "red", attrs=["bold"])
    back = colored("[1] Назад", "blue")
    menu = colored("[2] Выход в главное меню", "magenta")
    while True:
        print(f"{back}\n{menu}\n[3] Выйти")
        do_exit = input()
        if do_exit == "1":
            return "flag_again"
        elif do_exit == "2":
            return "flag_menu"
        elif do_exit == "3":
            print(f"{sure}\n{yes}\n{no}")
            do_maybe_exit = input()
            if do_maybe_exit == "1":
                return "flag_exit"
            elif do_maybe_exit == "2":
                continue
            else:
                print(colored("Неправильный формат ввода. Попробуйте снова", "red"))
                continue
        else:
            print(colored("Неправильный формат ввода. Попробуйте снова", "red"))
            continue


url = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")


def print_xml(value, find):
    url_json = url.json()
    return url_json["Valute"][value][find]


def flag_true():
    return True


def maybe_exit(do):
    if do == "1":
        return True
    elif do == "2":
        return False
    else:
        return "Неправильный формат ввода попробуйте снова"


while True:
    url = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    url_json = url.json()
    sure = colored("Вы точно хотите выйти?", "white", "on_yellow")
    yes = colored("[1] Да", "green")
    no = colored("[2] Нет", "red", attrs=["bold"])
    syntax = colored("Неправильный формат ввода", "red")
    what_result = f"{sure}\n{yes}\n{no}"
    convert = colored("Конвертер валют v1.0 Выберите действие:", "white", "on_yellow")
    do_1 = colored("[1] Вывести список валют", "red")
    do_2 = colored("[2] Перевести из одной валюты в другую", "green", attrs=["dark"])
    do_3 = colored("[3] Дополнительная информация о валютах", "grey")
    print(f"{convert}\n{do_1}\n{do_2}\n{do_3}\n[4] Выйти")
    do = input()
    if do == "4":
        while True:
            print(what_result)
            do_exit = input()
            exit = False
            if maybe_exit(do_exit) == True:
                exit = flag_true()
                break
            elif maybe_exit(do_exit) == False:
                main_menu = flag_true()
                break
            else:
                print(maybe_exit(do_exit))
                continue
        if exit:
            break
        elif main_menu:
            continue

    elif do == "1":
        flag = False
        while True:
            for value in url_json["Valute"]:
                print(
                    f"{colored(value, 'green')} {colored(print_xml(value, 'Name'), 'yellow')}"
                )
            while True:
                print(colored("[1] Назад", "blue"))
                do_exit = input()
                if do_exit == "1":
                    flag = True
                    break
                else:
                    print(syntax)
                    continue
            if flag:
                break
        if flag:
            continue

    elif do == "3":
        flag = False
        flag_exit = False
        while True:
            what_inf = colored(
                "Какая дополнительная информация вас интересует?", "white", "on_yellow"
            )
            ID = colored("[1] ID", "magenta")
            NumCode = colored("[2] Цифровой код", "grey")
            Nominal = colored("[3] Номинал", "green")
            back = colored("[4] Назад", "blue")
            print(f"{what_inf}\n{ID}\n{NumCode}\n{Nominal}\n{back}")
            do_additional = input()
            if do_additional == "1":
                for value in url_json["Valute"]:
                    print(
                        f"{colored(value, 'green')} {colored(print_xml(value, 'ID'), 'yellow')}"
                    )
                print(f"{back}\n[2] Выйти")
                do_additional = input()
                if do_additional == "1":
                    continue
                elif do_additional == "2":
                    print(what_result)
                    do_exit = input()
                    if do_exit == "1":
                        flag = True
                        break
                    elif do_exit == "2":
                        continue

            elif do_additional == "2":
                for value in url_json["Valute"]:
                    print(
                        f"{colored(value, 'green')} {colored(print_xml(value, 'NumCode'), 'yellow')}"
                    )
                print(f"{back}\n[2] Выйти")
                do_additional = input()
                if do_additional == "1":
                    continue
                elif do_additional == "2":
                    print(what_result)
                    do_exit = input()
                    if do_exit == "1":
                        flag = True
                        break
                    elif do_exit == "2":
                        continue

            elif do_additional == "3":
                for value in url_json["Valute"]:
                    print(
                        f"{colored(value, 'green')} {colored(print_xml(value, 'Nominal'), 'yellow')}"
                    )
                print(f"{back}\n[2] Выйти")
                do_additional = input()
                if do_additional == "1":
                    continue
                elif do_additional == "2":
                    print(what_result)
                    do_exit = input()
                    if do_exit == "1":
                        flag = True
                        break
                    elif do_exit == "2":
                        continue
            elif do_additional == "4":
                flag_exit = True
                break
            else:
                print(syntax)
                continue
        if flag:
            break
        elif flag_exit:
            continue

    elif do == "2":
        flag_again = False
        flag_menu = False
        flag_exit = False
        that = colored("Вот перевод", "yellow")
        while True:
            try:
                write = colored(
                    'Ввидите валюту и сумму(пример: "AUD/RUB 100")',
                    "white",
                    "on_yellow",
                )
                or_write = colored("Или ввидите", "white", "on_yellow")
                print(f"{write}\n{or_write} [1] Чтобы выйти")
                do_value = input()
                if do_value == "1":
                    flag_again = True
                    break
                from_value = do_value[:3]
                to_value = do_value[4:7]
                count_from = float(do_value[8:])
                val = colored(from_value + "/" + to_value, "green")
                if from_value == "RUB":
                    print(
                        f'{that} {val}: {colored(round(count_from / print_xml(to_value, "Value"), 2), 'green', attrs=['dark'])}'
                    )
                    flag = final_translate()
                    if flag == "flag_menu":
                        flag_menu = True
                        break
                    elif flag == "flag_again":
                        flag_again = True
                        continue
                    elif flag == "flag_exit":
                        flag_exit = True
                        break

                elif to_value == "RUB":
                    val = colored(from_value + "/" + to_value, "green")
                    print(
                        f'{that} {val}: {colored(round(count_from * print_xml(from_value, "Value"), 2), 'green', attrs=['dark'])}'
                    )
                    flag = final_translate()
                    if flag == "flag_menu":
                        flag_menu = True
                        break
                    elif flag == "flag_again":
                        flag_again = True
                        continue
                    elif flag == "flag_exit":
                        flag_exit = True
                        break
                else:
                    to_rub = print_xml(from_value, "Value") * count_from
                    print(
                        f'{that} {val}: {colored(round(to_rub / print_xml(to_value, "Value"), 2), 'green', attrs=['dark'])}'
                    )
                    flag = final_translate()
                    if flag == "flag_menu":
                        flag_menu = True
                        break
                    elif flag == "flag_again":
                        flag_again = True
                        continue
                    elif flag == "flag_exit":
                        flag_exit = True
                        break
            except ValueError:
                print(syntax)
                continue
        if flag_exit:
            break
    else:
        print(syntax)
        continue
