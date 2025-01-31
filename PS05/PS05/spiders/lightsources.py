import scrapy

class LightsourcesSpider(scrapy.Spider):
    name = "lightsources"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/rostov-na-donu/category/svet"]

    def parse(self, response):
        lights = response.css('div._Ud0k')
        for light in lights:
            yield {
                'name': light.css('div.lsooF span::text').get(),
                'price': light.css('div.q5Uds span::text').get(),
                'url': light.css('a').attrib['href']
            }
