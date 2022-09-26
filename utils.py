import json

def get_posts_all():
    with open('data/posts.json', 'r', encoding="utf-8") as post_source:
        posts_list = json.load(post_source)
        for one_post in posts_list:
            return one_post
            
def get_posts_by_user(user_name):
    with open('data/posts.json', 'r', encoding="utf-8") as post_source:
        posts_list = json.load(post_source)
        posts_by_username = []
        for _ in posts_list:
            if user_name in _.values():
                    posts_by_username.append(_)
        return posts_by_username


print(get_posts_by_user('leo'))