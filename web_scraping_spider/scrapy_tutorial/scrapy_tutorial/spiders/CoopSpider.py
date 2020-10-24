import scrapy

class CoopSpider(scrapy.Spider):
    name = "CoopSpider"
    start_urls = [
        'https://www.coop.ch/en/inspiration-gifts/new-products/c/m_1061'
    ]

    def parse(self, response):
        productName = response.css(".productTile-details__name-value::text").extract()
        yield {'productName': productName}

