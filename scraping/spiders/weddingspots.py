import scrapy
import scrapy
from scrapy.http import Response, Request
import re  # For regex matching


class WeddingspotsSpider(scrapy.Spider):
    name = "weddingspots"
    allowed_domains = ['wedding-spot.com']
    start_urls = ['https://www.wedding-spot.com/wedding-venues/?pr=new%20jersey&r=new%20jersey%3anorth%20jersey&r=new%20jersey%3aatlantic%20city&r=new%20jersey%3ajersey%20shore&r=new%20jersey%3asouth%20jersey&r=new%20jersey%3acentral%20jersey&r=new%20york%3along%20island&r=new%20york%3amanhattan&r=new%20york%3abrooklyn&r=pennsylvania%3aphiladelphia&sr=1']
    count = 0  # Counter to track the number of URLs extracted
    max_count = 108 # Maximum number of URLs to extract
    current_page = 1  # Starting page for pagination

    def parse(self, response: Response):
        # Extract product URLs from the listing page
        product_cards = response.xpath('//*[@id="stickyBoundary"]/div[2]/div/div[1]/div')

        for product in product_cards:
            if self.count >= self.max_count:
                return  # Stop further processing

            url = product.xpath('./a/@href').get()
            if url:
                absolute_url = response.urljoin(url)
                yield Request(absolute_url, callback=self.parse_product)
                self.count += 1  # Increment count after yielding a URL

        # Pagination Handling
        if self.count < self.max_count:
            self.current_page += 1  # Increment the page number for the next request

            # Generate the next page URL based on the pattern provided
            next_page_url = f"https://www.wedding-spot.com/wedding-venues/?page={self.current_page}&pr=new%20jersey&r=new%20jersey%3anorth%20jersey&r=new%20jersey%3aatlantic%20city&r=new%20jersey%3ajersey%20shore&r=new%20jersey%3asouth%20jersey&r=new%20jersey%3acentral%20jersey&r=new%20york%3along%20island&r=new%20york%3amanhattan&r=new%20york%3abrooklyn&r=pennsylvania%3aphiladelphia&sr=1"
            
            # Make the request to the next page
            yield Request(next_page_url, callback=self.parse)

    def parse_product(self, response: Response):
        # Extract the details from the venue's page
        venue_name = response.xpath('//*[@id="ws-react-app"]/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/text()').get()

        # Extract the phone number from the 'tel:' link
        number = response.xpath('//*[@id="call-venue"]/span[2]/text()').get()
        if number:
            cleaned_text = number.replace("-", "").replace(" ", "")  # Remove hyphens and spaces
            cleaned_number = cleaned_text.split("ext.")[0]
            phone = cleaned_number  # Take the cleaned number as phone
            
        else:
            phone = 'N/A'

        # Extract venue highlights using a while loop
        venue_highlights = []
        i = 1  # Start with div[1]

        while True:
            # Construct XPath for the current div element
            xpath = f'//*[@id="ws-react-app"]/div[1]/div[3]/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[{i}]/div/text()'
            highlight = response.xpath(xpath).get()

            # If no highlight is found, break the loop
            if not highlight:
                break

            # Add the highlight to the list
            venue_highlights.append(highlight.strip())

            # Increment the index for the next div
            i += 1

        # If venue highlights are empty, set to "N/A"
        if not venue_highlights:
            venue_highlights = ["N/A"]

        # Combine the highlights into a single string
        venue_highlights = ', '.join(venue_highlights)

        # Extract only the numeric value for guest capacity
        guest_capacity_text = response.xpath('//*[@id="ws-react-app"]/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[2]/div/p/text()').get()
        guest_capacity = self.extract_number(guest_capacity_text)  # Use regex to extract number

        address1 = response.xpath('//*[@id="ws-react-app"]/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[4]/div/p/text()').get()
        address2 = response.xpath('//*[@id="ws-react-app"]/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[4]/div/p/span/text()').get()
        if address1 and address2:
            address = address1 + " , " + address2
        else:
            address = 'N/A'

        # Yield the details (Scrapy will save this to the CSV automatically)
        yield {
            'Url': response.url,
            'Venue Name': venue_name.strip() if venue_name else 'N/A',
            'Phone': phone.strip(),
            'Venue Highlights': venue_highlights.strip(),
            'Guest Capacity': guest_capacity,  # Just the number
            'Address': address.strip(),
        }

    def extract_number(self, text):
        """Extract the numeric value from a string using regex."""
        if text:
            match = re.search(r'\d+', text)  # Search for the first sequence of digits
            if match:
                return match.group()  # Return the matched number
        return 'N/A'  # Return 'N/A' if no number is found
