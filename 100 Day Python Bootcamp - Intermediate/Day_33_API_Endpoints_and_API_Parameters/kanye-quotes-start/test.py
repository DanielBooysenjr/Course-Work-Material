import requests

quote = requests.get(url="https://api.kanye.rest")
quote.raise_for_status()
kanye_quote = quote.json()
kanye_quote = kanye_quote["quote"]

print(kanye_quote)