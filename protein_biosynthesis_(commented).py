# ЦГА-ТГГ-ТЦЦ-ГАЦ - ДНК 1
# ГЦТ-АЦЦ-АГГ-ЦТГ - ДНК 2
# ГЦУ-АЦЦ-АГГ-ЦУГ - иРНК
# ЦГА,УГГ,УЦЦ,ГАЦ - тРНК
a = str(input("Введите последовательность нуклеотидов в цепи: "))  # На строке 5 программа запрашивает данные, которые пользователь должен ввести с клавиатуры
a = a.upper()  # На строке 6 программа конвертирует вводимую строку в верхний регистр, если с клавиатуры данные были введены в нижнем регистре (что не является правильным)

# С 9 по 21 программа переводит введенную цепь в другие цепи (ДНК, иРНК, тРНК)
replaced_text = a.replace("А", "*").replace("Т", "А").replace("*", "Т").replace("Г", "*").replace(
    "Ц", "Г").replace("*", "Ц")  # На строке 8-9 программа переводит ДНК1 в ДНК2
replaced_text1 = a.replace("Т", "*").replace("А", "У").replace("*", "А").replace("Ц", "*").replace(
    "Г", "Ц").replace("*", "Г")  # На строке 10-11 программа переводит ДНК2 в иРНК
replaced_text2 = a.replace("А", "Т").replace("У", "А").replace("Г", "*").replace(
    "Ц", "Г").replace("*", "Ц")  # На строке 12-13 программа переводит иРНК в ДНК2
replaced_text3 = a.replace("А", "*").replace("У", "А").replace("*", "У").replace("Г", "*").replace(
    "Ц", "Г").replace("*", "Ц").replace(",", "-")  # На строке 14-15 программа переводит иРНК в тРНК
replaced_text4 = a.replace("Т", "У")  # На строке 16 программа переводит ДНК2 в тРНК
replaced_text5 = a.replace("У", "Т").replace(",",
                                             "-")  # На строке 17 программа переводит тРНК в ДНК1 и иРНК в ДНК1
replaced_text6 = a.replace("А", "Т").replace("У", "А").replace("Г", "*").replace(
    "Ц", "Г").replace("*", "Ц").replace(",", "-")  # На строке 18-19 программа переводит тРНК в ДНК2

# С 24 по 93 строку программа переводит последовательность нуклеотидов молекулы иРНК в последовательность аминокислот молекулы белка (генетический код)
replaced_text7 = a.replace("УУУ", "Фен").replace("УУЦ", "Фен").replace("УУА",
                                                                       "Лей").replace(
    "УУГ", "Лей").replace("УЦУ", "Сер").replace("УЦЦ", "Сер").replace("УЦА", "Сер").replace(
    "УЦГ", "Сер").replace("УАУ", "Тир").replace("УАЦ", "Тир").replace("УАА",
                                                                      "СТОП Кодон").replace(
    "УАГ", "СТОП Кодон").replace("УГУ", "Цис").replace("УГЦ", "Цис").replace("УГА", "СТОП Кодон").replace("УГГ",
                                                                                        "Три").replace(
    "ЦУУ", "Лей").replace("ЦУЦ", "Лей").replace("ЦУА", "Лей").replace("ЦУГ", "Лей").replace(
    "ЦЦУ", "Про").replace("ЦЦЦ", "Про").replace("ЦЦА", "Про").replace("ЦЦГ", "Про").replace(
    "ЦАУ", "Гис").replace("ЦАЦ", "Гис").replace("ЦАА",
                                                "Глн").replace(
    "ЦАГ", "Глн").replace("ЦГУ", "Арг").replace("ЦГЦ", "Арг").replace("ЦГА", "Арг").replace(
    "ЦГГ", "Арг").replace("АУУ", "Иле").replace("АУЦ", "Иле").replace("АУА",
                                                                      "Иле").replace(
    "АУГ", "Мет").replace("АЦУ", "Тре").replace("АЦЦ", "Тре").replace("АЦА", "Тре").replace(
    "АЦГ", "Тре").replace("ААУ", "Асн").replace("ААЦ", "Асн").replace("ААА",
                                                                      "Лиз").replace(
    "ААГ", "Лиз").replace("АГУ", "Сер").replace("АГЦ", "Сер").replace("АГА", "Арг").replace(
    "АГГ", "Арг").replace("ГУУ", "Вал").replace("ГУЦ", "Вал").replace("ГУА", "Вал").replace(
    "ГУГ", "Вал").replace("ГЦУ", "Ала").replace("ГЦЦ", "Ала").replace("ГЦА", "Ала").replace(
    "ГЦГ", "Ала").replace("ГАУ", "Асп").replace("ГАЦ",
                                                "Асп").replace(
    "ГАА", "Глу").replace("ГАГ", "Глу").replace("ГГУ", "Гли").replace("ГГЦ", "Гли").replace(
    "ГГА", "Гли").replace("ГГГ", "Гли")

