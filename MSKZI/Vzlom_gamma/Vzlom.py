# 7 - й вариант

text = "щуучх бнч ьрсчбкгачщсэфхсшчщс ботталгэаюэуджс фкавщпюшекэшълфкьфс фкааяюсаакдщщкщ " \
       "фцсйещсдфхсфжпчдузгаубдхдэфаущгйфьгыуммюбкааищшшушттещсэбэ вбрсаакъгвегуякьачпттылфшгшдюутттжо юуусйжэнтарс " \
       "фцчдщцс фкцшцюйэжкйшшвдрурюеуштхдэбшкюсшчщс боттцещхфнсгцщъяупфыъряыщчсэбцчффшъшун ъшюжууъ южбъюфк " \
       "дглшшашмьуьъцалэтбкавщърддэфыькяууъддькътвщидькфтеюсщщквшююячжкдчфыъюфьнтбм ткэ " \
       "дбкьующыдбкавщпюшеквтчцдзьчсгеюьа к дяргшякфтерю бэд "
# text = "я стану водопадом падением с высоты и все твои вина из винограда для меня уже слишком просты в тебе больше " \
#        "нет хмеля и крепость твоя не та нам оставалась всего неделя и она уже прожита"
alphabeth = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
             "х", "ц", "ч", "ш", "щ",
             "ъ", "ы", "ь", "э", "ю", "я", " "]
# print(len(alphabeth))


