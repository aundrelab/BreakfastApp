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
        ["Pancakes","https://static01.nyt.com/images/2017/03/24/dining/24COOKING-CLASSICPANCAKES/24COOKING-CLASSICPANCAKES-articleLarge.jpg","https://cooking.nytimes.com/recipes/1893-everyday-pancakes"],
        ["Waffles","https://thesaltymarshmallow.com/wp-content/uploads/2018/08/belgian-waffles1.jpg","https://thesaltymarshmallow.com/homemade-belgian-waffle-recipe/"],
        ["French Toast","https://food.fnr.sndimg.com/content/dam/images/food/fullset/2008/3/26/0/IE0309_French-Toast.jpg.rend.hgtvcom.826.620.suffix/1431730431340.jpeg","https://www.foodnetwork.com/recipes/robert-irvine/french-toast-recipe-1951408"],
        ["Crepes","https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-basic-crepes-horizontal-1545245797.jpg?crop=0.6668xw:1xh;center,top&resize=980:*","https://www.delish.com/cooking/recipe-ideas/recipes/a52114/easy-basic-crepe-recipe/"],
        ["Cereal","https://images.media-allrecipes.com/userphotos/250x250/338461.jpg","https://www.allrecipes.com/recipe/44162/homemade-cereal/"],
        ["Breakfast Burrito","https://images-gmi-pmc.edge-generalmills.com/b313435a-e9b8-49de-8088-ba7082c4d2dd.jpg","https://www.pillsbury.com/recipes/easy-breakfast-burritos/2fd0666e-79c3-40e8-a375-7be8e6db7360"],
        ["Acai Breaksfast Bowl","https://theforkedspoon.com/wp-content/uploads/2016/07/acai-bowl-5.jpg.webp","https://theforkedspoon.com/acai-bowl/"],
        ["Huevos Rancheros","https://i2.wp.com/aspicyperspective.com/wp-content/uploads/2017/10/the-best-huevos-ranchero-recipe-16.jpg","https://www.aspicyperspective.com/best-huevos-rancheros-recipe/"],
        ["Oat Meal","https://fitfoodiefinds.com/wp-content/uploads/2015/10/50-best-oatmeal-recipes.png","https://fitfoodiefinds.com/the-50-best-oatmeal-recipes-on-the-planet/"],
        ["Omelet","https://x9wsr1khhgk5pxnq1f1r8kye-wpengine.netdna-ssl.com/wp-content/uploads/basic-french-omelet-930x550.jpg","https://www.incredibleegg.org/recipe/basic-french-omelet/"],
        ["Country-Fried Steak","https://www.momontimeout.com/wp-content/uploads/2018/08/best-chicken-fried-steak-recipe.jpg","https://www.momontimeout.com/chicken-fried-steak-recipe-with-gravy/"],
        ["Quesadillas","https://www.cookingclassy.com/wp-content/uploads/2019/02/quesadillas-2.jpg","https://www.cookingclassy.com/quesadillas/"],
        ["Breakfast Sandwhich","https://pinchofyum.com/wp-content/uploads/Breakfast-Sandwich-1.jpg","https://pinchofyum.com/breakfast-sandwich"]
        ]
    
    return random.choice(main_dish)
    
