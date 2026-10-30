
import json
import random
from PIL import Image

json_data_string = '{"University": ["T-shirt + Jeans + Shoes", "Hoodie + Shorts + Sneakers"],"Birthday": ["Blouse + Skirt + Heels", "Crop Top + Trousers + Boots"],"Sport": ["T-shirt + Shorts + Running Shoes", "Tank Top + Leggings + Sneakers"],"Work": ["Shirt + Trousers + Loafers", "Blazer + Trousers + Sneakers"],"Travel": ["Hoodie + Sweatpants + Ballet Flats", "Long-sleeve T-shirt + Cargo Pants + Flip-flops"]}'

json_data = json.loads(json_data_string)

def get_outfit_recommendation(outfit_options, occasion):
    global last_outfit

    available_outfits = [outfit for outfit in outfit_options if outfit != last_outfit]

    selected_outfit= random.choice (available_outfits)
    last_outfit = selected_outfit

    print(selected_outfit)
    outfit_number = outfit_options.index(selected_outfit) + 1
    image_path = f"images/{occasion}_{outfit_number}.jpg"
    image = Image.open(image_path)
    image.show()
    return selected_outfit

last_outfit = None
answer ="yes"
favourites = []

print("Welcome to Style My Day! Get outfit recommendations for different occasions.")
print("1. University")
print("2. Birthday")
print("3. Sport")
print("4. Work")
print("5. Travel")



while answer == "yes":
    choice = input("Please enter the number corresponding to your occasion: ").strip()
    if choice == "1":
        occasion = "University"
    elif choice == "2":
        occasion = "Birthday"
    elif choice == "3":
        occasion = "Sport"
    elif choice == "4":
        occasion = "Work"
    elif choice == "5":
        occasion = "Travel"
    else:
        print("Invalid choice. Please try again.")
        continue

    if occasion == "University":
        selected_outfit = get_outfit_recommendation(json_data[occasion], occasion)
    elif occasion == "Birthday":
        selected_outfit = get_outfit_recommendation(json_data[occasion], occasion)
    elif occasion == "Sport":
        selected_outfit = get_outfit_recommendation(json_data[occasion], occasion)
    elif occasion == "Work":
        selected_outfit = get_outfit_recommendation(json_data[occasion], occasion)
    elif occasion == "Travel":
        selected_outfit = get_outfit_recommendation(json_data[occasion], occasion)
    else:
        print("Invalid occasion. Please try again.")
    save = input("Would you like to save this outfit? (yes/no): ").strip().lower()
    if save == "yes":
        favourites.append(selected_outfit)
        print("Outfit added to favourites!")

    answer = input("Do you want to get another outfit recommendation? (yes/no): ").strip().lower()

print("Your favourite outfits are:")

if favourites:
    for outfit in favourites:
        print(outfit)
else:  
    print("No favourite outfits saved.")

print ("Thank you for using Style My Day!")


