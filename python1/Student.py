from random import randint

class Student:
    def __init__(self, name):
        self.gladness = 50.0
        self.progress = 0
        self.isAlive = True
        self.energy = 100.0
        self.satiety = 44.0
        self.money = 10
        self.name = name

    def info(self):
        print(f"Name: {self.name} Money = {self.money}$")
        print(f"Stats:\n Gladness = {self.gladness} Progress = {self.progress}", end=" ")
        print(f"Energy: {self.energy} Satiety = {self.satiety}")

    def check_life(self):
        if self.energy <=0:
            self.isAlive = False
            print("нульова енергія, кінець гри :(")
        elif self.satiety <= 0:
            self.isAlive = False
            print("шкала голоду опустилася до нуля, а треба було їсти >:(")
        elif self.gladness <= 0:
            self.isAlive = False
            print("1000-7 ха-ха-ха")
        elif self.progress <= -0.5:
            self.isAlive = False
            print("ваша мати не рада цьому")
        elif self.money <= -12:
            self.isAlive = False
            print("колектори змусили вас побачити на цей світ з іншого боку...")

    def to_skip(self):
        answ = int(input("Скільки уроків ти пропустив?"))
        if answ <= 5 and answ >= 1:
            self.progress = self.progress - (answ / 10)
        else:
            print("incorrect skipped lesson")

    def to_study(self):
        print("U studdy")
        self.gladness -= randint(-5, 30)
        self.progress += 0.5

    def to_eat(self):
        print("Nyam nyam")
        ups = randint(-10, 10)
        self.satiety += ups
        if ups > 0:
            self.gladness += ups
        else:
            self.gladness -= ups
        ups = abs(ups) * -1
        self.money += ups

    def to_sleep(self):
        anw = int(input("How m time u sleep?"))
        if anw >= 1 and anw <= 16:
            self.gladness += anw / 2
            print("Zzz Zzz")
        else:
            print("Incorrect number, u mot sleep")
            self.gladness -= 20

    def to_work(self):
        anw = int(input("How m hours u work?"))
        if anw >= 8:
            self.money += 2
            self.energy -= 4
            self.satiety -= 5
            self.gladness -= 3

    def to_walk(self):
        anw = int(input("Скільки годин ти гулятимеш? "))
        if anw > 7:
            print("марафонець находився")
            self.energy -= 20
            self.satiety -= 15
            if self.energy <= 0 or self.satiety <= 0:
                self.isAlive = False
                print("На жаль, тобі відмовили ноги через втому і тебе забанили за афк")
        else:
            print("Ура ура гульки.")
            self.gladness += anw * 2
            self.energy -= anw * 5
            self.satiety -= anw * 3

    def to_travel(self):
        print("Нарешті відпочинок, чіназис")
        self.gladness += 20
        self.energy += 30
        self.satiety += 10
        self.money -= 50

    def to_hobby(self):
        anw = int(input("Скільки годин ти займаєшся своїм хобі? "))
        if anw <= 3:
            print("виконуєш хобі")
            self.gladness += anw * 4
            self.energy -= anw * 2
            self.money -= anw * 3
        else:
            print("вся мана була витрачена!")
            self.gladness += anw * 3
            self.energy -= anw * 4
            self.money -= anw * 5