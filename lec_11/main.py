import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def filter_titles(data):
    return [item for item in data if len(item['title'].split()) <= 6]

def filter_bodies(data):
    return [item for item in data if item['body'].count('\n') <= 3]

def get_filtered_posts():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        data = response.json()
        filtered_by_title = filter_titles(data)
        filtered_by_body = filter_bodies(filtered_by_title)
        print("Filtered Posts:")
        for post in filtered_by_body:
            print(post)
    else:
        print(f"GET /posts failed with status code {response.status_code}")

def create_post():
    new_post = {
        "title": "Sample Post",
        "body": "This is a new post created via POST request.",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    if response.status_code == 201:
        print("Post Created Successfully:", response.json())
    else:
        print(f"POST /posts failed with status code {response.status_code}")

def update_post(post_id):
    updated_post = {
        "id": post_id,
        "title": "Updated Title",
        "body": "This is the updated body of the post.",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_post)
    if response.status_code == 200:
        print("Post Updated Successfully:", response.json())
    else:
        print(f"PUT /posts/{post_id} failed with status code {response.status_code}")

def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print(f"Post with ID {post_id} deleted successfully.")
    else:
        print(f"DELETE /posts/{post_id} failed with status code {response.status_code}")

def main():
    print("Making GET call to fetch and filter posts...")
    get_filtered_posts()
    
    print("\nMaking POST call to create a new post...")
    create_post()
    
    print("\nMaking PUT call to update a post...")
    update_post(post_id=1)
    
    print("\nMaking DELETE call to delete a post...")
    delete_post
    
if __name__ == "__main__":
    main()
