def identify_animal(answers):
    swims, has_wings, long_neck = answers.split()
    swims = swims.lower() == 'да'
    has_wings = has_wings.lower() == 'да'
    long_neck = long_neck.lower() == 'да'

    if swims:
        if has_wings:
            if long_neck:
                return "Утка"
            else:
                return "Пингвин"
        else:
            if long_neck:
                return "Плезиозавры"
            else:
                return "Дельфин"
    else:
        if has_wings:
            if long_neck:
                return "Страус"
            else:
                return "Курица"
        else:
            if long_neck:
                return "Жираф"
            else:
                return "Кот"

answers = input()
print(identify_animal(answers))