import sqlite3
from sqlite3 import Error
import bot.sql.sql_utils as db
class Ruler:
    def __init__(self, name, yearstrt, yearend, img):
        self.name = name
        self.yearstrt = yearstrt
        self.yearend = yearend
        self.img = img


class Category:
    def __init__(self, name):
        self.name = name

class Coin:
    def __init__(self, name, img, year):
        self.name = name
        self.img = img
        self.year = year
    def __repr__(self):
        return f'{self.name},{self.img}'

class Mroduct:
    def __init__(self, ruler, dvor, name, year, price, rarity, variation, img, proba, novo):
        self.ruler = ruler
        self.dvor = dvor
        self.price = price
        self.rarity = rarity
        self.variation = variation
        self.proba = proba
        self.novo = novo
        self.name = name
        self.img = img
        self.year = year
    def __repr__(self):
        return f'{self.name},{self.img}'


class Product:
    def __init__(self, ruler, dvor, name, year, price, rarity, variation, img, chesh, front, back, proba, novo, valuable):
        self.ruler = ruler
        self.dvor = dvor
        self.price = price
        self.rarity = rarity
        self.variation = variation
        self.chesh = chesh
        self.front = front
        self.back = back
        self.proba = proba
        self.novo = novo
        self.valuable = valuable
        self.name = name
        self.img = img
        self.year = year
    def __repr__(self):
        return f'{self.name},{self.img}'

def show_categories(ruler):
    try:
        conn = sqlite3.connect("D:/Downloads/tcarcoins.db")
        cursor = conn.cursor()
        query = """
        SELECT nominalImageName
        FROM coins
        """
        cursor.execute(query)
        categoriesdb = cursor.fetchall()
        categories = []
        for category in categoriesdb:
            category = Category(category[0].strip())
            categories.append(category)
    except Error:
        print(Error)
    finally:
        conn.close()

    return categories

def show_rulers():
    print(1)
    try:
        if True == True:
            conn = sqlite3.connect("C:/Users/user/data.sqlite")
            cursor = conn.cursor()
            query = """
            SELECT name, yearstrt, yearend, img
            FROM rulers
            ORDER BY
            yearstrt DESC;
            """
            cursor.execute(query)
            rulersdb = cursor.fetchall()
            rulers = []
            for ruler in rulersdb:
                ruler = Ruler(ruler[0], str(ruler[1].replace(".0","")), str(ruler[2].replace(".0","")), ruler[3])
                rulers.append(ruler)





# def show_rulers(part):
#     print(part)
#     try:
#         if part == '1596-1750':
#             conn = sqlite3.connect("C:/Users/user/data.sqlite")
#             cursor = conn.cursor()
#             query = """
#             SELECT name, yearstrt
#             FROM rulers
#             WHERE yearstrt BETWEEN 1595 and 1750;
#             """
#             cursor.execute(query)
#             rulersdb = cursor.fetchall()
#             rulers = []
#             for ruler in rulersdb:
#                 # ruler = Ruler()
#                 rulers.append(ruler[0])
#         elif part == '1750-1917':
#             conn = sqlite3.connect("C:/Users/user/data.sqlite")
#             cursor = conn.cursor()
#             query = """
#             SELECT name, yearstrt
#             FROM rulers
#             WHERE yearstrt BETWEEN 1740 and 1917;
#             """
#             cursor.execute(query)
#             rulersdb = cursor.fetchall()
#             rulers = []
#             for ruler in rulersdb:
#                 rulers.append(ruler[0])
#         else:
#             conn = sqlite3.connect("C:/Users/user/data.sqlite")
#             cursor = conn.cursor()
#             query = """
#             SELECT name, yearstrt
#             FROM rulers
#             WHERE yearstrt BETWEEN 1917 and 2020;
#             """
#             cursor.execute(query)
#             rulersdb = cursor.fetchall()
#             rulers = []
#             for ruler in rulersdb:
#                 rulers.append(ruler[0])
            for i in rulers:
                print(f'{i.name}({i.yearstrt}-{i.yearend})')

    except Error:
        print(Error)
    finally:
        conn.close()

    return rulers


# def show_categories(ruler):
#     print(ruler)
#     try:
#         conn = sqlite3.connect("C:/Users/user/cat.sqlite")
#         cursor = conn.cursor()
#         query = """
#         SELECT name, img
#         FROM categories
#         WHERE ruler =:ruler
#         ORDER BY
#         name;
#         """
#         cursor.execute(query, {'ruler': ruler})
#         categoriesdb = cursor.fetchall()
#         categories = []
#         for category in categoriesdb:
#             category = Category(category[0], category[1])
#             categories.append(category)
#     except Error:
#         print(Error)
#     finally:
#         conn.close()
#
#     return categories


