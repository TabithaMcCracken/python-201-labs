'''
Done
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests
import json

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

# Get user data
def get_users():
    user_request = requests.get(base_url)
    data = user_request.text
    parsed_json = json.loads(data)
    return parsed_json

# Create a user
def create_new_user():
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    email = input("What is your email address: ")

    body = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }

    response = requests.post(base_url, json=body)
    if response.status_code == 201:
        print("Your new user info was saved.")
        response = requests.get(base_url)
        data = response.json()
        last_added_data = data["data"][-1]["id"]
        print(f"Your use id is: {last_added_data}")
    else:
        print("Oops, something went wrong!")

# Update email address
def update_email():
    user_id = int(input("What is your user id?"))
    new_email = input("What is your new email address?")
    user_data = get_users()
    user_filter_data = user_data["data"]
    first_name = []
    last_name = []

    for data in user_filter_data:
        user_access = data["id"]
        if user_access == user_id:
            first_name = data["first_name"]
            print(f"Your first name is: {first_name}")
            last_name = data["last_name"]
            print(f"Your last name is: {last_name}")

    body = {
        "id": user_id,
        "email": new_email,
        "first_name": first_name,
        "last_name": last_name
    }

    response = requests.put(base_url, json= body)
    if response.status_code == 201 or response.status_code == 200:
        print("Your new email has been saved.")
    else:
        print("Looks like something went wrong.")
        print(response.status_code)


print("Pleae select from the following options: \n")
task = int(input("1) Create a new user \n2) Update my email \n3) Do nothing\n"))
if task == 1:
    create_new_user()
elif task == 2:
    update_email()
else:
    print("We're sorry that you have chosen to do nothing, have a nice day!")



