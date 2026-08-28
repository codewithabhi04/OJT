from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

def scrape_foundit(role="Data", location="India", max_jobs=100):
    driver = webdriver.Chrome()
    jobs = []

    for page in range(1, 4):
        url = f"https://www.foundit.in/srp/results?query={role}&locations={location}&page={page}"
        driver.get(url)
        time.sleep(5)

        job_cards = driver.find_elements(By.CSS_SELECTOR, "div.cardContainer")

        for job in job_cards:

            try:
                title = job.find_element(By.CSS_SELECTOR, ".jobTitle").text
            except:
                title = "N/A"

            try:
                company = job.find_element(By.CSS_SELECTOR, ".companyName").text
            except:
                company = "N/A"

            # ✅ Link
            try:
                link = job.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            except:
                link = "N/A"

            # =========================
            # 📍 LOCATION (FIXED ONLY)
            # =========================
            text = job.text.lower()   # ✅ REQUIRED LINE

            location_val = "N/A"

            # prioritize remote first
            if "remote" in text:
                location_val = "Remote"
            else:
                locations_list = [
                    "mumbai", "pune", "bangalore", "delhi",
                    "hyderabad", "chennai", "gurgaon",
                    "noida", "kolkata", "india"
                ]

                for loc in locations_list:
                    if loc in text:
                        location_val = loc.title()
                        break

            # =========================
            # EXPERIENCE (UNCHANGED)
            # =========================
            try:
                experience = job.find_element(By.CSS_SELECTOR, ".exp").text
            except:
                match = re.search(r'\d+\s*-\s*\d+\s*(years|yrs)', text)
                experience = match.group() if match else "N/A"

            salary = "Not Disclosed"

            jobs.append({
                "title": title,
                "company": company,
                "location": location_val,
                "experience": experience,
                "salary": salary,
                "link": link,
                "source": "Foundit"
            })

            if len(jobs) >= max_jobs:
                break

        if len(jobs) >= max_jobs:
            break

    driver.quit()
    return jobs