import requests
from urllib.parse import quote

def wikipedia_summary(topic):

    encoded_topic = quote(topic.replace(" ", "_"))

    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded_topic}"

    headers = {
        "User-Agent": "AI-Hackathon-Student-Project/1.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"Information not found. Status code: {response.status_code}"

    data = response.json()

    return data.get("extract", "No summary available.")


print(wikipedia_summary("Artificial intelligence"))