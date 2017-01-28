import scrapy
from utils import is_address, remove_white


class SchulenSpider(scrapy.Spider):
    DOWNLOAD_DELAY = 0.25

    """
    http://www.w3schools.com/cssref/css_selectors.asp
    """
    name = "schulen"
    start_urls = ['https://www.schule.at/schulfuehrer.html']

    def parse(self, response):
        for a in response.css('a[href*="/schulfuehrer/detail"]::attr("href")').extract():
            yield scrapy.Request(response.urljoin(a), callback=self.parse_school)

        next_page = response.css('.next::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_school(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first()

        address = None
        for candidate in response.css('article p::text').extract():
            candidate = remove_white(candidate)
            if is_address(candidate):
                if address is None:
                    address = candidate
                elif len(address) < len(candidate):
                    address = candidate

        attributes = {
            'name': extract_with_css('div[id="cms-content"] h1::text'),
            'address': address,
            'email': extract_with_css('article p a[href*="mailto"]::text'),
            'homepage': extract_with_css('article p a[href*="http"]::text'),
        }

        yield attributes
