import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        """
        Parses the response from the main page of the 'books.toscrape.com' website.

        Extracts information about books from the provided HTML response using CSS selectors.
        For each book, follows the link to its detailed page and invokes the 'parse_book_page'
        callback to extract additional information.

        Args:
            response (scrapy.http.Response): The HTTP response object containing the HTML content.

        Yields:
            scrapy.Request: A scrapy Request object to follow links to individual book pages.

        Returns:
            None
        """
        books = response.css("article.product_pod")

        for book in books:
            relative_url = book.css("h3 a ::attr(href)").get()

            if "catalogue/" in relative_url:
                next_page_url = "https://books.toscrape.com/" + relative_url
            else:
                next_page_url = "https://books.toscrape.com/catalogue/" + relative_url
            yield response.follow(next_page_url, callback=self.parse_book_page)

        if next_page is not None:
            if "catalogue/" in next_page:
                boook_url = "https://books.toscrape.com/" + next_page
            else:
                boook_url = "https://books.toscrape.com/catalogue/" + next_page
            yield response.follow(boook_url, callback=self.parse)

    def parse_book_page(self, rsponse):
        pass
