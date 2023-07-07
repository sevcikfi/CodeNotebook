import requests
import random
import time
from faker import Faker
from bs4 import BeautifulSoup
import webbrowser
url= "some url" # input ("Video or Article")
num_views = 100
min_sleep = 0.5
max_sleep = 0
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
]


fake = Faker()
for i in range(num_views):
    headers = {
        "User-Agent": random.choice(user_agents),
        "X-Forwarded-For": fake.ipv4(),
    }
    response = requests.get(url, headers=headers, cookies={"viewed": "true"})
    soup = BeautifulSoup(response.content, "html.parser")
    time.sleep(random.uniform(min_sleep, max_sleep))
    print(f"View {i + 1}: Status code {response.status_code} - {soup.title.string}")