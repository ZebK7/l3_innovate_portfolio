#activity 2 dictionary
# Countries = {
#     'UK' : 'London',
#     'France' : 'Paris',
#     'Germany' : 'Berlin',
#     'Spain' : 'Madrid',
#     'Italy': 'Rome'
# }

# Creating dictionary
# capitals = { 
#     "UK" : "London",
#     "France" : "Paris",
#     "Germany" : "Berlin",
#     "Spain" : "Madrid",
#     'Italy' : 'Rome'
#     }
# print("Original Dictionary : ")
# print(capitals)
# # adding item in dictionary
# capitals['Ireland'] = 'Dublin'
# capitals['Norway'] = 'Oslo'
# # printing dictionary after adding item
# print()
# print("After adding item in dictionary :")
# print("Updated Dictionary:")
# print(capitals)

Country = {
    'UK' : 'London',
    'France' : 'Paris',
    'Germany' : 'Berlin',
    'Spain' : 'Madrid',
    'Italy': 'Rome'
}
Country.setdefault('Poland','Warsaw')
Country.setdefault('Turkey','Ankara')
print(Country)
#running above code lists all countries and capitals with the two additional ones
