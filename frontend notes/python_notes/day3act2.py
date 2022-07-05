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

# Country = {
#     'UK' : 'London',
#     'France' : 'Paris',
#     'Germany' : 'Berlin',
#     'Spain' : 'Madrid',
#     'Italy': 'Rome'
# }
# Country.setdefault('Poland','Warsaw')
# Country.setdefault('Turkey','Ankara')
# print(Country)
#running above code lists all countries and capitals with the two additional ones

#another version
# dict = {'Country': 'UK', 'Capital': 'London', 'Language': 'English'}
# print ("dict['Country']: ", dict['Country'])
# print ("dict['Capital']: ", dict['Capital'])
# print ("dict['Language']:", dict['Language'])
countries = {
    "UK":"London",
    "France":"Paris",
    "Germany":"Berlin",
    "Spain":"Madrid",
    "Italy":"Rome",
}
countries.setdefault("Poland","Warsaw")
countries.setdefault("Turkey","Ankara")

for i in countries.items():
    print(i)

countries.update({
    "UK":"English",
    "France":"French",
    "Germany":"German",
    "Spain":"Spanish",
    "Italy":"Italian",
    "Poland":"Polish",
    "Turkey":"Turkish"})
for i in countries.items():
    print(i)
    