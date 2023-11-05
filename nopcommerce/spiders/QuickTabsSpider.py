from pathlib import Path

import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from ..items import QuickTabItem

class QuickTabsSpider(SitemapSpider):
    name = "quicktabs"
    sitemap_urls = []
    tabs_file = ""
    link_extractor = LinkExtractor()

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        cls.sitemap_urls = [crawler.settings.get('SITEMAP_URL')]
        spider = super(SitemapSpider, cls).from_crawler(crawler, *args, **kwargs)
        return spider

    def parse_tab(self, response, text, slug):
        yield QuickTabItem(content=response.body, name=text, product_slug=slug, content_url=response.url)

    def parse(self, response):
        slug = response.url.split("/")[-1]
        self.log(f"Scraping {response.url}")
        for link in self.link_extractor.extract_links(response):
            if "ProductTab/ProductCustomTab" in link.url:
                self.log(f"Parsing tab: {link.text} from {link.url} on product {slug}")
                yield Request(link.url, callback=lambda r: self.parse_tab(r, link.text, slug))