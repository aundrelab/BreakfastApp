from google.appengine.ext import ndb

# class main_dish(ndb.Model):
#     name = ndb.StringProperty()
#     recipe_url = ndb.StringProperty()

# class side_dish(ndb.Model):
#     name = ndb.StringProperty()
#     recipe_url = ndb.StringProperty()
    
# class drinks(ndb.Model):
#     name = ndb.StringProperty()
#     recipe_url = ndb.StringProperty()

class menu(ndb.Model):
    day = ndb.StringProperty()
    main_dish_name = ndb.StringProperty()
    main_dish_url = ndb.StringProperty()
    side_dish_name = ndb.StringProperty()
    side_dish_url = ndb.StringProperty()
    drink_name = ndb.StringProperty()
    drink_url = ndb.StringProperty()