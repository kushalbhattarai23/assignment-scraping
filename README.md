
# Scrapy Wedding Spots Scraping Project

This repository contains a Scrapy project to scrape wedding venue data from the [Wedding Spot](https://www.wedding-spot.com). The data includes venue names, contact details, highlights, and guest capacities.

## Project Setup

### Prerequisites

Before setting up the project, ensure you have the following installed:

- **Anaconda** (or Miniconda)
- **Python 3.8+** (or another compatible version)
- **Scrapy** for web scraping

### Setting Up the Conda Environment

1. **Clone this repository** (or download it as a zip file):
   
   ```bash
   git clone <repository_url>
   cd assignment-scraping
   ```

2. **Create a Conda environment** from the `environment.yml` (if provided) or manually create a Conda environment:

   ```bash
   conda create --name assignment python=3.8
   ```

3. **Activate the Conda environment**:

   ```bash
   conda activate assignment
   ```

4. **Install project dependencies**:
   
   If you have a `requirements.txt` file in the repository (you do, as per your directory structure), install the required Python packages using:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, if you prefer to use Conda packages, you can install Scrapy manually within the environment:

   ```bash
   conda install -c conda-forge scrapy
   ```

### Project Structure

The project is structured as follows:

```
D:ssignment
│
└───assignment-scraping
    └───scraping
        ├───spiders
        ├───__pycache__
        ├───items.py
        ├───middlewares.py
        ├───pipelines.py
        ├───settings.py
        └───weddingspots.py
    ├───requirements.txt
    ├───scrapy.cfg
    └───weddingspots-data.csv
```

- `scraping/spiders/weddingspots.py`: The main spider that scrapes the wedding venue data.
- `scraping/items.py`: Defines the structure of the scraped data.
- `scraping/middlewares.py`: Custom middleware (if used).
- `scraping/pipelines.py`: Data processing pipelines (optional).
- `scraping/settings.py`: Configuration settings for Scrapy.

### Running the Spider

1. **Navigate to the project directory**:

   ```bash
   cd D:ssignmentssignment-scraping
   ```

2. **Run the spider** to start scraping wedding spots:

   ```bash
   scrapy crawl weddingspots
   ```

   This will begin scraping the wedding venue details and save the data to a CSV file (`weddingspots-data.csv`).

### Output

- The `weddingspots-data.csv` file will contain the following data for each wedding venue:
    - Venue Name
    - Phone Number
    - Venue Highlights
    - Guest Capacity
    - Address

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
