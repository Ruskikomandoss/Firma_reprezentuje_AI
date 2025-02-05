import scrapy
from urllib.parse import urlparse

_START: str = "https://www.tekstowo.pl/piosenki_artysty,firma.html"
parser = urlparse(_START)



class LyricsURLSpider(scrapy.Spider):
    # name: str = "urls"
    ...


class LyricsTextSpider(scrapy.Spider):
    name: str = "lyrics"
    allowed_domains: list[str] = ["www.tekstowo.pl"]
    start_urls: list[str] = [_START]

    def parse(self, response):
        
        songs_urls = response.xpath("//div[@class='flex-group']/a[@class='title']/@href").getall()

        for url in songs_urls:
            yield {
                "url": url
            }

        next_page: str = response.xpath('//a[@class="page-link"][@title="Następna >>"]/@href').get()

        if next_page:
            yield response.follow(next_page, self.parse)

    # def parse(self, response):
    #     for song in response.xpath('//div[@class="ranking-lista"]//a/@href'):
    #         yield song
        


