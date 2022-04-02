import mysql.connector
from datetime import datetime
import random

users = ["emir", "arda", "talha"]
foods = ["sut", "supangle", "sutlac"]
deskNumber = "10"


def openMysql():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="", database="test")


def timeSettings(now=datetime.today()):
    timeNow = []
    timeNow.append(str(now.year)), timeNow.append(str(now.month)), timeNow.append(str(now.day)), timeNow.append(
        str(now.hour)), timeNow.append(str(now.minute))
    return ".".join(timeNow)


def InsertTable():
    db = openMysql()
    cursor = db.cursor()
    for x in range(10, 100, random.randint(1, 3)):
        name = random.choice(users)
        foodName = foodList()
        sql = f"INSERT INTO foodhistory (person,names,numbers,desknumber,crdate) VALUES ('{name}','{foodName}','{x}','{deskNumber}','{timeSettings()}')"
        cursor.execute(sql)
        db.commit()


def foodList():
    liste = []
    newFoods = foods.copy()
    for x in range(0, 3, random.randint(1, 2)):
        food = random.choice(newFoods)
        liste.append(food)
        newFoods.remove(f'{food}')
    return ",".join(liste)


if __name__ == "__main__":
    InsertTable()
