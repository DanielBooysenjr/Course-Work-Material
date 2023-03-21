import requests

class Post:
    def blog_posts(self):
        blog_url = ("https://api.npoint.io/3ddca80c1d4a3d82012d")
        response = requests.get(blog_url)
        blogs = response.json()
        return blogs

# test = Post
# test.blog_posts()