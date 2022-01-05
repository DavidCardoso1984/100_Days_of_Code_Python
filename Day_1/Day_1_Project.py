# 1. Create a name gereting for band;

# 2. Ask the user for the city that they grew up in;

# 3. Ask the user for the name of a pet;

# 4. Combine the name of their city and pet and show their band name;

# 5. Make sure the input  cursor shows on a new line.

print("Welcome to the Band Name Generator.")
city_name = input("What's name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
city_name = str(city_name)
pet_name = str(pet_name)
print("Your band name could be " + city_name + " " + pet_name + ".")