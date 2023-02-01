import scrapy
from scrapy_splash import SplashRequest
from ..items import YahoofinanceItem

per_page_count = 100
data_count = 8924
offset = (data_count // per_page_count) * per_page_count

class YahooSpider(scrapy.Spider):
    name = 'yahoo'

    def start_requests(self):
        global offset, per_page_count
        
        for i in range(0, offset+1, per_page_count):
            yield SplashRequest(f'https://finance.yahoo.com/crypto/?count={per_page_count}&offset={i}',
                callback=self.parse,
                args={'wait': 1, 'timeout': 300}
            )

    def parse(self, response):
        item = YahoofinanceItem()
        rows = response.css('tbody tr')
        
        for row in rows:
            item['name'] = row.css('a::text').get()
            item['price'] = row.css('fin-streamer[data-field="regularMarketPrice"]::text').get()
            item['change'] = row.css('fin-streamer[data-field="regularMarketChange"] span::text').get()
            item['change_percentage'] = row.css('fin-streamer[data-field="regularMarketChangePercent"] span::text').get()
            item['market_cap'] = row.css('fin-streamer[data-field="marketCap"]::text').get()
            item['volume_in_currency_since_0_UTC'] = row.css('td[aria-label="Volume in Currency (Since 0:00 UTC)"]::text').get()
            item['volume_in_currency_24Hr'] = row.css('td[aria-label="Volume in Currency (24Hr)"]::text').get()
            item['total_volume_all_currencies_24Hr'] = row.css('td[aria-label="Total Volume All Currencies (24Hr)"]::text').get()
            item['circulating_supply'] = row.css('td[aria-label="Circulating Supply"]::text').get()
            yield item