#https://pokeapi.co/

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name): #name je parametr funkce
    url = f"{base_url}/pokemon/{name}" #vytvoříme url adresu
    response = requests.get(url)
    print(response)

pokemon_name = "pikachu" #pokemon_name je argument
get_pokemon_info(pokemon_name)