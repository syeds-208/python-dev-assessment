import requests

# Base URL for JSONPlaceholder API
BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_and_display_users(num_users):
    """
    Fetches users from the JSONPlaceholder API and displays name, email, and city.
    
    Args:
        num_users (int): Number of users to display.
    
    Returns:
        None
    """
    # Endpoint for users
    url = f"{BASE_URL}/users"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Network or HTTP error occurred: {e}")
        return None

    try:
        users = response.json()
    except ValueError:
        print("Error: Response is not valid JSON.")
        return None

    if not isinstance(users, list):
        print("Error: Unexpected JSON structure. Expected a list of users.")
        return None

    for i, user in enumerate(users):
        if i >= num_users:
            break
        try:
            name = user["name"]
            email = user["email"]
            city = user["address"]["city"]
            print(f"User {i+1}: Name: {name}, Email: {email}, City: {city}")
        except KeyError as e:
            print(f"Error: Missing key {e} in user data.")
            continue

# Example usage
if __name__ == "__main__":
    print("Fetching 3 users:")
    fetch_and_display_users(3)
