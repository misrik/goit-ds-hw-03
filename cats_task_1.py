# "mongodb+srv://polina:ZpKR1wedUi59dSmN@cluster0.gt9kg.mongodb.net/"
from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://polina:ZpKR1wedUi59dSmN@cluster0.gt9kg.mongodb.net/",
    server_api=ServerApi('1')
)

db = client['test'] 
collection = db['cats'] 

def get_all_cats(): # список всіх котів
    cats = db['cats'].find()  
    for cat in cats:
        print(cat) 

def get_cat_by_name(name): # виводимо кота за іменем
    cat = db.cats.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Cat named {name} was not found.")

def update_age(name, new_age):
    cat = db.cats.find_one({"name": name})
    if not cat:
        print(f"Cat named {name} was not found.")
        return  # Виходимо з функції, якщо кота немає
    
    db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
    result = db.cats.find_one({"name": name})
    print(result)

def update_features(name, new_feature):
    cat = db.cats.find_one({"name": name})
    if not cat:
        print(f"Cat named {name} was not found.")
        return  # Виходимо з функції, якщо кота немає

    # Перевірка, чи існує нова характеристика
    if new_feature in cat.get("features", []):
        print(f"Feature '{new_feature}' already exists for {name}.")
        return  # Якщо характеристика вже є, нічого не робимо
    
    else:
        # якщо характеристики немає, додаємо її
        db.cats.update_one({"name": name}, {"$push": {"features": new_feature}})
        print(f"Feature '{new_feature}' has been added for cat named {name}.")

    updated_cat = db.cats.find_one({"name": name})
    print(updated_cat)


def delete_a_cat(name):
    cat = db.cats.find_one({"name": name})
    if not cat:
        print(f"Cat named {name} was not found.")
        return  # Виходимо з функції, якщо кота немає
    # Якщо кіт знайдений, видаляємо
    db.cats.delete_one({"name": name})
    print(f"Cat named {name} has been deleted.")

def delete_all_cats():
    db.cats.delete_many({})
    print("Cats have been deleted.")

get_all_cats()  
get_cat_by_name("Murchyk")
update_age("barsik", 4)
update_age("Michelle", 8)
update_features("Michelle", "hazel eyes")
update_features("Liza", "має пухнастий хвіст")
update_features("Lama", "має короткий хвіст")
delete_a_cat("Dariy")
#delete_all_cats()