def show_categor(year):
    try:
        conn = sqlite3.connect("C:/Users/user/coins.db")
        cursor = conn.cursor()
        query = """
        SELECT DISTINCT category 
        FROM coins
        WHERE year =:year
        ORDER BY
        ruler;
        """
        cursor.execute(query, {'year': year})
        coins = cursor.fetchall()
        print(coins)
        if coins == []:
            conn = sqlite3.connect("C:/Users/user/newcoins.db")
            cursor = conn.cursor()
            query = """
                    SELECT DISTINCT category 
                    FROM coins
                    WHERE year =:year
                    """
            cursor.execute(query, {'year': year})
            coins = cursor.fetchall()
    except Error:
        print(Error)
    finally:
        conn.close()

    return coins


def show_coins(ruler, category):
    try:
        conn = sqlite3.connect("C:/Users/user/coins.db")
        cursor = conn.cursor()
        query = """
        SELECT coinName, imageName, year
        FROM coins
        WHERE ruler =:ruler and category =:category
        """
        cursor.execute(query, {'ruler': ruler, 'category':category})
        coinsdb = cursor.fetchall()
        coins = []
        for coin in coinsdb:
            coin = Coin(coin[0], coin[1], coin[2])
            print(coin.name, coin.img)
            coins.append(coin)
        if coins == []:
            conn = sqlite3.connect("C:/Users/user/newcoins.db")
            cursor = conn.cursor()
            query = """
                    SELECT coinName, imageName, year
                    FROM coins
                    WHERE ruler =:ruler and category =:category
                    """
            cursor.execute(query, {'ruler': ruler, 'category': category})
            coinsdb = cursor.fetchall()
            for coin in coinsdb:
                coin = Coin(coin[0], coin[1], coin[2])
                coins.append(coin)

    except Error:
        print(Error)
    finally:
        conn.close()
    print(f'hui{coins}')
    return coins


def show_coin(img):
    try:
        conn = sqlite3.connect("C:/Users/user/coins.db")
        cursor = conn.cursor()
        query = """
        SELECT ruler, dvor, coinName, year, price, rarity, variation, imageName, isCheshuya, front, back, isProbnaya, isNovodel, isValuable
        FROM coins
        WHERE imageName =:img
        """
        cursor.execute(query, {'img': img})
        coinsdb = cursor.fetchall()
        coins = []
        for coin in coinsdb:
            coin = Product(coin[0], coin[1], coin[2], coin[3], coin[4], coin[5], coin[6], coin[7], coin[8], coin[9], coin[10], coin[11], coin[12], coin[13])
            print(coin.name, coin.img)
            coins.append(coin)
        if coins == []:
            conn = sqlite3.connect("C:/Users/user/newcoins.db")
            cursor = conn.cursor()
            query = """
                    SELECT ruler, dvor, coinName, year, price, rarity, variation, imageName, isProbnaya, isNovodel
                    FROM coins
                    WHERE imageName =:img
                    """
            cursor.execute(query, {'img': img})
            coinsdb = cursor.fetchall()
            for coin in coinsdb:
                coin = Mroduct(coin[0], coin[1], coin[2], coin[3], coin[4], coin[5], coin[6], coin[7], coin[8], coin[9])
                coins.append(coin)

    except Error:
        print(Error)
    finally:
        conn.close()
    print(f'hui{coins}')
    return coins
# def show_coin():
#     try:
#         conn = sqlite3.connect("C:/Users/user/ussrcoins.db")
#         cursor = conn.cursor()
#         query = """
#         SELECT *
#         FROM coins;
#         """
#         cursor.execute(query)
#         coins = cursor.fetchall()
#     except Error:
#         print(Error)
#     finally:
#         conn.close()
#
#     return coins

# import os
# from os.path import join
# for i in db.show_coin():
#     img = str(i[10])
#     img = img + '_min1.jpeg'
#     print(img)
#     lookfor = img
#     file_list = os.listdir('C:/Users/user/min1')
#     if lookfor in file_list:
#         print (1)
#         break

def show_images():
    try:
        conn = sqlite3.connect("D:/Downloads/tcarcoins.db")
        cursor = conn.cursor()
        query = """
        SELECT imageName
        FROM coins
        """
        cursor.execute(query)
        coins = cursor.fetchall()
    except Error:
        print(Error)
    finally:
        conn.close()

    return coins
for img in db.show_images():
    try:
        photo = open(f'D:/Programming/coins_telegram1/images/full/{img[0]}_full.jpeg', 'rb')
    except:
        print(img[0])
        continue