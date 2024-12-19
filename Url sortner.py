import hashlib
import os

# File to store mappings
DB_FILE = "url_db.txt"

def load_mappings():
    """Load URL mappings from the file."""
    mappings = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            for line in f:
                short_url, long_url = line.strip().split(',')
                mappings[short_url] = long_url
    return mappings

def save_mapping(short_url, long_url):
    """Save a new URL mapping to the file."""
    with open(DB_FILE, 'a') as f:
        f.write(f"{short_url},{long_url}\n")

def generate_short_url(long_url):
    """Generate a short URL using a hash."""
    # Generate a hash of the long URL
    hash_object = hashlib.md5(long_url.encode())
    # Take the first 6 characters of the hash as the unique key
    short_key = hash_object.hexdigest()[:6]
    return short_key

def shorten_url(long_url):
    """Shorten the URL and store it in the file."""
    mappings = load_mappings()

    # Check if URL is already shortened
    for short_url, stored_url in mappings.items():
        if stored_url == long_url:
            print(f"URL is already shortened: {short_url}")
            return short_url

    # Create a new short URL
    short_url = generate_short_url(long_url)
    mappings[short_url] = long_url
    save_mapping(short_url, long_url)
    print(f"Shortened URL: {short_url}")
    return short_url

def retrieve_long_url(short_url):
    """Retrieve the long URL given the short URL."""
    mappings = load_mappings()
    long_url = mappings.get(short_url)
    if long_url:
        print(f"Original URL: {long_url}")
        return long_url
    else:
        print("Short URL not found.")
        return None

# Example Usage
if __name__ == "__main__":
    print("URL Shortener")
    while True:
        choice = input("\n1. Shorten URL\n2. Retrieve URL\n3. Exit\nChoose an option: ")
        
        if choice == "1":
            long_url = input("Enter the URL to shorten: ")
            shorten_url(long_url)
        elif choice == "2":
            short_url = input("Enter the short URL to retrieve: ")
            retrieve_long_url(short_url)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")