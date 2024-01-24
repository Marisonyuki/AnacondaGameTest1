import random
import math
import json

print("Konflikt")
print("1. Новая игра\n2. Загрузить сохранение")
T = int(input())
if (T == 1):
    data = {
        "gold": 0,
        "power": 1,
        "mana": 0,
        "Experience": 0,
        "damage": 2,
        "sdamage": 0,
        "health": 20,
        "pArmor": 0,
        "mArmor": 0,
        "d": 0,
        
        "name": None,
        "magic": None,
        "weapon": None
    }
    with open('save.json', 'w') as file:
        json.dump(data, file, indent=4)
        
    with open('save.json', 'r') as file:
        data = json.load(file)
        
        gold = data["gold"]
    power = data["power"]
    mana = data["mana"]
    Experience = data["Experience"]
    damage = data["damage"]
    sdamage = data["sdamage"]
    health = data["health"]
    maxhp = data["health"]+2*data["power"]
    pArmor = data["pArmor"]
    mArmor = data["mArmor"]
    d = data["d"]

    Character = {"Name": data["name"], "Magic": data["magic"], "Weapon": data["weapon"]}
    Stats = {"Gold": gold, "Power": power, "EXP": Experience, "DMG":damage, "SDMG": sdamage, "Mana": mana, "HP":health}
    Spells = []
    
    print("Вы просыпаетесь в лесу на открытой поляне под одиноко стоящим деревом.\nГолова сильно болела и вы совершенно ничего не могли вспомнить, ни о том как здесь оказались, ни о своём прошлом.\nПеред вами сидел мужчина в стильной шляпе и курил свою стильную сигару не обращая внимания на вас.\nПо виду он был уже в преклонном возрасте - Седые волосы, уставшее и усеянное шрамами лицо.\nОдеяния наёмника намекали на его профессию, однако он уже скорее всего давно подал в отставку");
    print("1. Сказать что-то\n2. Промолчать")
    T = int(input())
        
    def IntroScene1():
        print("Вы что-то неуверенно мямлите и мужчина резко прокашливается дымом от лёгкой неожиданности, наконец обратив на вас внимание тот лишь поправляет свою шляпу и спокойно смотрит в вашу сторону")
    def IntroScene2():
        print("Докурив сигарету мужчина наконец обращает внимание на вас и спокойно подходит вытягивая руку вперёд для рукопожатия")

    if (T == 1):
        IntroScene1()
    if (T == 2):
        IntroScene2()
    if (T != None and T != 1 and T != 2):
        print("Из-за вашей нерешительности вы просто молча уселись на траве дожидаясь когда мужчина закончит своё дело")
        IntroScene2()

    print()
    print("Незнакомец: \"Что-то с тобой сегодня не в порядке, не узнаешь старика?\" - Говорил мужчина обращая своё внимание на ваше нежелание приветствовать его")
    print("1. Спросить кто он")
    T = int(input())

    def Explanation1():
        print("Кейн: \"Ты безымянный герой что спас меня когда мы встретились в мёртвой зоне, я уже представлялся и меня зовут Кейн, но своё имя ты так мне и не сказал..\"")
    if (T == 1):
        print("Незнакомец: \"Не удивлён что ты ещё и память потерял, если бы меня так-же жахнули то я бы тут и не стоял\"")
        Explanation1()
    else:
        print("Незнакомец: \"Судя по всему твоё тело ослабло да и похоже ты потерял часть своей памяти из-за атаки берсерка\"")
        print(Explanation1())
        print("Введите ваше имя")
        Character["Name"] = input()
        CName = Character["Name"]
        print("Кейн: \"Мне точно тебя так называть?\"")
        print("1. Да\n2. Нет")
        T = int(input())

        def Prank1():
            print("Кейн: \"Ладно неважно, я и с первого раза понял\"")

        if (T != None):
            Prank1()
        print(f"Кейн: \"Что-же {CName} рано тебе ещё расслабляться, может ты и забыл но у тебя благая цель - Остановить это безумие с вечно наступающими монстрами и победить истинное зло, только ты на такое способен, но не в таком состоянии, так ты и часа не продержишься в мёртвой зоне, ступай и тренируйся.\nЕсли понадоблюсь то я буду ждать тебя здесь, можешь спросить у меня совета или просто поболтать.\"")
        print("Готовы ли вы начать?")
        print("1. Да\n2. Нет")
        L = int(input())
        if (L == 2):
            quit()
