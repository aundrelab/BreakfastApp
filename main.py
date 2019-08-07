import webapp2
import jinja2
import os
from models import menu


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


main_dish = [
    "Eggs Benedict",
    "Pancakes",
    "Waffles",
    "French Toast",
    "Crepes",
    "Cereal",
    "Breaksfast Burrito",
    "Acai Breaksfast Bowl",
    ]
    
side_dish = [
    "Toast",
    "Avocado Toast",
    "Yogurt",
    "Granola",
    "Scones",
    "Mixed Fruit",
    "Sausage",
    "Hash Browns",
    "Bacon",
    "Country Potatoes",
    
    
    ]
    
drinks = [
    "Milk",
    "Coffee",
    "Orange Juice",
    "Apple Juice",
    "Smoothie",
    "Water",
    "Mango Juice",
    "Cranberry Juice",
    "Hot Chocolate",
    ]
