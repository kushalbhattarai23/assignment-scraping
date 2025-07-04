import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetsPipeline:
    def open_spider(self, spider):
        # Define the scope
        scope = ["https://spreadsheets.google.com/feeds",
                 "https://www.googleapis.com/auth/spreadsheets",
                 "https://www.googleapis.com/auth/drive.file",
                 "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)

        # Open the sheet
        self.sheet = client.open("WeddingVenuesData").sheet1  # Replace with your actual sheet name

        # Write headers only once
        self.sheet.append_row(['Url', 'Venue Name', 'Phone', 'Venue Highlights', 'Guest Capacity', 'Address'])

    def process_item(self, item, spider):
        # Append the item to the sheet
        self.sheet.append_row([
            item['Url'],
            item['Venue Name'],
            item['Phone'],
            item['Venue Highlights'],
            item['Guest Capacity'],
            item['Address']
        ])
        return item