if (T == 2):
    with open('save.json', 'r') as file:
        data = json.load(file)
       
    gold = data["gold"]
    power = data["power"]
    mana = data["mana"]
    Experience = data["Experience"]
    damage = data["damage"]
    sdamage = data["sdamage"]
    health = data["health"]
    maxhp = data["health"]+2*data["power"]
    pArmor = data["pArmor"]
    mArmor = data["mArmor"]
    d = data["d"]

    Character = {"Name": data["name"], "Magic": data["magic"], "Weapon": data["weapon"]}
    Stats = {"Gold": gold, "Power": power, "EXP": Experience, "DMG":damage, "SDMG": sdamage, "Mana": mana, "HP":health}
    Spells = []

        
    print("START")
    T = 0

    def StarterCharacter():
        MagicRoll()
        WeaponRoll()
        
    def MagicRoll():
        MR = random.randint(1,2)
        if (MR == 1):
            Character["Magic"] = "Fire"
        if (MR == 2):
            Character["Magic"] = "Water"
            
    def WeaponRoll():
        WR = random.randint(1,2)
        if (WR == 1):
            Character["Weapon"] = "Sword"
        if (WR == 2):
            Character["Weapon"] = "Spear"
            

    def TownEvent():
        EventRoll = random.randint(1,4)
        print(f"На событие вы выбрасываете... {EventRoll}!")
        if (EventRoll == 1):
            print("Вы спокойно прошли по городу и ничего не случилось")
        if (EventRoll == 2):
            gg = random.randint(1,20)
            print(f"Какая удача! Вы походили по деревне и наткнулись на мешочек монет в котором было ровно {gg} монет")
            Stats["Gold"] = Stats["Gold"]+gg
        if (EventRoll == 3):
            gg = random.randint(1,20)
            print(f"Вы столкнуклись с каким-то незнакомцем и позже заметили что потеряли кошелёк. Вы потеряли {gg} монет")
            if (Stats["Gold"]>gg):
                Stats["Gold"] = Stats["Gold"]-gg
            else:
                Stats["Gold"] = 0
        if (EventRoll == 4):
            lhp = random.randint(1,2)
            print (f"вы подскользнулись и упали об твёрдую землю. Вы потеряли {lhp}")
            Stats["HP"] = Stats["HP"]-lhp

    def NormalGame():
        print("Вы находитесь в городе, повсюду слоняются горожане и стража. Всё находится в движении. Что-же будете делать вы?")
        print("1. Пройтись по городу\n2. Проверить своё состояние\n3. Выполнить задание\n4. Потренироваться\n5. Сходить к Кейну\n6. Сдаться")
        T = int(input())
        if (T == 1):
            Town()
        if (T == 2):
            StatCheck()
        if (T == 3):
            Quests()
        if (T == 6):
            quit()
        
    def Town():
        TownEvent()
        print("Вы ходите по городу подмечая для себя некоторые места для ваших интересов")
        print("1. Таверна\n2. Магазин\n3. Кузня\n4. Больница\n5. У меня нет желания")
        T = int(input())
        
    def StatCheck():
        for keys, values in Character.items():
            print(keys)
            print(values)
        print()
        for keys, values in Stats.items():
            print(keys)
            print(values)
        print()
        for spellcards in Spells:
            print(spellcards)
        print("1. Выйти")
        T = int(input())
        if (T == 1):
            NormalGame()
            
    def DamageCheck():
        if (Character["Weapon"] == "Sword"):
            Stats["DMG"] = 2+4+math.trunc(power/0.5)
        if (Character["Weapon"] == "Spear"):
            Stats["DMG"] = 2+8+math.trunc(power/0.9)
    
    def Fight1():
        EnemyHP = 100
        EnemyDamage = 10
        EnemyPArmor = 0
        EnemyMArmor = 0
        Turn = 0
        while(Stats["HP"] >= 0 or EnemyHP >= 0):
            Turn = Turn+1
            print(f"Ход {Turn}")
            print(f"Большой жук ({EnemyHP}/100)")
            print("Ваши характеристики:")
            print(f'HP: {Stats["HP"]}/{maxhp}\nDamage: {Stats["DMG"]}')
            print("Ваш ход\n1. Атаковать оружием")
            T = int(input())
            if (T == 1):
                EnemyHP = EnemyHP-Stats["DMG"]
            print("Ход врага")
            EnemyAttack = random.randint(1,EnemyDamage)
            print(F"Жук атакует и наносит {EnemyAttack} урона!")
            Stats["HP"] = Stats["HP"]-EnemyAttack
            if (Stats["HP"] <= 0):
                print("Вы проиграли бой и вас увезли в  больницу")
                print("1. Продолжить\n2. Сдаться")
                T = int(input())
                if (T == 1):
                    Stats["HP"] = maxhp
                    NormalGame()
                    break
                if (T == 2):
                    quit()
            if (EnemyHP <= 0):
                print("Вы победили и получили 100 опыта")
                Stats["EXP"] = Stats["EXP"]+100
                print("Вернуться в город?")
                print("1. Да")
                T = int(input())
                if (T == 1):
                    NormalGame()
                    break
                    
    def Fight2():
        EnemyHP = 30
        EnemyDamage = 8
        EnemyPArmor = 0
        EnemyMArmor = 0
        Turn = 0
        while(Stats["HP"] >= 0 or EnemyHP >= 0):
            Turn = Turn+1
            print(f"Ход {Turn}")
            print(f"Волк ({EnemyHP}/30)")
            print("Ваши характеристики:")
            print(f'HP: {Stats["HP"]}/{maxhp}\nDamage: {Stats["DMG"]}')
            print("Ваш ход\n1. Атаковать оружием")
            T = int(input())
            if (T == 1):
                EnemyHP = EnemyHP-Stats["DMG"]
            print("Ход врага")
            EnemyAttack = random.randint(1,EnemyDamage)
            print(F"Волк атакует и наносит {EnemyAttack} урона!")
            Stats["HP"] = Stats["HP"]-EnemyAttack
            if (Stats["HP"] <= 0):
                print("Вы проиграли бой и вас увезли в  больницу")
                print("1. Продолжить\n2. Сдаться")
                T = int(input())
                if (T == 1):
                    Stats["HP"] = maxhp
                    NormalGame()
                    break
                if (T == 2):
                    quit()
            if (EnemyHP <= 0 and Stats["HP"] > 0):
                print("Вы победили и получили 20 опыта")
                Stats["EXP"] = Stats["EXP"]+20
                print("Вернуться в город?")
                print("1. Да")
                T = int(input())
                if (T == 1):
                    NormalGame()
                    break
            
            
    def Quests():
        print("Вы встали перед доской заданий решив выбрать для себя подходящую работу")
        print("1. Убийство жуков-гигантов\n2. Охота на волков\n3. Отказ")
        T = int(input())
        if (T == 1):
            Fight1()
        if (T == 2):
            Fight2()
        if (T == 3):
            NormalGame()
            
    def PowerCheck():
        Stats["Power"] = math.trunc(Stats["EXP"]/400)

if (T == 2):
    with open('save.json', 'r') as file:
        data = json.load(file)
    StarterCharacter()
    while (T != 6):
        DamageCheck()
        PowerCheck()
        NormalGame()