import mysql.connector
from datetime import datetime
import random, string

users = ["emir", "arda", "talha"]
foods = ["sut", "supangle", "sutlac", "cikolata"]
categorys = ["sicak", "soguk", "tatli"]
deskNumber = "10"


def openMysql():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="", database="test")


def createCode(alphabet=string.ascii_lowercase, numbers=string.digits):
    a = 0
    liste = []
    alphabet = list(alphabet)
    numbers = list(numbers)
    alphabet = alphabet + numbers
    while a < 12:
        a += 1
        liste.append(random.choice(alphabet))
    return "".join(liste)


def timeSettings(now=datetime.today()):
    timeNow = []
    timeNow.append(str(now.year)), timeNow.append(str(now.month)), timeNow.append(str(now.day)), timeNow.append(
        str(now.hour)), timeNow.append(str(now.minute))
    return ".".join(timeNow)


def InsertTable():
    def insertFoodInfo():
        def randomPrice():
            return random.randint(10, 25)

        def foodCheck(x):
            liste = []
            sql = f"SELECT name FROM foodrecords"
            cursor.execute(sql)
            for y in cursor.fetchall():
                liste.append(y[0])
            if x in liste:
                return False
            else:
                return True

        for x in foodNameSingle.split(","):
            if foodCheck(x):
                sql = f"INSERT INTO foodrecords (name,price,category,code,number,crdate) VALUES ('{x}','{randomPrice()}','{random.choice(categorys)}','{createCode()}','0','{timeSettings()}')"
                cursor.execute(sql)
                db.commit()
            else:
                print("Zaten var")

    db = openMysql()
    cursor = db.cursor()
    for x in range(10, 40):
        name = random.choice(users)
        foodName = foodList()
        foodNameSingle = foodName[0]
        foodNameNumber = foodName[1]
        sql = f"INSERT INTO foodhistory (person,names,numbers,desknumber,crdate) VALUES ('{name}','{foodNameSingle}','{foodNumbers(foodNameNumber)}','{deskNumber}','{timeSettings()}')"
        cursor.execute(sql)
        db.commit()
        possibility = random.randint(1, 2)
        if possibility == 1:
            insertFoodInfo()
        else:
            pass


def foodList():
    liste = []
    newFoods = foods.copy()
    for x in range(0, len(foods), random.randint(1, len(foods))):
        food = random.choice(newFoods)
        liste.append(food)
        newFoods.remove(f'{food}')
    return ",".join(liste), len(liste)


def foodNumbers(foodNameNumber):
    liste = []
    for x in range(foodNameNumber):
        liste.append(str(random.randint(1, 15)))
    return ",".join(liste)


if __name__ == "__main__":
    InsertTable()
