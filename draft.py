# python3

import subprocess  # Запуск приложений windows
import time  # работа со временем
import pyautogui as pg  # работа с картинками
import keyboard  # работа с нажатиями клавиш
import sys  # системными библиотеками
import datetime  # работа с датой и времени
from datetime import datetime
import sqlite3  # Импортируем библиотеку, соответствующую типу нашей базы данных
import random  # рандомные числа


def startlnk():  # функция запуска приложения
    subprocess.Popen('C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe')  # запуск приложения
    time.sleep(2)  # время ожидания запуска battle.net


def pointclick():  # функция произвольного нажатия в цикле
    pg.doubleClick(1599, 524)


def ss(template):  # функция определения и двойного нажатия на координаты кнопки
    global zero, activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        pg.doubleClick(buttonx, buttony)
        print(buttonx, buttony)
        time.sleep(1)
        return activity
    except TypeError:
        return zero


def simple_press(template):  # функция определения и двойного нажатия на координаты кнопки
    global activity, zero
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        pg.click(buttonx, buttony)
        print(buttonx, buttony)
        time.sleep(1)
        return activity
    except TypeError:
        return zero


def card_selection(template):  # функция определения и двойного нажатия на координаты кнопки
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        pg.click(buttonx, buttony)
        print(buttonx, buttony)
        activity = time.time()
        time.sleep(1)
        return  activity
    except TypeError:
        return zero


def start_game(template):
    global hod
    global Gcikl
    global Ggame
    global cikl
    global vygr
    global progr
    global zero
    global vygr
    global progr
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        Gcikl += 1
        hod = 1
        Ggame = 1
        cikl = 0
        vygr = 0
        progr = 0
        print("Старт игры")
        activity = time.time()
        time.sleep(1)
        return hod, Gcikl, Ggame, cikl, vygr, progr, activity
    except TypeError:
        return zero


def vash_hod(template):
    global game #индикатор своего хода
    global zero
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7)
        if game == 0:
            game = 1
            print("Старт хода")
            pg.moveTo(buttonx, buttony, duration=0)
            activity = time.time()
            time.sleep(1)
            return game, activity
    except TypeError:
        return zero


def chughoj_hod(template):
    global game
    global unit
    global hod
    global mana
    global zero
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        if game == 1:
            hod += 1
            game = 0
            unit = 0
        print("Ход противника")
        activity = time.time()
        time.sleep(5)
        if hod < 11:
            mana = hod
        elif hod >= 11:
            mana = 10
        return game, unit, hod, mana, activity
    except TypeError:
        return zero


def karta(template):  # функция покупки юнита
    global zero
    global unit
    global hod
    global game
    global moneta
    global mana
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 700, 1600, 200), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        activity = time.time()
        print('Нашел карту', buttonx, buttony)
        print("unit", unit)
        print("hod", hod)
        pg.press(['right'])
        if hod == 4 and unit == 0:
            moneta = 1
            print("Выложил монету на стол")
            pg.moveTo(buttonx, buttony, duration=0)  # перемещение к кнопке
            pg.mouseDown(button='left')  # нажать левую клавишу мыши
            pg.moveTo(969, 614, duration=1)  # перемещение
            pg.mouseUp(button='left')  # отпустить левую клавиши мыши
        if unit == 0 and hod > 3 and game == 1 and mana >= 5:
            print("Выложил одну карту на стол")
            pg.moveTo(buttonx, buttony, duration=0)  # перемещение к кнопке
            pg.mouseDown(button='left')  # нажать левую клавишу мыши
            pg.moveTo(969, 614, duration=1)  # перемещение
            pg.mouseUp(button='left')  # отпустить левую клавиши мыши
            unit += 1
        return unit, hod, game, moneta, mana, activity
    except TypeError:
        return zero


def health(template):  # функция лечения
    global zero, activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(800, 600, 400, 300), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        pg.press(['right'])
        print("лечение")
        pg.moveTo(buttonx, buttony, duration=0) #перемещение к кнопке
        pg.mouseDown(button='left') #нажать левую клавишу мыши
        pg.moveTo(800, buttony, duration=1) #перемещение
        pg.mouseUp(button='left') #отпустить левую клавиши мыши
        return activity
    except TypeError:
        return zero


