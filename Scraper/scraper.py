import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        print(f"✅ Page Title: {title}")
    else:
        print(f"❌ Failed to fetch page. Status code: {response.status_code}")

if __name__ == "__main__":
    get_page_title("https://www.example.com")