replaced_text8 = replaced_text1.replace("УУУ", "Фен").replace("УУЦ", "Фен").replace("УУА",
                                                                                    "Лей").replace(
    "УУГ", "Лей").replace("УЦУ", "Сер").replace("УЦЦ", "Сер").replace("УЦА", "Сер").replace(
    "УЦГ", "Сер").replace("УАУ", "Тир").replace("УАЦ", "Тир").replace("УАА",
                                                                      "-").replace(
    "УАГ", "-").replace("УГУ", "Цис").replace("УГЦ", "Цис").replace("УГА", "-").replace("УГГ",
                                                                                        "Три").replace(
    "ЦУУ", "Лей").replace("ЦУЦ", "Лей").replace("ЦУА", "Лей").replace("ЦУГ", "Лей").replace(
    "ЦЦУ", "Про").replace("ЦЦЦ", "Про").replace("ЦЦА", "Про").replace("ЦЦГ", "Про").replace(
    "ЦАУ", "Гис").replace("ЦАЦ", "Гис").replace("ЦАА",
                                                "Глн").replace(
    "ЦАГ", "Глн").replace("ЦГУ", "Арг").replace("ЦГЦ", "Арг").replace("ЦГА", "Арг").replace(
    "ЦГГ", "Арг").replace("АУУ", "Иле").replace("АУЦ", "Иле").replace("АУА",
                                                                      "Иле").replace(
    "АУГ", "Мет").replace("АЦУ", "Тре").replace("АЦЦ", "Тре").replace("АЦА", "Тре").replace(
    "АЦГ", "Тре").replace("ААУ", "Асн").replace("ААЦ", "Асн").replace("ААА",
                                                                      "Лиз").replace(
    "ААГ", "Лиз").replace("АГУ", "Сер").replace("АГЦ", "Сер").replace("АГА", "Арг").replace(
    "АГГ", "Арг").replace("ГУУ", "Вал").replace("ГУЦ", "Вал").replace("ГУА", "Вал").replace(
    "ГУГ", "Вал").replace("ГЦУ", "Ала").replace("ГЦЦ", "Ала").replace("ГЦА", "Ала").replace(
    "ГЦГ", "Ала").replace("ГАУ", "Асп").replace("ГАЦ",
                                                "Асп").replace(
    "ГАА", "Глу").replace("ГАГ", "Глу").replace("ГГУ", "Гли").replace("ГГЦ", "Гли").replace(
    "ГГА", "Гли").replace("ГГГ", "Гли")

replaced_text9 = replaced_text3.replace("УУУ", "Фен").replace("УУЦ", "Фен").replace("УУА",
                                                                                    "Лей").replace(
    "УУГ", "Лей").replace("УЦУ", "Сер").replace("УЦЦ", "Сер").replace("УЦА", "Сер").replace(
    "УЦГ", "Сер").replace("УАУ", "Тир").replace("УАЦ", "Тир").replace("УАА",
                                                                      "-").replace(
    "УАГ", "-").replace("УГУ", "Цис").replace("УГЦ", "Цис").replace("УГА", "-").replace("УГГ",
                                                                                        "Три").replace(
    "ЦУУ", "Лей").replace("ЦУЦ", "Лей").replace("ЦУА", "Лей").replace("ЦУГ", "Лей").replace(
    "ЦЦУ", "Про").replace("ЦЦЦ", "Про").replace("ЦЦА", "Про").replace("ЦЦГ", "Про").replace(
    "ЦАУ", "Гис").replace("ЦАЦ", "Гис").replace("ЦАА", "Глн").replace(
    "ЦАГ", "Глн").replace("ЦГУ", "Арг").replace("ЦГЦ", "Арг").replace("ЦГА", "Арг").replace(
    "ЦГГ", "Арг").replace("АУУ", "Иле").replace("АУЦ", "Иле").replace("АУА", "Иле").replace(
    "АУГ", "Мет").replace("АЦУ", "Тре").replace("АЦЦ", "Тре").replace("АЦА", "Тре").replace(
    "АЦГ", "Тре").replace("ААУ", "Асн").replace("ААЦ", "Асн").replace("ААА", "Лиз").replace(
    "ААГ", "Лиз").replace("АГУ", "Сер").replace("АГЦ", "Сер").replace("АГА", "Арг").replace(
    "АГГ", "Арг").replace("ГУУ", "Вал").replace("ГУЦ", "Вал").replace("ГУА", "Вал").replace(
    "ГУГ", "Вал").replace("ГЦУ", "Ала").replace("ГЦЦ", "Ала").replace("ГЦА", "Ала").replace(
    "ГЦГ", "Ала").replace("ГАУ", "Асп").replace("ГАЦ", "Асп").replace(
    "ГАА", "Глу").replace("ГАГ", "Глу").replace("ГГУ", "Гли").replace("ГГЦ", "Гли").replace(
    "ГГА", "Гли").replace("ГГГ", "Гли")

# С 96 по 103 строку вводятся названия (переменные) для символов, которые мы будем использовать в условии IF
string = a
symbol = ","
symbol0 = "-"
letter1 = "А"
letter2 = "Т"
letter3 = "У"
letter4 = "Ц"
letter5 = "Г"

# С 106 по 122 строку программа с помощью условия IF и специальных символов, которые вводятся на строках 96-103, определяет чем является вводимая строка - ДНК, иРНК или тРНК. После определения выводится результат перевода
if letter1 and letter2 in string:
    print("ДНК2:", replaced_text)
    print("иРНК:", replaced_text1)
    print("тРНК:", replaced_text4)
    print("А/К:", replaced_text8)
else:
    if symbol0 in string:
        print("ДНК1:", replaced_text2)
        print("ДНК2:", replaced_text5)
        print("тРНК:", replaced_text3)
        print("А/К:", replaced_text7)
    else:
        if symbol and letter1 and letter3 in string:
            print("ДНК1:", replaced_text5)
            print("ДНК2:", replaced_text6)
            print("иРНК:", replaced_text3)
            print("А/К:", replaced_text9)
