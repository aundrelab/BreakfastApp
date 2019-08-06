from google.appengine.ext import ndb

class Breakfast(ndb.Model):
    main_dish = ndb.StringProperty()
    side_dish = ndb.StringProperty()
    drinks = ndb.StringProperty()
    