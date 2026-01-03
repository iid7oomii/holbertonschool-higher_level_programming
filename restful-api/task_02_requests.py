import requests
import csv

def fetch_and_print_posts():
    """
    Fetches and prints the titles of all posts from JSONPlaceholder.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        
        # تحضير البيانات بصيغة قائمة قواميس
        filtered_data = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']} 
            for p in posts
        ]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_data)
