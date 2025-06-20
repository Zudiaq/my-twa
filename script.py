import requests

def fetch_and_print_subscriptions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        links = [line.strip() for line in f if line.strip()]

    for idx, url in enumerate(links, 1):
        print(f"\n--- Subscription #{idx}: {url} ---")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            content = response.text.strip()

            print(content)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

if __name__ == "__main__":
    fetch_and_print_subscriptions("subscriptions.txt")
