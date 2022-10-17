import mysql.connector, random

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
        a = cursor.fetchone()

        if len(a) == 0:
            pass
        else:
            return a[0]

    def takeNumberFood():
        sql = f"SELECT number FROM foodrecords WHERE name = '{x}'"
        cursor.execute(sql)
        a = cursor.fetchone()

        if len(a) == 0:
            pass
        else:
            return a[0]

    return takePriceFood(), takeNumberFood()


def allFoods(db=openMysql()):
    liste = []
    cursor = db.cursor()
    sql = "SELECT name FROM foodrecords"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x[0])
    return liste


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


def listeArrangement():
    names = takeNames()
    numbers = collectionOfNumbers()
    numbersTwo = numbers.copy()
    newNames = []
    newNumbers = []
    for x in range(len(names)):
        bigNumber = max(numbers)
        index = numbersTwo.index(bigNumber)
        newNames.append(names[index])
        newNumbers.append(bigNumber)
        numbers.remove(bigNumber)
    return newNames, newNumbers


requests = {
    "border": -1,
    "cantsell": [],
    "discount": True,
    "discountStart": 0,
    "discountFinish": 70
}

newLists = listeArrangement()

if requests["discount"]:
    newLists[1][0] -= newLists[1][0] * ((random.randint(requests["discountStart"], requests["discountFinish"])) / 100)
    check = str(newLists[1][0]).split(".")
    if len(check) != 1:
        newLists[1][0] = check[0]

for x, y in zip(newLists[0], newLists[1]):
    a = foodDatas(x)
    # print(f"{x} den su kadar alınmıs {y} fiyati {a[0]} elde su kadar var {a[1]}")
    if x in allFoods():
        if a[1] > requests["border"]:
            if x not in requests["cantsell"]:
                print(x, y, end=" ")
            else:
                pass
        else:
            pass
    else:
        pass
