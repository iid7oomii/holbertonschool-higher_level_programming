import csv
import requests

def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.

    This function sends a GET request to the posts endpoint. If the request
    is successful (status code 200), it extracts the 'id', 'title', and
    'body' fields from each post and writes them into a CSV file named
    'posts.csv' using the csv.DictWriter class.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        posts_list = []
        
        for post in posts:
            posts_list.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(posts_list)
