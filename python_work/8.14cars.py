def car_profile(manufacture, car_model, **kwargs):
    """"describe a car"""
    kwargs['manufacture'] = manufacture
    kwargs['car_model '] = car_model
    return kwargs

car_info = car_profile('subaru', 'outback',
                       color = 'blue',
                       tow_package= True)
print(car_info )