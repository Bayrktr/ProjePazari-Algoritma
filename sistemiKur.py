import mysql.connector


def openMysql():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="")


def connectSystem():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="", database="system")


def checkSystem():
    liste = []
    db = openMysql()
    cursor = db.cursor()
    sql = "SHOW DATABASES"
    cursor.execute(sql)
    for x in cursor:
        liste.append(x[0])
    return liste


if "system" in checkSystem():
    print("zaten var")
else:
    db = openMysql()
    cursor = db.cursor()
    sql = "CREATE DATABASE system"
    cursor.execute(sql)
    db.commit()
    db = connectSystem()
    cursor = db.cursor()
    sql = "CREATE TABLE companyrecords (name TEXT, password TEXT,code TEXT,mail TEXT,activity TEXT,fromip TEXT,crdate DATE)"
    cursor.execute(sql)
    db.commit()
    sql = "CREATE TABLE userrecords (name TEXT,password TEXT,mail TEXT,crdate DATE)"
    cursor.execute(sql)
    db.commit()
    sql = f"INSERT INTO companyrecords (name,password) VALUES ('admin','123')"
    cursor.execute(sql)
    db.commit()
