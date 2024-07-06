import requests

def get_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data for {state}")
        return []

def main():
    states = ["Alaska", "Maine", "New York"]
    breweries_count = {}

    for state in states:
        breweries = get_breweries_by_state(state)
        breweries_count[state] = len(breweries)

    for state, count in breweries_count.items():
        print(f"Number of breweries in {state}: {count}")

if __name__ == "__main__":
    main()
