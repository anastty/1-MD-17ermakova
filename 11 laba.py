def task_1():
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

new_restaurant = Restaurant("The Blue Marlin", "Seafood")

print("Название ресторана:", new_restaurant.restaurant_name)
print("Тип кухни:", new_restaurant.cuisine_type)

new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

def task_2():
class Restaurant:
  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name.title()
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

restaurant1 = Restaurant('the white flag', 'miu')
restaurant2 = Restaurant('cherry', 'cake')
restaurant3 = Restaurant('aurora', 'raskolnikov')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

def task_2():
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
      self.restaurant_name = restaurant_name.title()
      self.cuisine_type = cuisine_type
      self.rating = 0

    def describe_restaurant(self):


        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine and has a rating of {self.rating}.")


    def set_rating(self, new_rating):
      self.rating = new_rating

class
    restaurant = Restaurant('aurora', 'cherry')

print(f"Initial rating: {restaurant.rating}")

restaurant.set_rating(4.5)

print(f"Updated rating: {restaurant.rating}")
