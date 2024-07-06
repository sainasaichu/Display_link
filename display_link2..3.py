import requests
from collections import defaultdict


def get_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data for {state}")
        return []


def count_brewery_types(breweries):
    city_brewery_types = defaultdict(lambda: defaultdict(int))
    for brewery in breweries:
        city = brewery['city']
        brewery_type = brewery['brewery_type']
        city_brewery_types[city][brewery_type] += 1
    return city_brewery_types


def main():
    states = ["Alaska", "Maine", "New York"]

    for state in states:
        breweries = get_breweries_by_state(state)
        city_brewery_types = count_brewery_types(breweries)

        print(f"Brewery types in cities of {state}:")
        for city, types in city_brewery_types.items():
            print(f"  {city}:")
            for brewery_type, count in types.items():
                print(f"    {brewery_type}: {count}")
        print()


if __name__ == "__main__":
    main()
