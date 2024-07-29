# GitHub README Fetcher

This Python script fetches and displays the contents of the `README.md` files from a list of specified GitHub repositories.

## Features

- Fetches the raw Markdown content of `README.md` files from GitHub repositories.
- Displays the content in the console.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/William2716057/githubReadmeScrape.git
    ```

2. Install the required Python libraries:

    ```bash
    pip install requests
    ```

## Usage

1. Modify the `repo_urls` list in the `main()` function to include the URLs of the GitHub repositories you want to fetch the `README.md` files from.

    ```python
    repo_urls = [
        "https://github.com/repository1",
        "https://github.com/repository2",
        "https://github.com/repository3"
    ]
    ```

2. Run the script:

    ```bash
    python fetch_readme.py
    ```

3. The script will print the contents of the `README.md` files for the specified repositories.

## Example Output

```plaintext
README content for https://github.com/repository1:

# Repository1
This repository contains...

================================================================================

README content for https://github.com/repository2:

# Repository2
This project aims to...

================================================================================

README content for https://github.com/repository3:

# Repository3
A collection of...

================================================================================
