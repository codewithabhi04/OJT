from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_naukri(role="Data Scientist", location="India", max_jobs=100):
    driver = webdriver.Chrome()
    jobs = []
    page = 1

    while len(jobs) < max_jobs:
        url = f"https://www.naukri.com/{role.replace(' ','-').lower()}-jobs-in-{location.lower()}-{page}"
        driver.get(url)

        time.sleep(5)

        job_cards = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")

        for job in job_cards:
            try:
                title = job.find_element(By.CSS_SELECTOR, "a.title").text
            except:
                title = "N/A"

            try:
                company = job.find_element(By.CSS_SELECTOR, "a.comp-name").text
            except:
                company = "N/A"

            try:
                loc = job.find_element(By.CSS_SELECTOR, ".locWdth").text
            except:
                loc = "N/A"

            try:
                exp = job.find_element(By.CSS_SELECTOR, ".expwdth").text
            except:
                exp = "N/A"

            try:
                salary = job.find_element(By.CSS_SELECTOR, ".sal-wrap span").text
            except:
                salary = "Not Disclosed"
            # ✅ Job Link
            try:
                link = job.find_element(By.CSS_SELECTOR, "a.title").get_attribute("href")
            except:
                link = "N/A"

            jobs.append({
                "title": title,
                "company": company,
                "location": loc,
                "experience": exp,
                "salary": salary,
                "link": link, 
                "source": "Naukri"
            })

            if len(jobs) >= max_jobs:
                break

        page += 1

    driver.quit()
    return jobs