import requests

def fetch_readme(repo_url):
    # Modify the URL to fetch the raw content
    readme_url = repo_url.replace("github.com", "raw.githubusercontent.com") + "/master/README.md"
    response = requests.get(readme_url)

    if response.status_code == 200:
        return response.text.strip()
    else:
        print(f"Failed to fetch README from {repo_url}")
        return None

def main():
    # List of GitHub repository URLs
    repo_urls = [
        "https://github.com/repository1",
        "https://github.com/repository2",
        "https://github.com/repository3"
    ]

    for url in repo_urls:
        readme_content = fetch_readme(url)
        if readme_content:
            print(f"README content for {url}:\n")
            print(readme_content)
            print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    main()