import scrapy
import json
from pathlib import Path
from bs4 import BeautifulSoup

class BootstarpSpider(scrapy.Spider):
    name = 'bootstrap_spider'
    allowed_domains = ['getbootstrap.com']
    start_urls = [ 'https://getbootstrap.com/docs/5.3/getting-started/introduction/']
    
    custom_settings = {
        'DEPTH_LIMIT': 2,
    }
    count = 0

    def parse(self, response):
        try:
            if not response.url.startswith('https://getbootstrap.com/docs/5.3'):
                return
            
            self.count += 1

            if self.count > 500: # limit to 500 files
                return
            
            page_title = response.css('h1::text').get()
            filename = f"bootstrap-{self.count}.json"

            # Extracting text from all children of <main> tag
            main_content = response.xpath('//main//*//text()').getall()
        
            # Joining the extracted text
            extracted_text = ''.join(main_content).strip()
            extracted_text = extracted_text.replace("\n", "")

            data = {
                "id": self.count,
                "url": response.url,
                "title": page_title,
                "content": extracted_text,
            }

            with open(filename, "w") as json_file:
                json.dump(data, json_file, indent=4)
                self.log(f"Saved file {filename}")

        except:
            self.count -= 1
        
        # Follow links to other pages
        for next_page in response.css('a::attr(href)').getall():
            yield response.follow(next_page, callback=self.parse)
