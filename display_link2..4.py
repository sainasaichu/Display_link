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

    for state in states:
        breweries = get_breweries_by_state(state)
        breweries_with_websites = [brewery for brewery in breweries if brewery.get('website_url')]

        print(f"Number of breweries with websites in {state}: {len(breweries_with_websites)}")
        for brewery in breweries_with_websites:
            print(f" - {brewery['name']}: {brewery['website_url']}")
        print()


if __name__ == "__main__":
    main()
