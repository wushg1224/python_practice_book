travel=["shanghai",'paris','maldivs','london',"amstrong",'chroasia']
print(sorted(travel))
print(sorted(travel, reverse=True))
print(travel)
travel.reverse()
print(travel)
travel.sort()
print(travel)
travel.sort(reverse=True)
print(travel)

print("The first three items in the list are:")
print(travel[0:3])

print('Three items from the middle of the list are:')
print(travel[1:4])

print("The last three items in the list are:")
print(travel[-3:])