class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Restaurant Name: ', self.restaurant_name)
        print('Cuisine Type: ', self.cuisine_type + ' Dish')

    def open_restaurant(self):
        print(self.restaurant_name + ' is open Today')

    def increment_number_served(self, no_customer):
        self.number_served += no_customer
        print(self.restaurant_name + " has served "
              + str(self.number_served) + " people today.")


class IceCreamStand(Restaurant):
    def __init__(self, flavours, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def flavour(self):
        """Display the flavours"""
        Restaurant.describe_restaurant(self)
        print(f'Flavours available at {self.restaurant_name} are;')
        for i in self.flavours:
            print('--', i)


data1 = Restaurant('Kilimanjaro', 'African')
data2 = Restaurant('Genesis', 'Chinese')

data1.describe_restaurant()
print('-' * 30)
data1.open_restaurant()
data1.increment_number_served(28)
data1.increment_number_served(20)

print('')
print('')
data2.describe_restaurant()
print('-' * 30)
data2.open_restaurant()
data2.increment_number_served(23)

print('')
print('')

items = ['chocolate', 'vanilla', 'pepper-ish', 'salty', 'vintage']
ice = IceCreamStand(items, 'Genesis', 'Desert')
ice.flavour()
