favorite_place= {
    'zls': ["xiamen",'chengdu',],
    'czy': ["xiamen",'shenzhen','chengdu'],
    'cecilia': ['tianjin','sydney','jining'],
    }

for name, places in favorite_place.items():
    if len(places)==1:
        print(f"{name}'s favorite place is {places}")
    elif len(places)>1:
        print(f"{name}'s favorite place are:")
        for place in places:
            print(f"\t{places}")
    

    
