import mysql.connector

name = "arda"


def openMysql():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="", database="test")


def datas(db=openMysql()):
    cursor = db.cursor()

    def userFoodList():
        liste = []
        sql = f"SELECT names FROM foodhistory WHERE person = '{name}'"
        cursor.execute(sql)
        for x in cursor.fetchall():
            liste.append(x[0])
        return liste

    def userNumberList():
        liste = []
        sql = f"SELECT numbers FROM foodhistory WHERE person = '{name}'"
        cursor.execute(sql)
        for x in cursor.fetchall():
            liste.append(x[0])
        return liste

    return ",".join(userFoodList()).split(','), ",".join(userNumberList()).split(',')


def foodDatas(x):
    db = openMysql()
    cursor = db.cursor()

    def takePriceFood():
        sql = f"SELECT price FROM foodrecords WHERE name = '{x}'"
        cursor.execute(sql)
        return cursor.fetchone()[0]

    def takeNumberFood():
        sql = f"SELECT number FROM foodrecords WHERE name = '{x}'"
        cursor.execute(sql)
        return cursor.fetchone()[0]

    return takePriceFood(), takeNumberFood()


def takeNames():
    realList = datas()[0].copy()
    foodListe = realList.copy()
    nameList = []
    a = 0
    flag = 0
    while flag < len(realList):
        firstname = foodListe[a]
        if firstname not in nameList:
            nameList.append(firstname)
            a += 1
        else:
            a += 1
            flag -= 1
        flag += 1
        if a == len(realList):
            break
    return nameList


def allIndexNumbers():
    foodNameList = takeNames()
    realList = datas()[0].copy()
    allIndex = []
    for x in foodNameList:
        foodList = realList.copy()
        listem = []
        b = 0
        foodName = x
        number = foodList.count(foodName)
        for x in range(number):
            index = foodList.index(foodName)
            listem.append(index + b)
            foodList.pop(index)
            b += 1
        allIndex.append(listem)
    return allIndex


def collectionOfNumbers():
    def collectionForList():
        allNumbers = []
        for x in allIndexNumbers():
            liste = []
            for y in x:
                liste.append(datas()[1][y])
            allNumbers.append(liste)
        return allNumbers

    def collection():
        a = 0
        liste = []
        for x in collectionForList():
            a = 0
            for y in x:
                a = a + int(y)
            liste.append(a)
        return liste

    return collection()


for x, y in zip(takeNames(), collectionOfNumbers()):
    a = foodDatas(x)
    print(f"{x} den su kadar alınmıs {y} fiyati {a[0]} elde su kadar var {a[1]}")
