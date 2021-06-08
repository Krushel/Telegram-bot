import os

class Coin:
    def __init__(self, id, ruler, dvor, category, name, year,
                 variation, material, tyrazh, weight, diameter,
                 gurt, desription, priceVf, priceXf, imageName, nominallmageName,
                 udid, isCheshuya, front, back, isProbnaya, isNovodel,
                 isValuable, additionallmages):
        self.id = id
        self.ruler = ruler
        self.dvor = dvor
        self.category = category
        self.name = name
        self.year = year
        self.variation = variation
        self.material = material
        self.tyrazh = tyrazh
        self.weight = weight
        self.diameter = diameter
        self.gurt = gurt
        self.description = desription
        self.priceVf = priceVf
        self.priceXf = priceXf
        self.imageName = imageName
        self.nominallmageName = nominallmageName
        self.udid = udid
        self.isCheshuya = isCheshuya
        self.front = front
        self.back = back
        self.isProbnaya = isProbnaya
        self.isNovodel = isNovodel
        self.isValuable = isValuable
        self.additionallmages = additionallmages


class Ruler:
    def __init__(self, name, years, img, greyimg):
        self.name = name
        self.years = years
        self.img = img
        self.greyimg = greyimg


class Category:
    def __init__(self, name, prices, front, back):
        self.name = name
        self.prices = prices
        self.front = front
        self.back = back
        self.back = back
