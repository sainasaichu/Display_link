import requests


class CountryDataFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()  # Parse the JSON data
            return data
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None

    def display_countries_with_euro_currency(self):
        data = self.fetch_data()
        if data:
            euro_countries = []
            for country in data:
                name = country.get('name', {}).get('common', 'Unknown')
                currencies = country.get('currencies', {})
                for currency_code, currency_info in currencies.items():
                    currency_name = currency_info.get('name', '').lower()
                    if 'euro' in currency_name:
                        euro_countries.append(name)
                        break
            if euro_countries:
                print("Countries using Euro as currency:")
                for country in euro_countries:
                    print(country)
            else:
                print("No countries found with Euro as currency")
        else:
            print("Failed to fetch country data")


# Example usage
url = "https://restcountries.com/v3.1/all"
fetcher = CountryDataFetcher(url)
fetcher.display_countries_with_euro_currency()
