from pymongo import MongoClient

# Create a MongoClient instance
client = MongoClient('mongodb://user:secret@localhost:27017/')

# Access a database
db = client['recipebook']

# Access a collection
collection = db['recipes']

# Insert multiple recipes
recipes = [
    {
        "id": 1, 
        "title": "Spaghetti Bolognese",
        "ingredients": "['pasta', 'tomato', 'bolognese sauce']",
        "method": "['cook pasta', 'add sauce', 'serve']", 
    },
    {
        "id": 2,
        "title": "Fried Rice",
        "ingredients": "['rice', 'vegetables', 'chicken']", 
        "method": "['cook rice', 'add vegetables', 'serve']", 
    },
    {
        "id": 3, 
        "title": "Butter Chicken", 
        "description": "Famous Indian dish.",
        "ingredients": "['chicken', 'butter', 'onions', 'ginger', 'garlic']", 
        "method": "['cook chicken', 'add sauce', 'serve']", 
        },
    # {"id: 4", "title: Shepherd Pie", "description: Famous pie.", "ingredients: ['flour', 'eggs', 'milk', 'butter', 'beef']", "method: ['cook flour', 'add everything else', 'serve']", "favourite: True"},
    # {"id: 5", "title: Beef Stroganoff", "description: Famous Russian dish.", "ingredients: ['beef', 'onions', 'mushrooms', 'eggs', 'pepper']", "method: ['cook beef', 'add sauce', 'serve']", "favourite: False"},
    # {"id: 6", "title: Lasagne", "description: Famous Italian pasta.", "ingredients: ['pasta', 'tomato', 'lasagna sauce']", "method: ['cook pasta', 'add sauce', 'serve']", "favourite: False"},
    # {"id: 7", "title: Cheese Burger", "description: Famous American dish.", "ingredients: ['beef', 'cheese', 'buns']", "method: ['cook beef', 'add cheese', 'serve']", "favourite: True"}
]

# Perform a database operation (e.g., insert)
collection.insert_many(recipes)

# Perform a database operation (e.g., find)
recipes = collection.find({})
for recipe in recipes:
    print(recipe)