def throw_a_ball(template):
    global zero, activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(800, 600, 400, 300), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        pg.press(['right'])
        print("метнуть шар")
        pg.moveTo(buttonx, buttony, duration=0)  # перемещение к кнопке
        pg.mouseDown(button='left')  # нажать левую клавишу мыши
        pg.moveTo(800, 170, duration=1)  # перемещение
        pg.mouseUp(button='left')  # отпустить левую клавиши мыши
        return activity
    except TypeError:
        return zero


def punch_in_the_face():
    global activity
    activity = time.time()
    pg.moveTo(800, 690, duration=0)  # перемещение к своему лицу
    pg.mouseDown(button='left')  # нажать левую клавишу мыши
    pg.moveTo(800, 170, duration=1)  # перемещение
    pg.mouseUp(button='left')  # отпустить левую клавиши мыши
    pg.click(button='right')  # нажать и отпустить правую клавишу
    return activity


def projgrysh(template):
    global zero
    global progr
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        progr = 1
        pg.moveTo(buttonx, buttony, duration=0)
        pg.doubleClick(buttonx, buttony)
        activity = time.time()
        time.sleep(2)
        return progr, activity
    except TypeError:
        return zero


def vyjgrysh(template):
    global zero
    global vygr
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        activity = time.time()
        vygr = 1
        pg.moveTo(buttonx, buttony, duration=0)
        pg.doubleClick(buttonx, buttony)
        time.sleep(1)
        return vygr, activity
    except TypeError:
        return zero


def endGame(template):
    global zero
    global Ggame
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        Ggame = 0
        print("Конец игры")
        pg.doubleClick(buttonx, buttony)
        time.sleep(1)
        return Ggame, activity
    except TypeError:
        return zero


def timer_game():
    global start_time
    now = datetime.datetime.now()
    loctime = format(time.time() - start_time)  # время в игре
    print(now)
    return now, loctime


def print_oll_table(): #функция вывода всей таблицы
    c.execute("SELECT * FROM total;")
    all_results = c.fetchall()
    for id in all_results:
        print(id[0], id[1], id[2], id[3], id[4], id[5], id[6], id[7], id[8], id[9], id[10], id[11], id[12], id[13], id[14],
              id[15], id[16], id[17], id[18], id[19], id[20],)
        conn.commit()  # применяем изменения


def load_table():
    c.execute("SELECT * FROM total  WHERE   name_id = (SELECT MAX(name_id)  FROM total);")
    result_old = c.fetchone()
    print(result_old) # выводит последнюю строку таблицы
    # for id in result_old: # выводит по одному все значения последней строки
    #     print(id)
    b = result_old[1]
    print(result_old[0])
    print(b)
    conn.commit()


def fill_table_start(): # заполняем строку таблицы
    c.execute("""INSERT INTO total(date, startgame, endgame, l_days, l_hours, l_minuts, l_seconds,
                g_days, g_hours, g_minuts, g_seconds, tipe, deck, hod, localvictory, locallosing,
                localpercent, globalvictory, globallosing, globalpercent)
                VALUES('01.01.2021', '00:00', '00.00', '0', '0', '0', '0',
                '0', '0', '0', '0', 'стандарт', 'жрец', '0' , '0', '0', '0', '0', '0', '0');""")
    conn.commit()


