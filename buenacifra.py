from random_username.generate import generate_username

def print_username():
    username = generate_username()[0]
    print(f"Username: {username}")