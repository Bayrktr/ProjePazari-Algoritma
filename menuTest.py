import mysql.connector, random, sys
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QMainWindow, QLabel, QComboBox

name = "arda"


def openMysql():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="", database="test")


def allMenuDatas():
    liste = []
    db = openMysql()
    cursor = db.cursor()
    sql = "SELECT * FROM menuoptions WHERE flag = '1'"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x)
    db.close()
    return liste


data = allMenuDatas()
if len(data) == 0:
    print("Seçili menü yok")
else:
    data = data[0]
    data = list(data)
    print(data)
    backgroundOptions = {
        "height": int(data[1]),
        "widght": int(data[2]),
        "fontColor": str(data[3]),
        "titleColor": str(data[4]),
        "fontType": str(data[5]),
        "categoryBetween": int(data[8]),
        "fontSize": int(data[6]),
        "titleSize": int(data[7]),
        "startX": int(data[9]),
        "startY": int(data[10]),
        "fontBetweenSize": int(data[11]),
        "titleBetweenSizeX": int(data[12]),
        "titleBetweenSizeY": int(data[13]),
        "PriceColor": str(data[14]),
        "unitName": str(data[15])
    }

requests = {
    "border": 0,
    "cantsell": [],
    "discount": True,
    "discountStart": 0,
    "discountFinish": 70
}


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


def allFoodNameList(db):
    liste = []
    cursor = db.cursor()
    sql = "SELECT name FROM foodrecords"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x[0])
    return liste


def foodDatas(x):
    db = openMysql()
    cursor = db.cursor()

    def takePriceFood():
        liste = []
        sql = f"SELECT price FROM foodrecords WHERE name = '{x}'"
        cursor.execute(sql)
        for y in cursor.fetchall():
            liste.append(y[0])
        return liste

    def takeNumberFood():
        liste = []
        sql = f"SELECT number FROM foodrecords WHERE name = '{x}'"
        cursor.execute(sql)
        for y in cursor.fetchall():
            liste.append(y[0])
        return liste

    return takePriceFood(), takeNumberFood()


def allFoods(db=openMysql()):
    liste = []
    cursor = db.cursor()
    sql = "SELECT name FROM foodrecords"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x[0])
    return liste


def allCategorys(db):
    liste = []
    cursor = db.cursor()
    sql = "SELECT name FROM categoryrecords"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x[0])
    return liste


def takeNames():
    realList = datas()[0].copy()
    foodListe = realList.copy()
    nameList = []
    for x in range(len(realList)):
        name = foodListe[x]
        if name not in nameList:
            nameList.append(name)
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
    newNames = []
    newNumbers = []
    for x in range(len(names)):
        bigNumber = max(numbers)
        name = names[numbers.index(bigNumber)]
        newNames.append(str(name))
        newNumbers.append(int(bigNumber))
        numbers.remove(bigNumber)
        names.remove(name)
    print(newNames, newNumbers)
    return newNames, newNumbers


def listeArrangementCategory(listOfNeed):
    names = algorithm(listOfNeed)
    print(names)
    numbers = names[1]
    names = names[0]
    newNames = []
    newNumbers = []
    for x in range(len(names)):
        bigNumber = max(numbers)
        name = names[numbers.index(bigNumber)]
        newNames.append(str(name))
        newNumbers.append(int(bigNumber))
        numbers.remove(bigNumber)
        names.remove(name)
    print(newNames, newNumbers)
    return newNames, newNumbers


def algorithm(listOfNeed):
    def bestCategoryList():
        db = openMysql()
        cursor = db.cursor()
        allCategory = []
        categorysNumber = []

        def categoryName(x):
            liste = []
            sql = f"SELECT category FROM foodrecords WHERE name = '{x}'"
            cursor.execute(sql)
            for y in cursor.fetchall():
                liste.append(y[0])
            return liste[0], listOfNeed[1][listOfNeed[0].index(x)]

        for x in listOfNeed[0]:
            if x not in allFoodNameList(db):
                pass
            else:
                content = categoryName(x)
                if content[0] not in allCategory:
                    allCategory.append(content[0])
                    categorysNumber.append(content[1])
                else:
                    newNumber = int(categorysNumber[allCategory.index(content[0])]) + int(content[1])
                    categorysNumber[allCategory.index(content[0])] = newNumber

        return allCategory, categorysNumber

    return bestCategoryList()


