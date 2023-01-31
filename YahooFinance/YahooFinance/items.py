# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YahoofinanceItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    change = scrapy.Field()
    change_percentage = scrapy.Field()
    market_cap = scrapy.Field()
    volume_in_currency_since_0_UTC = scrapy.Field()
    volume_in_currency_24Hr = scrapy.Field()
    total_volume_all_currencies_24Hr = scrapy.Field()
    circulating_supply = scrapy.Field()
