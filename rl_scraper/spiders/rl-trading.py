import scrapy
from rl_scraper.items import *

def get_items(trade_items):
    
    trades = []
    for items in trade_items.css('a.rlg-item'):
        name = str(items.css('div.rlg-item__text h2.rlg-item__name::text').get()).replace("\n", "").rstrip()
        color = str(items.css('div.rlg-item__paint::text').get()).replace("\n", "").rstrip()
        amount = str(items.css('div.rlg-item__quantity::text').get()).replace("\n", "").rstrip()
        
        trade_item = item(name= name, color= color, amount= amount)
        trades.append(trade_item)
    
    return trades

class rlSpider(scrapy.Spider):
    name="rl-trade-spider"

    start_urls = [
        'https://rocket-league.com/trading?filterItem=0&filterCertification=0&filterPaint=0&filterMinCredits=0&filterMaxCredits=100000&filterPlatform%5B%5D=1&filterSearchType=0&filterItemType=0',
    ]

    def parse(self, response):
        for trades in response.css('div.rlg-trade'):
            # get item trades
            has = get_items(trades.css('div.rlg-trade__itemshas'))
            wants = get_items(trades.css('div.rlg-trade__itemswants'))
            
            #create new trade object
            account = str(trades.css('div.rlg-trade__username::text').get()).replace("\n", "").rstrip()
            new_trade = trade(account= account, items_has= has, items_wants= wants)
            
            yield{
                'trade': new_trade
            }
