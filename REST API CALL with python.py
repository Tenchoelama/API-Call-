import requests 


response = requests.get("https://fakestoreapi.com/products")

print(response.json())

#Retrieve all products:
response = requests.get("https://fakestoreapi.com/products")

#Retrieve a single product by ID:
#Replace {id} with the ID of the product you want to retrieve.
response = requests.get("https://fakestoreapi.com/products/{id}")


# Retrieve all product categories:
response = requests.get("https://fakestoreapi.com/products/categories")

# Retrieve all products in a specific category:
# Replace {categoryName} with the name of the category you want to retrieve.
response = requests.get("https://fakestoreapi.com/products/category/{categoryName}")



# Retrieve all available product reviews:
# Replace {id} with the ID of the product you want to retrieve reviews for.
resoponse = requests.get("https://fakestoreapi.com/products/{id}/reviews")



# Retrieve a single user by ID:
# Replace {id} with the ID of the user you want to retrieve.
response = requests.get("https://fakestoreapi.com/users/{id}")


