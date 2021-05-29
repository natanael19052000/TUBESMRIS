import scrapy


class QuotesSpider(scrapy.Spider):
    name = "novel"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'hasil-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
        print (filename)