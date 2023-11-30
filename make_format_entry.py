import json
import os

def read_json_and_format(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    formatted_text = (
        f"#EXTINF:-1 tvg-name=\"{data['tvg-name']}\" "
        f"tvg-id=\"{data['tvg-id']}\" "
        f"group-title=\"{data['group-title']}\" "
        f"tvg-logo=\"{data['tvg-logo']}\","
        f"{data['channel_name']}\n"
        f"{data['channel_url']}\n"
    )

    return formatted_text

def process_directory(directory):
    # Open the output file and write "#EXTM3U" at the top
    with open('kodi_tv_test.m3u', 'w') as output_file:
        output_file.write("#EXTM3U\n")

    # Process each JSON file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            formatted_text = read_json_and_format(file_path)

            # Append the formatted text to the output file
            with open('kodi_tv_test.m3u', 'a') as output_file:
                output_file.write(formatted_text)

# Directory containing JSON files
directory_path = 'programms'  # Replace with your directory path
process_directory(directory_path)