def fill_table(): # заполняем строку таблицы
    global now, localpercent
    global start_time
    global tipe
    global deck
    global vygr
    global progr
    global hod
    global activity
    date = start_time.strftime("%d.%m.%Y")
    startgame = start_time.strftime("%H:%M:%S")
    end_game = datetime.now()
    endgame = end_game.strftime("%H:%M:%S")

    loctime = end_game - start_time  # время в игре
    l_days = loctime.days  # дни
    l_hours = int(loctime.seconds / 3600)  # часы
    l_minuts = int((loctime.seconds - l_hours * 3600) / 60)  # минуты
    l_seconds = loctime.seconds - l_hours * 3600 - l_minuts * 60  # секунды
    if vygr == 0 and progr == 0:
        progr = 1
    if vygr == 1:
        localpercent = 'выйгрыш'
    if progr == 1:
        localpercent = 'пройгрыш'
    if (time.time() - activity) >= 300:
        localpercent = 'offline'
    c.execute("SELECT * FROM total  WHERE   name_id = (SELECT MAX(name_id)  FROM total);")
    result_old = c.fetchone()
    print(result_old)

    g_days = result_old[8] + l_days  # дни
    g_hours = result_old[9] + l_hours  # часы
    g_minuts = result_old[10] + l_minuts  # минуты
    g_seconds = result_old[11] + l_seconds  # секунды

    if g_seconds >= 60:
        g_minuts = g_minuts + int(g_seconds / 60)
        g_seconds = g_seconds - (int(g_seconds / 60))*60
    if g_minuts >= 60:
        g_hours = g_hours  + int(g_minuts / 60)
        g_minuts = g_minuts - (int(g_minuts / 60))*60
    if g_hours >= 24:
        g_days = g_days  + int(g_hours / 24)
        g_hours = g_hours - (int(g_hours / 24))*24


    localvictory = vygr
    locallosing = progr
    globalvictory = result_old[18] + vygr
    globallosing = result_old[19] + progr
    globalpercent = round(((globalvictory / (globalvictory + globallosing)) * 100), 2)
    c.execute("""INSERT INTO total(date, startgame, endgame, l_days, l_hours, l_minuts, l_seconds, 
                g_days, g_hours, g_minuts, g_seconds, tipe, deck, hod, localvictory, locallosing,
                    localpercent, globalvictory, globallosing, globalpercent) 
                    VALUES(?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?);""",
              (date, startgame, endgame, l_days, l_hours, l_minuts, l_seconds,
               g_days, g_hours, g_minuts, g_seconds, tipe, deck, hod, localvictory, locallosing,
               localpercent, globalvictory, globallosing, globalpercent))
    conn.commit()