def encrypt(text, gamma):
    textLen = len(text)
    gammaLen = len(gamma)

    # Формируем ключевое слово(растягиваем гамму на длину текста)
    keyText = []
    for i in range(textLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(textLen % gammaLen):
        keyText.append(gamma[i])

    # Шифрование
    code = []
    for i in range(textLen):
        code.append(alphabeth[(alphabeth.index(text[i]) + alphabeth.index(keyText[i])) % 33])
    code_str = ""
    return code


def decrypt(code, gamma):
    codeLen = len(code)
    gammaLen = len(gamma)

    # Формируем ключевое слово(растягиваем гамму на длину текста)
    keyText = []
    for i in range(codeLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(codeLen % gammaLen):
        keyText.append(gamma[i])

    # Расшифровка
    text = []
    for i in range(codeLen):
        text.append(alphabeth[(alphabeth.index(code[i]) - alphabeth.index(keyText[i]) + 32) % 33])

    return text


# Функция взлома шифра гаммирования
def hack(code):
    codeLen = len(code)

    # Подобрать длину гаммы
    gammaLen = -1
    for n in range(2, codeLen // 2):
        # Формируем столбец
        col = []
        for i in range(0, codeLen, n):
            col.append(code[i])

        # Посчитать индекс Фридмана для каждого нулевого столбика для всех длин,
        # взять за эталонную первую, при которой индекс будет максимально близок к 0.066
        symbolsCount = [0 for i in range(33)]
        for symb in col:
            symbolsCount[alphabeth.index(symb)] += 1

        FriedmanIndex = 0
        for i in range(len(symbolsCount)):
            FriedmanIndex += (symbolsCount[i] * (symbolsCount[i] - 1)) / (len(col) * (len(col) - 1))

        # Проверить индекс на попадание в диапазон
        # if abs(FriedmanIndex - 0.066) < 0.006:
        if FriedmanIndex > 0.0553:
            # Если попал, берем n за эталон и уходим
            gammaLen = n
            break

    print('gamma len = ', gammaLen)

    # Теперь можно определить саму гамму

    # Разбиваем текст на столбцы по этой длине гаммы
    # формируем подстроки
    rows = []  # блоки(строки)
    for i in range(0, codeLen - gammaLen, gammaLen):  # без последнего блока
        row = [code[i + j] for j in range(gammaLen)]
        rows.append(row)

    # формируем столбцы
    collumns = []
    for k in range(n):  # выбираем номер столбца
        collumn = []
        for i in range(len(rows)):  # выбираем строку
            collumn.append(rows[i][k])
        collumns.append(collumn)

    # Находим относительные сдвиги столбцов с помощью взаимного индекса Фридмана(совпадений)
    slides = []
    for n in range(1, gammaLen):
        # Находим встречаемость каждого символа в первом столбике
        firstSymbolsCount = [0 for i in range(33)]
        for symb in collumns[n - 1]:
            firstSymbolsCount[alphabeth.index(symb)] += 1

        # Ищем сдвиг для второго столбца такой, чтобы взаимный индекс Фридмана был близок к 0.066
        for m in range(33):
            # сдвинуть второй столбец
            slideSecondCol = []
            for symb in collumns[n]:
                slideSecondCol.append(alphabeth[(alphabeth.index(symb) + m) % 33])

            # Находим встречаемость каждого символа во втором столбике
            secondSymbolsCount = [0 for i in range(33)]
            for symb in slideSecondCol:
                secondSymbolsCount[alphabeth.index(symb)] += 1

            # Находим взаимный индекс Фридмана
            FriedmanIndex = 0
            for i in range(len(firstSymbolsCount)):
                FriedmanIndex = FriedmanIndex + (
                            (firstSymbolsCount[i] * secondSymbolsCount[i]) / (len(collumns[n]) ** 2))

            # Проверяем диапазон
            # if abs(FriedmanIndex - 0.066) < 0.006:
            if FriedmanIndex > 0.0553:
                # Если попали, запоминаем это смещение и останавливаем перебор
                slides.append((33 - m) % 33)
                break

    # У нас есть взаимные сдвиги всех столбцов, теперь нужно найти сдвиг первого
    # искать будем с помощью частотного анализа символов(как в шифре Цезаря)
    currentSymbolsFreq = [0 for i in range(33)]
    for symb in collumns[0]:
        currentSymbolsFreq[alphabeth.index(symb)] += 1
    for i in range(len(currentSymbolsFreq)):
        currentSymbolsFreq[i] = currentSymbolsFreq[i] / len(collumns[0]) * 100

    # Находим все возможные сдвиги для первого столбца
    slidesOfFirstCol = []
    for i in range(len(currentSymbolsFreq)):
        for j in range(len(currentSymbolsFreq)):
            if abs(currentSymbolsFreq[i] - currentSymbolsFreq[j]) < 0.3222:  # 0.25
                slidesOfFirstCol.append(i - j)

    # Берем за эталонное такое смещение, которое встречалось чаще всего
    finalSlide = slidesOfFirstCol[0]
    maximum = slidesOfFirstCol.count(slidesOfFirstCol[0])
    for slide in slidesOfFirstCol:
        if slidesOfFirstCol.count(slide) > maximum:
            maximum = slidesOfFirstCol.count(slide)
            finalSlide = slide

    # Посчитать сдвиги для столбиков, зная сдвиг первого
    finalSlides = []
    finalSlides.append(finalSlide)
    for slide in slides:
        finalSlides.append(slide)
    # считаем сдвиги столбиков
    for i in range(1, len(finalSlides)):
        finalSlides[i] = (finalSlides[i - 1] + finalSlides[i]) % 33

    # Мы нашли гамму в виде сдвигов, осталось преобразовать ее в слово
    gamma = []
    for slide in finalSlides:
        gamma.append(alphabeth[slide])

    return ''.join(gamma)


def __main__():
    list_of_gamma = []
    # print(hack(text))
    gamma = str(input("\nВведите гамму: "))
    if gamma not in list_of_gamma:
        list_of_gamma.append(gamma)
    else:
        gamma = str(input("\nВведите еще раз гамму: "))
    # closed_text = encrypt(text, gamma)
    # for i in closed_text:
    #     print(i, end="")
    open_text = decrypt(text, gamma)
    print("\n")
    symbol_flag = " "
    count = 0
    list_count = [600]
    for i in range(len(open_text)):
        print(open_text[i], end="")
        if i in list_count:
            print()





if __name__ == __main__():
    __main__()

