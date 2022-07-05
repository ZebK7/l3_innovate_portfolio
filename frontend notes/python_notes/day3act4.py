fav_music = [
    "The Doors - Morrison Hotel",
    "Aerosmith - Permanent Vacation",
    "Matallica - Metallica",
]

list_songs = [
    {"artist":"The Doors",
    "song_name":"Peace Frog",
    "genre":"Rock",
    "release_year":"1970"},
    {"artist":"Aerosmith",
    "song_name":"Rag Doll",
    "genre":"Rock",
    "release_year":"1987"},
    {"artist":"Metallica",
    "song_name":"Enter Sandman",
    "genre":"Heavy Metal",
    "release_year":"1991"},
]

# each dictionary is defined by index position in the list

for i in list_songs:
    print(i)
    print("\n")

for i in list_songs[0].items():
    print(i)

print("\n")
# used to print individual dictionary using index postion

list_songs[0].update({"artist":"Jim Morrison"})
# updated [0], artist value
for i in list_songs[0].items():
    print(i)

print("\n")

# append method to add another dictionary to the end of the list
list_songs.append(
    {"artist":"Stone Roses",
    "song_name":"I Wanna Be Adored",
    "genre":"Rock",
    "release_year":"1989"}
)


for i in list_songs:
    print(i, "\n")
# used del function to remove index [1] from the list
del(list_songs[1])
for i in list_songs:
    print(i)
    print("\n")
