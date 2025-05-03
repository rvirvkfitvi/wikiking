import requests
import os

# Function to fetch data from Wikipedia API
def fetch_wikipedia_content(topic):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for topic: {topic}")
        return None

# Function to create HTML file for a topic
def create_html_page(topic, content):
    sanitized_topic = topic.replace(" ", "_")
    file_name = f"{sanitized_topic}.html"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{content['title']}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>{content['title']}</h1>
        <nav>
            <a href="index.html">Home</a>
        </nav>
    </header>
    <main>
        <p>{content.get('extract', 'No summary available.')}</p>
        <a href="{content.get('content_urls', {}).get('desktop', {}).get('page', '#')}" target="_blank">Read more on Wikipedia</a>
    </main>
    <footer>
        <p>&copy; 2025 Wikking. All rights reserved.</p>
    </footer>
</body>
</html>
        """)
    print(f"Generated page: {file_name}")

# Topics to fetch data for
topics = ["Science", "History", "Geography", "Technology", "Mathematics", "Art"]

# Create HTML pages for each topic
if not os.path.exists("generated_pages"):
    os.makedirs("generated_pages")
os.chdir("generated_pages")

for topic in topics:
    content = fetch_wikipedia_content(topic)
    if content:
        create_html_page(topic, content)

print("All pages generated successfully!")