def categoryName(db, y):
    cursor = db.cursor()
    liste = []
    sql = f"SELECT category FROM foodrecords WHERE name = '{y}'"
    cursor.execute(sql)
    for y in cursor.fetchall():
        liste.append(y[0])
    return liste


def addEmptyArg():
    db = openMysql()
    newLists = listeArrangement()
    categoryList = listeArrangementCategory(newLists)
    print(newLists, categoryList)
    for x in allFoodNameList(db):
        if x not in newLists[0]:
            newLists[0].append(str(x))
            newLists[1].append(int(0))
    for x in allCategorys(db):
        if x not in categoryList[0]:
            categoryList[0].append(str(x))
            categoryList[1].append(int(0))
    return newLists, categoryList


a = addEmptyArg()
newLists, categoryList = a[0], a[1]
print(newLists, categoryList)


class menuBackground(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MENU")
        self.background()
        self.texts()

    def background(self):
        label = QLabel(self)
        pixmap = QPixmap('Sarı Örgülü Mutlu Kahvaltı Yumurtalar Restoran Menü (3).png')
        label.setPixmap(pixmap)
        self.resize(backgroundOptions["widght"], backgroundOptions["height"])

    def texts(self):
        global extraCategoryList
        db = openMysql()
        print(newLists, categoryList)
        flag = 0
        startX = backgroundOptions["startX"]
        startY = 250
        extraCategoryList = []
        for x in categoryList[0]:
            if flag == backgroundOptions["categoryBetween"]:
                startY += backgroundOptions["titleBetweenSizeY"]
                startX = backgroundOptions["startX"]
                flag = 0
            if startY + backgroundOptions["titleBetweenSizeY"] > backgroundOptions["height"]:
                extraCategoryList.append(str(x))
                print(extraCategoryList)
            else:
                label = QLabel(f"{x}", self)
                label.setGeometry(startX, startY, 200, 50)
                label.setFont(QFont('Times', backgroundOptions["titleSize"]))
                label.setStyleSheet("color:{};".format(backgroundOptions["titleColor"]))
                label2 = QLabel("{}".format(backgroundOptions["unitName"]), self)
                label2.setGeometry(startX + 80, startY + 12, 150, 25)
                label2.setFont(QFont('Times', backgroundOptions["titleSize"]))
                label2.setStyleSheet("color:{};".format(backgroundOptions["PriceColor"]))
                foodY = startY + 10
                for y in newLists[0]:
                    category = categoryName(db, y)
                    price = foodDatas(y)[0]
                    if len(category) == 0:
                        pass
                    elif category[0] == str(x):
                        foodY += backgroundOptions["fontBetweenSize"]
                        label = QLabel(f"{y}", self)
                        label.setGeometry(startX, foodY, 150, 25)
                        label.setFont(QFont('Times', backgroundOptions["fontSize"]))
                        label.setStyleSheet("color:{};".format(backgroundOptions["fontColor"]))
                        label = QLabel(f"{price[0]}", self)
                        label.setGeometry(startX + 80, foodY, 40, 25)
                        label.setFont(QFont('Times', backgroundOptions["fontSize"]))
                        label.setStyleSheet("color:{};".format(backgroundOptions["fontColor"]))
                    else:
                        pass
                startX += backgroundOptions["titleBetweenSizeX"]
                flag += 1
        if len(extraCategoryList) != 0:
            secondPageButton = QPushButton("Next Page", self)
            secondPageButton.setGeometry(500, 750, 100, 50)
            secondPageButton.setStyleSheet("QPushButton"
                                           "{"
                                           "background-color : gray;"
                                           "}"
                                           "QPushButton::pressed"
                                           "{"
                                           "background-color : black;"
                                           "}"
                                           )
            secondPageButton.clicked.connect(self.openSecondPage)

    def openSecondPage(self):
        self.hide()
        self.secondPagePart = secondPage()
        self.secondPagePart.show()


class secondPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SecondPage")
        label = QLabel(self)
        pixmap = QPixmap('Koyu Kahverengi Kupalar Kahve Dükkanı Menü.png')
        label.setPixmap(pixmap)
        self.resize(600, 800)
        firstPageButton = QPushButton("Back Page", self)
        firstPageButton.setGeometry(0, 750, 100, 50)
        firstPageButton.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : white;"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color : black;"
                                      "}"
                                      )
        firstPageButton.clicked.connect(self.turnBackFirstPage)
        self.text()

    def text(self):
        global extraCategoryList
        flag = 0
        startX = backgroundOptions["startX"]
        startY = backgroundOptions["startY"]
        db = openMysql()
        print(extraCategoryList)
        self.liste = []
        for x in extraCategoryList:
            print(x)
            if flag == backgroundOptions["categoryBetween"]:
                startY += backgroundOptions["titleBetweenSizeY"]
                startX = 30
                flag = 0
            if startY + backgroundOptions["titleBetweenSizeY"] > backgroundOptions["height"]:
                self.liste.append(str(x))
                print(extraCategoryList)
            else:
                label = QLabel(f"{x}", self)
                label.setGeometry(startX, startY, 200, 50)
                label.setFont(QFont('{}'.format(backgroundOptions["fontType"]), backgroundOptions["titleSize"]))
                label.setStyleSheet("color:{};".format(backgroundOptions["titleColor"]))
                label2 = QLabel("{}".format(backgroundOptions["unitName"]), self)
                label2.setGeometry(startX + 80, startY + 12, 150, 25)
                label2.setFont(QFont('{}'.format(backgroundOptions["fontType"]), backgroundOptions["titleSize"]))
                label2.setStyleSheet("color:{};".format(backgroundOptions["PriceColor"]))
                foodY = startY + 10
                for y in newLists[0]:
                    category = categoryName(db, y)
                    price = foodDatas(y)[0]
                    if len(category) == 0:
                        pass
                    elif category[0] == str(x):
                        foodY += backgroundOptions["fontBetweenSize"]
                        label = QLabel(f"{y}", self)
                        label.setGeometry(startX, foodY, 150, 25)
                        label.setFont(QFont('{}'.format(backgroundOptions["fontType"]), backgroundOptions["fontSize"]))
                        label.setStyleSheet("color:{};".format(backgroundOptions["fontColor"]))
                        label = QLabel(f"{price[0]}", self)
                        label.setGeometry(startX + 80, foodY, 40, 25)
                        label.setFont(QFont('{}'.format(backgroundOptions["fontType"]), backgroundOptions["fontSize"]))
                        label.setStyleSheet("color:{};".format(backgroundOptions["fontColor"]))
                    else:
                        pass
                startX += backgroundOptions["titleBetweenSizeX"]
                flag += 1
        print(self.liste)
        if len(self.liste) != 0:
            secondPageButton = QPushButton("Next Page", self)
            secondPageButton.setGeometry(500, 750, 100, 50)
            secondPageButton.setStyleSheet("QPushButton"
                                           "{"
                                           "background-color : gray;"
                                           "}"
                                           "QPushButton::pressed"
                                           "{"
                                           "background-color : black;"
                                           "}"
                                           )
            secondPageButton.clicked.connect(self.openSecondPage)

    def openSecondPage(self):
        global extraCategoryList
        extraCategoryList = self.liste.copy()
        self.hide()
        self.secondPagePart = secondPage()
        self.secondPagePart.show()

    def turnBackFirstPage(self):
        self.hide()
        self.firstPagePart = menuBackground()
        self.firstPagePart.show()




if __name__ == "__main__":
    if len(data) != 0:
        app = QApplication(sys.argv)
        oMainwindow = menuBackground()
        oMainwindow.show()
        sys.exit(app.exec_())
