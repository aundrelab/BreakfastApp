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

# def breakfast_meal():
#     breakfast_dict = [
#         "main_dish":{
#             "Pancakes":["link", "image url"],
#             "Waffles":["link", "image url"]
#         },
        
#         "side_dish":{
#             "Yogurt":["link", "image url"],
#             "Fruit Bowl":["link", "image url"]
#         },
        
#         "drinks":{
#             "Apple Juice":["link", "image url"],
#             "Orange Juice":["link", "image url"]
#         }
#     ]
#     return random.choice(breakfast_dict)

def get_main_dish():
    main_dish = [
        ["Eggs Benedict","https://www.simplyrecipes.com/wp-content/uploads/2010/04/eggs-benedict-vertical-a-1600.jpg", "https://www.simplyrecipes.com/recipes/eggs_benedict/"],
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
    return main_dish[0]
    # return random.choice(main_dish)
    
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
        main = get_main_dish()
        the_variable_dict = {
            "name": main[0],
            "image": main[1],
            "recipe": main[2]
        }
    
    #     main_dish = get_main_dish()
    #     print(main_dish)
        
    #     side_dish = get_side_dish()
    #     print(side_dish)
        
    #     drinks = get_drinks()
    #     print(drinks)
        
    #     my_dictionary = {
    #         'main': main_dish,
    #         "sides": side_dish,
    #         "drink": drinks
            
    #     }
        
        end_template = the_jinja_env.get_template("templates/welcome.html")
        self.response.write(end_template.render(the_variable_dict))


        
class MealsHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        main = get_main_dish()
        the_variable_dict = {
            "main_name": main[0],
            "image": main[1],
            "recipe": main[2],
            "side_name"
        }
        
        welcome_template = the_jinja_env.get_template('templates/.html')
        self.response.write(welcome_template.render(my_dictionary))
        
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