def get_side_dish():
    side_dish = [
        ["Toast","https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fcdn-image.foodandwine.com%2Fsites%2Fdefault%2Ffiles%2Fstyles%2F4_3_horizontal_inbody_900x506%2Fpublic%2F1459261213%2Fmarinated-piquillo-peppers-and-whipped-eggplant-toasts-XL-RECIPE0516.jpg%3Fitok%3DsoRIcO6w&w=200&c=sc&poi=face&q=85","https://www.foodandwine.com/slideshows/toast-recipes"],
        ["Avocado Toast","https://cookieandkate.com/images/2012/04/avocado-toast-recipe-3.jpg","https://cookieandkate.com/avocado-toast-recipe/"],
        ["Yogurt","https://i5.walmartimages.com/asr/6561f7ae-2d16-4782-b60d-4c2dfbeaf6b2_1.fba6264b145f97b1c1359f2ca0f04da9.jpeg?odnWidth=200&odnHeight=200&odnBg=ffffff","https://www.walmart.com/browse/food/yogurt-yogurt-drinks/976759_1071964_976788_1001470"],
        ["Granola","https://www.gimmesomeoven.com/wp-content/uploads/2018/01/The-Best-Healthy-Granola-Recipe-4.jpg","https://www.gimmesomeoven.com/best-healthy-granola/"],
        ["Scones","https://www.fifteenspatulas.com/wp-content/uploads/2015/08/English-Style-Scones-Fifteen-Spatulas-1-640x960.jpg","https://www.fifteenspatulas.com/english-style-scones/"],
        ["Mixed Fruit","https://www.tasteofhome.com/wp-content/uploads/2017/10/Chilled-Mixed-Fruit_exps41090_CW143039C09_16_6bC_RMS-696x696.jpg","https://www.tasteofhome.com/recipes/chilled-mixed-fruit/"],
        ["Sausage","https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Chorizo_%284776711673%29.jpg/464px-Chorizo_%284776711673%29.jpg","https://tysonscore3.azureedge.net/assets/media/jimmydeanv2/products/packages/fresh-sausage/roll-sausage/productdetailheroes_783x440_16x9_0007_regular-pork-sausage-roll.ashx?data-specid=d071cee9-f2e0-4e5c-a620-05fd7f5981be&mw=668"],
        ["Hash Browns","https://assets.bonappetit.com/photos/57acf1d2f1c801a1038bc928/16:9/w_2560,c_limit/ba-best-hash-browns.jpg","https://www.bonappetit.com/recipe/bas-best-hash-browns"]
        # ["Bacon","",""]
        # ["Country Potatoes","",""]
        # ["Italian Sausage","",""]
        
        
        ]
    return (random.choice(side_dish))
    
def get_drinks():
    drinks = [
        ["Milk","https://i5.walmartimages.com/asr/cbcc26fb-af25-4672-bfb8-cb156cf1dadf_2.b93305e90bf7f66b9ab5f36f25652660.jpeg?odnHeight=150&odnWidth=150&odnBg=ffffff","https://grocery.walmart.com/browse/Milk?aisle=1255027787061_1255027788656"],
        ["Coffee","https://www.tasteofhome.com/wp-content/uploads/2018/01/Honey-Coffee_EXPS_CISMZ19_37409_E01_08_-4b-9-696x696.jpg","https://www.tasteofhome.com/recipes/honey-coffee/"],
        ["Orange Juice","https://images.media-allrecipes.com/userphotos/560x315/4513616.jpg","https://www.allrecipes.com/recipe/89229/fresh-orange-juice/"],
        ["Apple Juice","https://images-gmi-pmc.edge-generalmills.com/1eb60545-cc16-4c22-a4fc-a184887e4e8d.jpg","https://www.tablespoon.com/recipes/homemade-apple-juice/bcf44468-1eed-479a-88d6-2bd4c3cfacd3"],
        ["Smoothie","https://food.fnr.sndimg.com/content/dam/images/food/fullset/2011/3/2/4/RX-FNM_040111-Insert-016_s4x3.jpg.rend.hgtvcom.616.462.suffix/1371597358014.jpeg","https://www.foodnetwork.com/recipes/articles/50-smoothies"],
        ["Mango Juice","https://www.mycolombianrecipes.com/wp-content/uploads/2009/04/Mango-Juice-Jugo-de-Mango.jpg","https://www.mycolombianrecipes.com/mango-juice-jugo-de-mango"],
        ["Cranberry Juice","https://images.ourpaleolife.com/wp-content/uploads/2013/12/CranberryJuice.png","https://www.ourpaleolife.com/homemade-cranberry-juice/"],
        ["Hot Chocolate","https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-hot-chocolate-155-1542061491.jpg?crop=1xw:1xh;center,top&resize=768:*","https://www.delish.com/cooking/recipe-ideas/recipes/a50303/best-hot-chocolate-recipe/"]
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
            "recipe": main[2]
            
        }
        
        side = get_side_dish()
        second_variable_dict = {
            "side_name": side[0],
            "image": side[1],
            "recipe": side[2]
        }
        
        drink = get_drinks()
        third_variable_dict = {
            "drink_name": drink[0],
            "image": drink[1],
            "recipe": drink[2]
        }
        
        welcome_template = the_jinja_env.get_template('templates/meals.html')
        self.response.write(welcome_template.render(the_variable_dict))
        self.response.write(welcome_template.render(second_variable_dict))
        self.response.write(welcome_template.render(third_variable_dict))
        
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