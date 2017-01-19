import scrapy


class SchulenSpider(scrapy.Spider):
    """
    http://www.w3schools.com/cssref/css_selectors.asp
    """

    name = "schulen"

    def start_requests(self):
        url = 'https://www.schule.at/schulfuehrer.html'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for a in response.css('a[href*="/schulfuehrer/detail"]::attr("href")').extract():
            yield {
                'details': a
            }

        next_page = response.css('.next::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
