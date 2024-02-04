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

        next_page = response.css("li.next a ::attr(href)").get()
        if next_page is not None:
            if "catalogue/" in next_page:
                boook_url = "https://books.toscrape.com/" + next_page
            else:
                boook_url = "https://books.toscrape.com/catalogue/" + next_page
            yield response.follow(boook_url, callback=self.parse)

    def parse_book_page(self, response):
        """
        Parses the response from an individual book page on 'books.toscrape.com'.

        Extracts detailed information about a book from the provided HTML response using CSS selectors and XPath.
        The information includes the book's title, category, product type, prices, availability, number of reviews,
        star rating, and a short description.

        Args:
            response (scrapy.http.Response): The HTTP response object containing the HTML content of the book page.

        Yields:
            dict: A dictionary containing the extracted book information.
                - "url": The URL of the book page.
                - "title": The title of the book.
                - "category": The category of the book.
                - "product_type": The product type of the book.
                - "price": The price of the book.
                - "price_excl_tax": The price excluding tax.
                - "price_incl_tax": The price including tax.
                - "tax": The tax amount.
                - "availability": The availability status of the book.
                - "num_reviews": The number of reviews for the book.
                - "star_rating": The star rating of the book.
                - "book_description": The short description of the book.

        Returns:
            None
        """
        table_rows = response.css("table tr")
        yield {
            "url": response.url,
            "title": response.css(".product_main h1::text").get(),
            "category": response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
            "product_type": table_rows[1].css("td ::text").get(),
            "price": response.css("p.price_color ::text").get(),
            "price_excl_tax": table_rows[2].css("td ::text").get(),
            "price_incl_tax": table_rows[3].css("td ::text").get(),
            "tax": table_rows[4].css("td ::text").get(),
            "availability": table_rows[5].css("td ::text").get(),
            "num_reviews": table_rows[6].css("td ::text").get(),
            "star_rating": response.css("p.star-rating").attrib["class"],
            "book_description": response.xpath("//div[@id='product_description']//following-sibling::p/text()").get()
        }

