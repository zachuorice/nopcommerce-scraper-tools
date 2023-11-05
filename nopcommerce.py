import requests
import beautifulsoup
import time

# A single page from a NopCommerce site, which you can fetch data from.
class NopCommercePage:
	def __init__(self, page_content):
		pass

# Internal iterator for use by NopCommerce, defaults to fetching every sitemap_entry and returning page objects.
class NopCommerceIterator:
	def __init__(self, nop_commerce_obj, fetch_interval, user_agents):
		self.nop_commerce_obj = nop_commerce_obj
		self.fetch_interval = fetch_interval
		self.user_agents = user_agents

	def __iter__(self):
		return self

	def __next__(self):
		pass

# The main class for scraping a NopCommerce site.
class NopCommerce:
	def __init__(self, sitemap_url, user_agents, fetch_interval = range(1, 10), ignore_robots = False):
		self._sitemap_url = sitemap_url
		self._sitemap_entries = []
		self.fetch_interval = fetch_interval
		self.user_agents = user_agents
		self.ignore_robots = ignore_robots

	def __iter__(self):
		return NopCommerceIterator(self, self.fetch_interval)

	def populate_sitemap_entries(self):
		pass

	@property
	def sitemap_url(self):
		return self._sitemap_url
	
	@sitemap_url.setter
	def sitemap_url(self, value):
		self._sitemap_url = value
		self._sitemap_entries = []

	@property
	def sitemap_entries(self):
		return self._sitemap_entries
	
	# Fetch the given sitemap_entry and return a NopCommercePage.
	def process(self, sitemap_entry):
		pass