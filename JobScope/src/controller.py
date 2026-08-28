from scraper.naukri_scraper import scrape_naukri
from scraper.foundit_scraper import scrape_foundit

def get_all_jobs(role, location):
    data1 = scrape_naukri(role, location, max_jobs=100)
    data2 = scrape_foundit(role, location, max_jobs=100)

    return data1 + data2