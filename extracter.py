import re

def extract_urls_from_file(filename):
    # Read the file
    with open(filename, 'r') as file:
        text = file.read()

    # Extract URLs using regular expression
    urls = re.findall(r'(https?://\S+)', text)

    # Write URLs back to the file
    with open(filename, 'w') as file:
        for url in urls:
            file.write(url + '\n')

    print('URLs extracted and written back to the file.')

# Provide the filename here
filename = 'urls.txt'
extract_urls_from_file(filename)
