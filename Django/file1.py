import requests

url = "http://ya.ru"

resp = requests.get(url=url)
print(resp.url)
if __name__ == "__main__":
    pass
