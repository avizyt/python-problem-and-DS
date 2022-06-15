# create a capital dict

# dict is mapping of key to its value
# key must be unique otherwise there will be collision

capitals = {
    "India": "New Delhi",
    "China": "Beijing",
    "United States": "Washington",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Russia": "Moscow",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "Brazil": "Brasilia",
    "Canada": "Ottawa",
    "Switzerland": "Bern",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels"
}

print(capitals)
print(capitals["India"])  # here India is the key

# create a list from the capitals dict
list_of_countries = list(capitals.keys())
print(f"Countries: {list_of_countries}")

# create list of values from the capitals dict
list_of_capitals = list(capitals.values())
print(f"Capitals: {list_of_capitals}")


# check if a key exists in the dict and then do operationon it.
for country in list_of_countries:
    if country in capitals:
        # print(f"country : {country} || Capital : {capitals[country]}")
        print(f"Capital of {country} is {capitals[country]}")



# append a new key or country  to the list_of_countries
list_of_countries.append("Nigeria")
print(f"Countries: {list_of_countries}")

# what happen if we dont check the key 
for country in list_of_countries:
    print(f"Capital of {country} is {capitals[country]}")

'''
KeyError: 'Nigeria'
'''
