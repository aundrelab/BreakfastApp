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
        ["Pancakes"," data:image/jpeg;base64,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","https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/"]
        ["Waffles","https://thesaltymarshmallow.com/wp-content/uploads/2018/08/belgian-waffles1.jpg","https://thesaltymarshmallow.com/homemade-belgian-waffle-recipe/"]
        ["French Toast","https://food.fnr.sndimg.com/content/dam/images/food/fullset/2008/3/26/0/IE0309_French-Toast.jpg.rend.hgtvcom.826.620.suffix/1431730431340.jpeg","https://www.foodnetwork.com/recipes/robert-irvine/french-toast-recipe-1951408"]
        ["Crepes","https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-basic-crepes-horizontal-1545245797.jpg?crop=0.6668xw:1xh;center,top&resize=980:*","https://www.delish.com/cooking/recipe-ideas/recipes/a52114/easy-basic-crepe-recipe/"]
        ["Cereal","https://images.media-allrecipes.com/userphotos/250x250/338461.jpg","https://www.allrecipes.com/recipe/44162/homemade-cereal/"]
        ["Breaksfast Burrito","https://images-gmi-pmc.edge-generalmills.com/b313435a-e9b8-49de-8088-ba7082c4d2dd.jpg","https://www.pillsbury.com/recipes/easy-breakfast-burritos/2fd0666e-79c3-40e8-a375-7be8e6db7360"]
        ["Acai Breaksfast Bowl","https://theforkedspoon.com/wp-content/uploads/2016/07/acai-bowl-5.jpg.webp","https://theforkedspoon.com/acai-bowl/"]
        ["Huevos Rancheros","https://i2.wp.com/aspicyperspective.com/wp-content/uploads/2017/10/the-best-huevos-ranchero-recipe-16.jpg","https://i2.wp.com/aspicyperspective.com/wp-content/uploads/2017/10/the-best-huevos-ranchero-recipe-16.jpg"]
        ["Oat Meal","https://fitfoodiefinds.com/wp-content/uploads/2015/10/50-best-oatmeal-recipes.png","https://fitfoodiefinds.com/the-50-best-oatmeal-recipes-on-the-planet/"]
        ["Omelet","https://x9wsr1khhgk5pxnq1f1r8kye-wpengine.netdna-ssl.com/wp-content/uploads/basic-french-omelet-930x550.jpg","https://www.incredibleegg.org/recipe/basic-french-omelet/"]
        ["Country-Fried Steak","https://www.momontimeout.com/wp-content/uploads/2018/08/best-chicken-fried-steak-recipe.jpg","https://www.momontimeout.com/chicken-fried-steak-recipe-with-gravy/"]
        ["Quesadillas","https://www.cookingclassy.com/wp-content/uploads/2019/02/quesadillas-2.jpg","https://www.cookingclassy.com/quesadillas/"]
        ["Breakfast Sandwhich","https://pinchofyum.com/wp-content/uploads/Breakfast-Sandwich-1.jpg","https://pinchofyum.com/breakfast-sandwich"]
        ]
    return main_dish[0]
    # return random.choice(main_dish)
    
def get_side_dish():
    side_dish = [
        ["Toast","https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fcdn-image.foodandwine.com%2Fsites%2Fdefault%2Ffiles%2Fstyles%2F4_3_horizontal_inbody_900x506%2Fpublic%2F1459261213%2Fmarinated-piquillo-peppers-and-whipped-eggplant-toasts-XL-RECIPE0516.jpg%3Fitok%3DsoRIcO6w&w=200&c=sc&poi=face&q=85","https://www.foodandwine.com/slideshows/toast-recipes"]
        ["Avocado Toast","https://cookieandkate.com/images/2012/04/avocado-toast-recipe-3.jpg","https://cookieandkate.com/avocado-toast-recipe/"]
        ["Yogurt","https://i5.walmartimages.com/asr/6561f7ae-2d16-4782-b60d-4c2dfbeaf6b2_1.fba6264b145f97b1c1359f2ca0f04da9.jpeg?odnWidth=200&odnHeight=200&odnBg=ffffff","https://www.walmart.com/browse/food/yogurt-yogurt-drinks/976759_1071964_976788_1001470"]
        ["Granola","",""]
        ["Scones","",""]
        ["Mixed Fruit","",""]
        ["Sausage","",""]
        ["Hash Browns","",""]
        ["Bacon","",""]
        ["Country Potatoes","",""]
        ["Italian Sausage","",""]
        
        
        ]
    return (random.choice(side_dish))
    
def get_drinks():
    drinks = [
        ["Milk","",""]
        ["Coffee","",""]
        ["Orange Juice","",""]
        ["Apple Juice","",""]
        ["Smoothie","",""]
        ["Water","",""]
        ["Mango Juice","",""]
        ["Cranberry Juice","",""]
        ["Hot Chocolate","",""]
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
            "side_name": main[3]
        }
        
        welcome_template = the_jinja_env.get_template('templates/meals.html')
        self.response.write(welcome_template.render(the_variable_dict))
        
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