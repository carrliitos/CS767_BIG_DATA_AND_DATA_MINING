import scrapy


class RottentomatoesSpider(scrapy.Spider):
    name = "rottentomatoes"
    allowed_domains = ["www.listchallenges.com"]
    
    def __init__(self, *args, **kwargs):
        super(RottentomatoesSpider, self).__init__(*args, **kwargs)
        self.base_url = "https://www.listchallenges.com/1000-best-films-with-a-90-100-rating-on-rotten"
        self.start_urls = [self.base_url] + [f"{self.base_url}/list/{i}" for i in range(2, 26)]

    def parse(self, response):
        print(response.text)
