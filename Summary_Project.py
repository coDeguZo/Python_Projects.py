# Using all the skills I learned to make a project

#Variable  #String
boy_name = "Bryan"
building_type = "house"
shoe_name = "nikes"
sound_type = "shout"
pokemon_name = input("Enter Chibu's favorite pokemon : ")
person_name = input("Enter Bryan's favorite pokemon: ")
Bryan_chance = input("Enter Bryans chances of winning Pokemon Whole Number: ")
Bryan_chance2 = input("Enter Bryan's chances of winning Decimal: ")
results_Bryan = int(Bryan_chance) + float(Bryan_chance2) #Float/Int Attribute #Prints into Number so must string it.
Chibu_chance = input("Enter Chibus belief low Whole Numbe: ")
Chibu_chance2 = input("Enter Chibus belief high Decimal: ")
results_Chibu = int(Chibu_chance) + float(Chibu_chance2)
list_pokemon = ["Gangar", "Kyogre", "Lugia", "Ho-Oh"]

# Concatenation is apending another string onto another String.
print("There once was a man named " + boy_name + ",")
print("He lived in a " + building_type + " on a hill.")
print("He had a blue pair of " + shoe_name + " to run in,")
print("And he loved to " + sound_type + " all types of sounds.")
print(boy_name + " loved to play tag in his park.")
print(boy_name + " would have to be careful not to get his " + shoe_name + " dirty in the mud.")
print("A " + sound_type + " came from " + boy_name + "'s " + building_type + " late in the afternoon.")
print(boy_name + "'s mom was calling him to come in the " + building_type + " for dinner.")

boy_name = "Chibu"
friend_name = "Bryan"
building_type = "Dump"
boy_age = 23.5 #Number
is_upper = True #Boolean
video_game = "Pokemon"
print("Across the street lived a boy named, " + boy_name + ".")
print(boy_name + " loved to play in the " + building_type + " with his close friend " + friend_name + ".")
print(boy_name + ", is currently " + str(boy_age) + " years old and his friend " + friend_name + " is 24 years old.")
print(boy_name.upper() + " is a strong male and decides to challenge his friend " + friend_name + " to a new challenge.")
print(boy_name + " has been playing a new game called " + video_game + ", which he thinks Bryan will like.")
print(boy_name + " believes his favorite pokemon, " + pokemon_name + ", will be able to beat Bryan's favorite pokemon, " + person_name + ".")
print(friend_name + " believes his pokemon has a " + str(results_Bryan) + "% chance of winning the battle.")
print(boy_name + " did not believe those chances and believed that " + friend_name + "'s actual percent of beating him was " + str(results_Chibu) + "%.")
print(boy_name + " had a whole list of pokemon, such as " + str(list_pokemon) + ".")
print(friend_name + " was offended by " + boy_name + "'s estimate of him winning. ")
print(friend_name + " insisted that only " + str(list_pokemon[2]) + " was the only pokemon that could beat him and even " + friend_name + "'s younger brother, " + friend_name.replace("Bryan", "Bryce") + ", could beat " + boy_name + ".")
print(boy_name.upper().isupper()) 






