#преобразование метеорологических градусов в направления ветра
def wind_direction(direction):
    if (348 <= direction <= 360):
        return "С"
    if (0 <= direction <= 11):
        return "С"
    if (12 <= direction <= 33):
        return "ССВ"
    if (34 <= direction <= 56):
        return "СВ"
    if (57 <= direction <= 78):
        return "ВСВ"
    if (79 <= direction <= 101):
        return "В"
    if (102 <= direction <= 123):
        return "ВЮВ"
    if (124 <= direction <= 146):
        return "ЮВ"
    if (147 <= direction <= 168):
        return "ЮЮВ"
    if (169 <= direction <= 191):
        return "Ю"
    if (191 <= direction <= 213):
        return "ЮЮЗ"
    if (214 <= direction <= 236):
        return "ЮЗ"
    if (237 <= direction <= 258):
        return "ЗЮЗ"
    if (259 <= direction <= 281):
        return "З"
    if (282 <= direction <= 303):
        return "ЗСЗ"
    if (304 <= direction <= 326):
        return "СЗ"
    if (327 <= direction <= 347):
        return "ССЗ"
    else:
        return "Да не может такого быть!"