def lock_standart():
    global Ggame
    global Ngame
    global Gcikl
    global game
    global hod
    global mana
    global moneta
    global tipe
    global deck
    global vygr
    global progr
    global cikl
    global unit
    global start_time
    global delay
    global activity
    tipe = 'стандарт'
    deck = 'лок'
    ss("btn_lock.png")
    ss("btn_game_st.png")
    start_game("btn_start.png")
    if Ggame == 1:
        Ngame += 1
        print("игра локом началась", Gcikl)
        start_time = datetime.now()  # текущие дата и время
        while Ggame == 1:
            if keyboard.is_pressed('Enter'): # если клавиша Esc
                timer_game() #подсчет времени
                fill_table() #заполняем БД
                print_oll_table()
                sys.exit()  # завершаем программу
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            card_selection("btn_ok.png")
            chughoj_hod("chughoj_hod.png")
            vash_hod("btn_end.png")
            print("hod=", hod)
            if hod == 1 and game == 1:
                close_time = time.time() + 15
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                simple_press("btn_end.png")
                simple_press("btn_end2.png")
            elif hod > 1 and hod < 4 and game == 1:
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta("btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta("btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    pg.press(['right'])
                    simple_press("btn_soul.png")
                    mana = 0
                simple_press("btn_end.png")
                simple_press("btn_end2.png")
            elif hod == 4 and game == 1:
                pg.press(['right'])
                karta("btn_m0.png")
                if moneta == 1:
                    mana += 1
                    moneta = 0
                    pg.press(['right'])
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta("btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta("btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta("btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    pg.press(['right'])
                    simple_press("btn_soul.png")
                    mana = 0
                simple_press("btn_end.png")
                simple_press("btn_end2.png")
            elif hod == 5 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta("btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta("btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta("btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    pg.press(['right'])
                    simple_press("btn_soul.png")
                    mana = 0
                simple_press("btn_end.png")
                simple_press("btn_end2.png")
            elif hod == 6 and game == 1:
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta("btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta("btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta("btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if unit == 0 and mana >= 6:
                        pg.press(['right'])
                        karta("btn_m6.png")
                        if unit == 1:
                            mana = mana - 6
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    pg.press(['right'])
                    simple_press("btn_soul.png")
                    mana = 0
                simple_press("btn_end.png")
                simple_press("btn_end2.png")
            elif hod >= 7 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta("btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta("btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta("btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if unit == 0 and mana >= 6:
                        pg.press(['right'])
                        karta("btn_m6.png")
                        if unit == 1:
                            mana = mana - 6
                    if unit == 0 and mana >= 7:
                        pg.press(['right'])
                        karta("btn_m6.png")
                        if unit == 1:
                            mana = mana - 7
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    pg.press(['right'])
                    simple_press("btn_soul.png")
                    mana = 0
                simple_press("btn_end.png")
                simple_press("btn_end2.png")
            projgrysh("end_game.png")
            vyjgrysh("victory.png")
            endGame("end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
 #               print_oll_table()
            ss("bt.png")
            ss("bt2.png")
        return  Ggame, Ngame, Gcikl, vygr, progr, start_time, activity


def activity_analysis():
    global activity
    if (time.time() - activity) >= 420:
        simple_press("btn_gear.png")
        simple_press("btn_exit.png")
        simple_press("btn_connect_again.png")
        time.sleep(600)
    return activity



# variables (переменные)
Ngame = 0  # подсчет количества игр !(основное тело цикла)
vygr = 0  # подсчет выйгрышей в данной сессии
progr = 0  # подсчет проигранных игр в данной сессии
Ggame = 0  # индикатор начала рейтинговой игры !start_game()-->1, endGame()-->0
Gcikl = 0  # счетчик циклов внутри игры
cikl = 1  # подсчет общего числа циклов программы
hod = 0  # учет номера хода !start_game()-->1 !chughoj_hod()-->+1
unit = 0  # количество выложенных юнитов за ход (для того что бы знать сколько выложено)
game = 0  # индикатор игры (вашего хода)
moneta = 0  # индикатор монеты в руке
mana = 0  # счетчик маны во время хода
zero = 0  # ноль
delay = 25  # вемя на свой ход
activity = time.time()  # анализ активности игрового процесса


# Работа с БД
conn = sqlite3.connect('mydatabase.db')  # создаем переменную conn и  соединение с нашей базой данных
c = conn.cursor()  # Создаем курсор - это специальный объект который делает запросы и получает их результаты
c.execute("""CREATE TABLE IF NOT EXISTS total(
   name_id INTEGER PRIMARY KEY,
   date DATE NOT NULL,
   startgame DATE NOT NULL,
   endgame DATE NOT NULL,
   l_days DATE NOT NULL,
   l_hours DATE NOT NULL,
   l_minuts DATE NOT NULL,
   l_seconds DATE NOT NULL,
   g_days DATE NOT NULL,
   g_hours DATE NOT NULL,
   g_minuts DATE NOT NULL,
   g_seconds DATE NOT NULL,
   tipe TEXT NOT NULL,
   deck TEXT NOT NULL,
   hod INT NOT NULL,
   localvictory INT NOT NULL,
   locallosing INT NOT NULL,
   localpercent TEXT NOT NULL,
   globalvictory INT NOT NULL,
   globallosing INT NOT NULL,
   globalpercent REAL NOT NULL);
""")
conn.commit()  # применяем изменения


# исполняемый код
startlnk()  # запуск приложения Battle.net

#fill_table_start()

while "Бесконечный цикл":  # Цикл анализа
    if keyboard.is_pressed('Enter'):  # если клавиша Esc
        print_oll_table()
        sys.exit()  # завершаем программу
    cikl += 1
    print("Цикл =", cikl)
    print("Колличество игр ", Ngame)
    print("Пройгрыш", progr)
    print("Выйгрыш", vygr)
    time.sleep(5)
    ss("00_btn_game.png")
    ss("btn_game.png")
    lock_standart()
    # На случай потери соединения
    ss("bt.png")
    ss("bt2.png")
    pointclick()
    activity_analysis()