# Scrapy Wedding Spots Scraping Project

This project is a Scrapy-based web scraper that extracts wedding venue data from the Wedding Spot website ([https://www.wedding-spot.com](https://www.wedding-spot.com)).

## Features

*   Scrapes listings from Wedding Spot by region and paginated results.
*   Visits each venue's individual page to extract full details.
*   Captures:
    *   Venue Name
    *   Phone Number
    *   Highlights
    *   Guest Capacity
    *   Address
    *   URL of the venue
*   Sends the extracted data to a Google Spreadsheet in real-time.

## Project Setup

1.  **Prerequisites:**
    *   Python 3.8 or later
    *   Anaconda or Miniconda (recommended)
    *   Git

2.  **Setup:**
    ```bash
    git clone <repository_url>
    cd assignment-scraping
    conda create --name assignment python=3.8
    conda activate assignment
    pip install -r requirements.txt
	```

## Google Sheets Integration

To use Google Sheets as the output destination:

1. Visit Google Cloud Console: https://console.cloud.google.com/
2. Create a new project or use an existing one.
3. Enable both the following APIs:
   - Google Sheets API
   - Google Drive API
4. Create a service account under **Credentials**.
5. Generate and download the JSON key file.
6. Rename the downloaded file to `credentials.json` and place it inside the `assignment-scraping` folder.
7. Open your target Google Sheet in a browser.
8. Share the sheet with the service account email (usually ends with `@project-id.iam.gserviceaccount.com`) and assign **Editor** permission.

> **Important:** Make sure `credentials.json` is included in your `.gitignore` file to prevent uploading sensitive credentials to GitHub.

## Google Sheet Details

- The project expects the Google Sheet to be named exactly:  
  **WeddingVenuesData**

- The spider writes data to the first sheet (**Sheet1**) of this Google Sheet.

- To use a different sheet name, update the sheet name in the pipeline code accordingly.

## Project Structure

```
assignment-scraping/
├── scraping/
│   ├── spiders/
│   │   └── weddingspots.py          -> Main spider script
│   ├── items.py                     -> (optional) Defines Scrapy Items
│   ├── middlewares.py               -> (optional) Custom middlewares
│   ├── pipelines.py                 -> Pipeline that sends data to Google Sheets
│   ├── settings.py                  -> Project configuration
│   └── __pycache__/                 -> Compiled bytecode
├── .gitignore                      -> Should include credentials.json and other ignored files
├── credentials.json                -> Google API service account key (do not commit)
├── requirements.txt                -> List of all required Python packages
├── scrapy.cfg                      -> Scrapy project file
└── weddingspots-data.csv           -> Local optional CSV export (can be added in pipeline)
```

## Running the Spider

1. Open your terminal or Anaconda prompt.
2. Navigate to the project directory:  
   ```bash
   cd assignment-scraping
   ```
3. Run the spider:  
   ```bash
   scrapy crawl weddingspots
   ```

---
