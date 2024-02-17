# ЦГА-ТГГ-ТЦЦ-ГАЦ
# ГЦУ-АЦЦ-АГГ-ЦУГ
# ЦГА,УГГ,УЦЦ,ГАЦ
# ГЦТ-АЦЦ-АГГ-ЦТГ
a = str(input("Введите последовательность нуклеотидов в цепи: "))
a = a.upper()
a = a.replace("-", " ")

replaced_text = a.replace("А", "*").replace("Т", "А").replace("*", "Т").replace("Г", "*").replace(
    "Ц", "Г").replace("*", "Ц")  # ДНК 1 ДНК 2
replaced_text1 = a.replace("Т", "А").replace("А", "У").replace("Ц", "*").replace("Г", "Ц").replace(
    "*", "Г")
replaced_text2 = a.replace("А", "*").replace("У", "А").replace("*", "У").replace("", "").replace("Г",
                                                                                                 "*").replace(
    "Ц", "Г").replace("*", "Ц")
replaced_text3 = a.replace("А", "У").replace("Т", "А").replace("Г", "*").replace("Ц", "Г").replace(
    "*", "Ц")
replaced_text4 = a.replace("Т", "У")
replaced_text5 = a.replace("Т", "У")

string = a
symbol = ","
symbol0 = "-"
letter1 = "А"
letter2 = "Т"
letter3 = "У"
letter4 = "Ц"
letter5 = "Г"

setofletters = "УУУ"
setofletters0 = "УУЦ"
setofletters1 = "УУА"
setofletters2 = "УУГ"
setofletters3 = "УЦ"
setofletters4 = "УАУ"
setofletters5 = "УАЦ"
setofletters6 = "УАА"
setofletters7 = "УАГ"
setofletters8 = "УГУ"
setofletters9 = "УГЦ"
setofletters10 = "УГА"
setofletters11 = "УГГ"
setofletters12 = "ЦУ"
setofletters13 = "ЦЦ"
setofletters14 = "ЦАУ"
setofletters15 = "ЦАЦ"
setofletters16 = "ЦАА"
setofletters17 = "ЦАГ"
setofletters18 = "ЦГ"
setofletters19 = "АУУ"
setofletters20 = "АУЦ"
setofletters21 = "АУА"
setofletters22 = "АУГ"
setofletters23 = "АЦ"
setofletters24 = "ААУ"
setofletters25 = "ААЦ"
setofletters26 = "ААА"
setofletters27 = "ААГ"
setofletters28 = "АГУ"
setofletters29 = "АГЦ"
setofletters30 = "АГА"
setofletters31 = "АГГ"
setofletters32 = "ГУ"
setofletters33 = "ГЦ"
setofletters34 = "ГАУ"
setofletters35 = "ГАЦ"
setofletters36 = "ГАА"
setofletters37 = "ГАГ"
setofletters38 = "ГГ"
replaced_text6 = a
replaced_text6 = replaced_text2.replace("УУУ", "Фен").replace("УУЦ", "Фен").replace("УУА",
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

replaced_text7 = replaced_text3.replace("УУУ", "Фен").replace("УУЦ", "Фен").replace("УУА",
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

if letter1 and letter2 in string:
    print("ДНК:", replaced_text)
    print("иРНК:", replaced_text3)
    print("тРНК:", replaced_text5)
    print("А/К:", replaced_text7)
else:
    if symbol0 in string:
        print("ДНК 1:", replaced_text5)
        print("ДНК 2:", replaced_text1)
        print("тРНК:", replaced_text2)
    else:
        if symbol and letter1 and letter3 in string:
            print("ДНК 1:", replaced_text3)
            print("ДНК 2:", replaced_text4)
            print("иРНК:", replaced_text2)
            print("А/К:", replaced_text6)