import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import tkinter as tk
from tkinter import ttk

class XSSCrawlerSpider(CrawlSpider):
    name = 'xss_crawler'

    def __init__(self, domain):
        super().__init__()
        self.allowed_domains = [domain]
        self.start_urls = [f'http://{domain}']

    rules = [
        Rule(LinkExtractor(), callback='parse_page', follow=True),
    ]

    def parse_page(self, response):
        if self.xss_vulnerable(response):
            yield {'url': response.url, 'xss_vulnerable': True}
        else:
            yield {'url': response.url, 'xss_vulnerable': False}

    def xss_vulnerable(self, response):
        if 'javascript:' in response.text or '<script>' in response.text:
            return True
        return False

def crawl(domain):
    spider = XSSCrawlerSpider(domain)
    runner = scrapy.crawler.CrawlerRunner()
    deferred = runner.crawl(spider)
    deferred.addBoth(lambda _: reactor.stop())
    reactor.run()
    print('Crawling finished!')

root = tk.Tk()
root.title('XSS Crawler')

tk.Label(root, text='Created by Meownster').pack()
tk.Label(root, text='Follow me on GitHub:').pack()
github_link = tk.Label(root, text='https://github.com/ShalabhDevliyal')
github_link.pack()

tk.Label(root, text='Enter the domain:').pack()
domain_entry = tk.Entry(root)
domain_entry.pack()

def start_crawl():
    domain = domain_entry.get()
    root.destroy()
    crawl(domain)

start_button = ttk.Button(root, text='Start Crawl', command=start_crawl)
start_button.pack()

root.mainloop()