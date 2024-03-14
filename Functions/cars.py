def make_car(manufacturer, model_name, **others):
    profile = {'Manufacturer': manufacturer, 'Model_name': model_name}
    for key, value in others.items():
        profile[key] = value
    return profile


car1 = make_car('subaru', 'outback',
                color='blue', tow_package=True)
car2 = make_car('Toyota', 'Corolla',
                version='xe', color='red', Mod=True)
print(car1, '\n', car2)
