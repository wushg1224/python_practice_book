def describe_city(name, country='china'):
    """"show city name and country"""
    print(f"\n{name.title()} is in {country.title()}")

describe_city('reykjavik' , "iceland")
describe_city('shanghai')
describe_city('guangzhou')
describe_city('tianjin')