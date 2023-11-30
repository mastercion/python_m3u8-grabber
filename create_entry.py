import json
import os

def get_user_input():
    tvg_name = input("Enter TVG Name: ")
    tvg_id = input("Enter TVG ID: ")
    tvg_logo = input("Enter TVG Logo URL: ")
    channel_name = input("Enter Channel Name: ")
    channel_url = input("Enter Channel URL: ")

    # Predefined list for group-title
    group_titles = ["Vollprogramm", "Spartenprogramm", "Nachrichten", "Dokumentationen", "Sport", "Kinder", "Teleshopping", "Regional"]
    print("Choose a Group Title:")
    for i, title in enumerate(group_titles, 1):
        print(f"{i}. {title}")

    # Getting user selection for group-title
    group_title_index = int(input("Enter the number corresponding to your choice: ")) - 1

    # Validate selection
    if 0 <= group_title_index < len(group_titles):
        group_title = group_titles[group_title_index]
    else:
        print("Invalid selection. Exiting.")
        return

    return {
        "tvg-name": tvg_name,
        "tvg-id": tvg_id,
        "group-title": group_title,
        "tvg-logo": tvg_logo,
        "channel_name": channel_name,
        "channel_url": channel_url
    }

def save_to_json(data):
    # Create a directory named 'programms' if it doesn't exist
    os.makedirs('programms', exist_ok=True)

    file_name = f"programms/{data['tvg-id']}.json"
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {file_name}")

# Get user input
user_input = get_user_input()
if user_input:
    # Save the data to a JSON file
    save_to_json(user_input)
else:
    print("No valid input provided.")
