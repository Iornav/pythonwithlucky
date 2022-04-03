from multiprocessing.dummy import Array
from urllib.parse import ParseResultBytes


class User():
    first_name = ''
    last_name = ''
    email_addresses = ''
    phone_number = ''
    alergies = ''
    food_diet =''

class Menu:
    name = ''
    description = ''
    serving_size = ''
    allergens = ''
class MealCategory:
    list = ["Breakfast", "Lunch", "Dinner"]
class Order:
    quantity = ''
    time_date = datetime.datetime
class review:
    satisfiedService = True
    rate_food = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    feedback = ''
    
