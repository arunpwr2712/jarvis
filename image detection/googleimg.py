#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


import wikipedia

def get_person_summary(name):
    try:
        page = wikipedia.page(name)
        summary = page.summary
        return summary
    except wikipedia.exceptions.PageError:
        return "Sorry, no information found for that person."
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]  # Limiting the number of options to display
        options_text = "\n".join(options)
        return f"Multiple options found. Please specify:\n{options_text}"

# Example usage
person_name = input("Enter the name of the person: ")
summary = get_person_summary(person_name)
print(summary)







































# import requests
# from bs4 import BeautifulSoup

# # Function to upload an image to Google Images and retrieve its description
# def upload_image_and_get_description(image_path):
#     # Read the image file as binary data
#     with open(image_path, 'rb') as image_file:
#         image_data = image_file.read()

#     # Prepare the payload for the POST request
#     files = {'encoded_image': image_data}
#     params = {
#         'image_url': '',
#         'image_content': '',
#         'filename': '',
#         'hl': 'en',
#     }

#     # Send the POST request to Google Images
#     response = requests.post('https://www.google.com/searchbyimage/upload', files=files, params=params)

#     # Parse the response HTML
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Extract the image description
#     description = soup.find('a', class_='iu-card-header').text.strip()

#     # Print the image description
#     print(description)

# # Example usage
# image_path = 'images/elon_musk.jpg'
# upload_image_and_get_description(image_path)
