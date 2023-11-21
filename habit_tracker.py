import requests
from datetime import datetime

# Pixela how to use step by step tutorial: https://pixe.la/
# Pixela API doc: https://docs.pixe.la/

# STEP 1: CREATING THE USER ACCOUNT
# https://docs.pixe.la/entry/post-user
PIXELA_USER_PAGE = "https://pixe.la/@joaoluizpyhon"  # Got this after creating the user.
PIXELA_USERNAME = "joaoluizpyhon"
PIXELA_TOKEN = "jondee123"

pixela_user_endpoint = "https://pixe.la/v1/users"

pixela_user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_user_endpoint, json=pixela_user_params)
# print(response.text)  # With the .text, it actually prints a more descriptive error or success message.

# STEP 2: CREATE A GRAPH DEFINITION
# https://docs.pixe.la/entry/post-graph
pixela_graph_endpoint = f"{pixela_user_endpoint}/{PIXELA_USERNAME}/graphs"

pixela_graph_params = {
    "id": "graphbookread1",
    "name": "Book Reading Habit",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
    "timezone": "America/Sao_Paulo",
}

# Here we use headers to authenticate in a more secure way
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# response = requests.post(pixela_graph_endpoint, json=pixela_graph_params, headers=headers)
# print(response.text)

# STEP 3: GET THE GRAPH
# https://docs.pixe.la/entry/get-graph

# Open in the browser to actually see your graph:
# https://pixe.la/v1/users/joaoluizpyhon/graphs/graphbookread1.html

# STEP 4: POST VALUE TO THE GRAPH
today = datetime.now()
formatted_date_today = today.strftime("%Y%m%d")
print(formatted_date_today)

post_value_params = {
    "date": formatted_date_today,
    "quantity": "5"
}

pixela_graphbookread1 = f"{pixela_user_endpoint}/{PIXELA_USERNAME}/graphs/graphbookread1"
# post_value = requests.post(pixela_graphbookread1, json=post_value_params, headers=headers)
# print(post_value.text)

# UPDATE/CHANGE GRAPH (NOT THE SAME AS UPDATING A PIXEL/VALUE IN THE GRAPH)
update_graph_params = {
    "color": "shibafu"
}
# update_graph = requests.put(pixela_graphbookread1, json=update_graph_params, headers=headers)
# print(update_graph.text)

# UPDATE A PIXEL
update_pixel_params = {
    "quantity": "5"
}
# update_pixel = requests.put(f"{pixela_graphbookread1}/{formatted_date_today}", json=update_pixel_params, headers=headers)
# print(update_pixel.text)

# DELETE A PIXEL
# delete_pixel = requests.delete(f"{pixela_graphbookread1}/{formatted_date_today}", headers=headers)
# print(delete_pixel.text)

# CREATING A PIXEL BASED ON USER INPUT
post_value_input_params = {
    "date": formatted_date_today,
    "quantity": input("How many minutes did you spend reading today (just type the numbers)? "),
}
post_value_input = requests.post(pixela_graphbookread1, json=post_value_input_params, headers=headers)
print(post_value_input.text)
