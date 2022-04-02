import mysql.connector

dontDel = ["system","performance_schema", "information_schema", "phpmyadmin", "mysql"]


def openMysql():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="")


def openmysqlTwo():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="", database="system")


def takaDBnames():
    liste = []
    db = openMysql()
    cursor = db.cursor()
    sql = "SHOW DATABASES"
    cursor.execute(sql)
    for x in cursor:
        liste.append(x[0])
    for x in dontDel:
        liste.remove(x)
    return liste


def takeCompanyNames():
    liste = []
    db = openmysqlTwo()
    cursor = db.cursor()
    sql = f"SELECT name FROM companyrecords"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x[0])
    liste.remove("admin")
    return liste


db = openMysql()
cursor = db.cursor()
for x in takaDBnames():
    sql = f"DROP DATABASE {x}"
    cursor.execute(sql)
db = openmysqlTwo()
cursor = db.cursor()
for x in takeCompanyNames():
    sql = f"DELETE FROM companyrecords WHERE name = '{x}'"
    cursor.execute(sql)
    db.commit()
