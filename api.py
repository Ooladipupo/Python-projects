import requests

base_url = "https://pokeapi.co/api/v2/"

def get_poemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        print("Data retrived")
        pokemon_data = response.json()
        #print(pokemon_data["name"])
        return pokemon_data
        

    else:
        print(f"failed to retrive data{response.status_code}")

pokamon_name = "typhlosion"

pokemon_info = get_poemon_info(pokamon_name)

if pokemon_info:
   print(f"{pokemon_info["name"]}")
   print(f"{pokemon_info["id"]}")
   print(f"{pokemon_info["height"]}")
   print(f"{pokemon_info["order"]}")
   print(f"{pokemon_info["cries"]}")
   print(f"{pokemon_info["weight"]}")