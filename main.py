import webapp2
import jinja2
import os
from models import Breakfast
from google.appengine.api import users
import random


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



def get_main_dish():
    main_dish = [
        "Eggs Benedict",
        "Pancakes",
        "Waffles",
        "French Toast",
        "Crepes",
        "Cereal",
        "Breaksfast Burrito",
        "Acai Breaksfast Bowl",
        "Huevos Rancheros",
        "Oat Meal",
        "Omelet",
        "Country-Fried Steak",
        "Quesadillas",
        "Breakfast Sandwhich"
        ]
    return (random.choice(main_dish))
    
def get_side_dish():
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
        "Italian Sausage"
        
        
        ]
    return (random.choice(side_dish))
    
def get_drinks():
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
    return (random.choice(drinks))
    
class HomeHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
    
        main_dish = get_main_dish()
        print(main_dish)
        
        side_dish = get_side_dish()
        drinks = get_drinks()
        
        my_dictionary = {
            'main': main_dish,
            "sides": side_dish,
            "drink": drinks
            
        }
        
        end_template=the_jinja_env.get_template("templates/results.html")
        self.response.write(end_template.render(my_dictionary))


        
class MealsHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/meals.html')
        self.response.write(welcome_template.render())
        
class HistoryHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/history.html')
        self.response.write(welcome_template.render())
    
    
app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/meals', MealsHandler),
    ('/history', HistoryHandler)
    #('/allmemes', AllMemesHandler)
    
], debug=True)