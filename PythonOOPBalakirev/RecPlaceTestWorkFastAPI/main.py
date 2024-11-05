import requests

URL = "https://kinopoiskapiunofficial.tech/"

if __name__ == "__main__":
    r = requests.get(URL)
    print(r.text)
