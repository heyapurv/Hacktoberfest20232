import hashlib

# Dictionary to store URL mappings (for simplicity, using a dictionary in-memory)
url_mapping = {}

# Function to shorten a URL
def shorten_url(url):
    # Hash the URL to generate a unique key
    md5_hash = hashlib.md5(url.encode()).hexdigest()
    short_key = md5_hash[:6]  # Use the first 6 characters of the hash as the key

    # Store the mapping in the dictionary
    url_mapping[short_key] = url

    return f"Your shortened URL: http://your-short-domain/{short_key}"

# Function to expand a shortened URL
def expand_url(short_url):
    # Extract the key from the short URL
    short_key = short_url.split("/")[-1]

    # Retrieve the original URL from the dictionary
    original_url = url_mapping.get(short_key)

    if original_url:
        return f"Original URL: {original_url}"
    else:
        return "Short URL not found."

# Main program
while True:
    print("Options:")
    print("1. Shorten a URL")
    print("2. Expand a shortened URL")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        long_url = input("Enter the URL to shorten: ")
        short_url = shorten_url(long_url)
        print(short_url)
    elif choice == '2':
        short_url = input("Enter the shortened URL: ")
        expanded_url = expand_url(short_url)
        print(expanded_url)
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
