rivers= {
    'nile': "egypt",
    'amazon': "brazil",
    'changjiang': "china",
    'ganges': "india",
    'thames': "british"
    }
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}. ")

print("The following rivers have been mentioned:")
for river in rivers.keys():
    print(f"\t\t{river.title()}")
print("The following country have been mentioned:")
for country in rivers.values():
    print(f"\t{country.title()}")