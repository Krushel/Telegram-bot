
from datetime import datetime

from aiogram.utils.callback_data import CallbackData

import bot.sql.sql_utils as db

from aiogram.types import ReplyKeyboardRemove, \
        ReplyKeyboardMarkup, KeyboardButton, \
        InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    btn_year = KeyboardButton(text = '📆Найти по году', callback_data='yearfind')
    btn_ruler = KeyboardButton(text='🤴🏻Найти по правителю', callback_data='rulerfind')
    btn_collection = KeyboardButton(text='👛Моя коллекция', callback_data='user_collection')

    markup_menu = ReplyKeyboardMarkup()
    markup_menu.row(btn_year, btn_ruler)
    markup_menu.row(btn_collection)

    return markup_menu


def part_menu():
    btn_part1 = KeyboardButton(text = '1596-1750', callback_data='1596-1750')
    btn_part2 = KeyboardButton(text='1750-1917', callback_data='1750-1917')
    btn_part3 = KeyboardButton(text=f'1917-{datetime.now().year}', callback_data='part3')

    markup_menu = ReplyKeyboardMarkup()
    markup_menu.row(btn_part1, btn_part2)  # add about and exit bot ?
    markup_menu.row(btn_part3) # add categories and cart

    return markup_menu


def categ_menu(ruler):
    markup_categ = ReplyKeyboardMarkup()
    for category in db.show_categories(ruler=ruler): # add all categories
        btn_categ = KeyboardButton(text = category[0])
        markup_categ.insert(btn_categ)
    markup_categ.add(InlineKeyboardButton('Назад', callback_data='back_categ'))

    return markup_categ


def ruler_menu():
    markup_categ = ReplyKeyboardMarkup(resize_keyboard=True)
    markup_categ.add(InlineKeyboardButton('📆Найти по году', callback_data='back_categ'))
    markup_categ.add(InlineKeyboardButton('👛Моя коллекция', callback_data='back_categ'))
    for category in db.show_rulers(): # add all categories
        btn_categ = InlineKeyboardButton(text = f'{category.name}\n({category.yearstrt}-{category.yearend})')
        markup_categ.add(btn_categ)
    return markup_categ



def categi_menu(year):
    markup_categ = ReplyKeyboardMarkup()
    for category in db.show_categor(year): # add all categories
        btn_categ = KeyboardButton(text = category[0])
        markup_categ.insert(btn_categ)
    markup_categ.add(InlineKeyboardButton('Назад', callback_data='back_categ'))

    return markup_categ

# 3 level: print specific products
def products_buttons():
    btn_incr = InlineKeyboardButton('-', callback_data='decr')
    btn_decr = InlineKeyboardButton('+', callback_data='incr')
    btn_addcart = InlineKeyboardButton('В корзину', callback_data='addcart')
    btn_back_product = InlineKeyboardButton('Назад', callback_data='back_product')

    markup_product = InlineKeyboardMarkup().row(btn_incr, btn_decr) # add '+' and '-'
    markup_product.row(btn_addcart) # add to cart
    markup_product.row(btn_back_product) # add back and cart

    return markup_product

# cart
def cart_menu():
    btn_place = InlineKeyboardButton('Оформить заказ на', callback_data='place_order') # + srt (sum)
    '''
    btn_left = InlineKeyboardButton('<', callback_data='left') # flipping
    btn_quantity = InlineKeyboardButton('', callback_data='quantity') # to add pages
    btn_right = InlineKeyboardButton('>', callback_data='right')
    '''
    btn_empty_cart = InlineKeyboardButton('Очистить', callback_data='empty')
    btn_back_cart = InlineKeyboardButton('К товарам', callback_data='back_cart')

    markup_cart = InlineKeyboardMarkup(row_width=1)
    markup_cart.add(btn_place, btn_empty_cart, btn_back_cart)

    return markup_cart

def raler_menu(ruler):
    btn_ruler = InlineKeyboardButton(text = f"{ruler.name}\n{ruler.yearstrt}-{ruler.yearend}", callback_data='categ')
    markup_menu = InlineKeyboardMarkup()
    markup_menu.add(btn_ruler)
    return markup_menu
