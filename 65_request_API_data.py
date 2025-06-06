# https://pokeapi.co/

import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):  # name je parametr funkce
    url = f"{base_url}/pokemon/{name}"  # vytvoříme url adresu
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_name = "blastoise"  # pokemon_name je argument
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
    print(f"Abilities: {[ability['ability']['name'] for ability in pokemon_info['abilities']]}")
