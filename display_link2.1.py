import requests

def get_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    if response.status_code == 200:
        return [brewery['name'] for brewery in response.json()]
    else:
        print(f"Failed to get data for {state}")
        return []

def main():
    states = ["Alaska", "Maine", "New York"]
    breweries = {state: get_breweries_by_state(state) for state in states}

    for state, brewery_list in breweries.items():
        print(f"Breweries in {state}:")
        for brewery in brewery_list:
            print(f" - {brewery}")

if __name__ == "__main__":
    main()
