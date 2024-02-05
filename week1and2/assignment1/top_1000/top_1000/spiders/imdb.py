import scrapy

class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/list/ls048276758/",
                  "https://www.imdb.com/list/ls048276758/?sort=list_order,asc&st_dt=&mode=detail&page=2",
                  "https://www.imdb.com/list/ls048276758/?sort=list_order,asc&st_dt=&mode=detail&page=3",
                  "https://www.imdb.com/list/ls048276758/?sort=list_order,asc&st_dt=&mode=detail&page=4",
                  "https://www.imdb.com/list/ls048276758/?sort=list_order,asc&st_dt=&mode=detail&page=5",
                  "https://www.imdb.com/list/ls048276758/?sort=list_order,asc&st_dt=&mode=detail&page=6",
                  "https://www.imdb.com/list/ls048276758/?sort=list_order,asc&st_dt=&mode=detail&page=7",
                  "https://www.imdb.com/list/ls048276758/?sort=list_order,asc&st_dt=&mode=detail&page=8",
                  "https://www.imdb.com/list/ls048276758/?sort=list_order,asc&st_dt=&mode=detail&page=9",
                  "https://www.imdb.com/list/ls048276758/?sort=list_order,asc&st_dt=&mode=detail&page=10"]

    def parse(self, response):
        print(response.text)
