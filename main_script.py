import requests
from typing import List

class WebScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def create_list_of_website_links(self, page_url: str) -> List[str]:
        """
        Extracts and returns a list of links from a given webpage.

        Parameters:
        - page_url (str): The URL of the webpage to extract links from.

        Returns:
        - List[str]: A list of extracted links.
        """
        full_url = self.base_url + page_url
        response = requests.get(full_url)
        if response.status_code == 200:
            links = self.extract_links_from_html(response.text)
            return links
        else:
            print(f"Failed to fetch data from {full_url}")
            return []

    def extract_links_from_html(self, html_content: str) -> List[str]:
        """
        Extracts and returns links from HTML content.

        Parameters:
        - html_content (str): The HTML content to extract links from.

        Returns:
        - List[str]: A list of extracted links.
        """

if __name__ == "__main__":
    base_url = "https://example.com"
    web_scraper = WebScraper(base_url)

    page_url = "/articles"
    links = web_scraper.create_list_of_website_links(page_url)
    print(links)
