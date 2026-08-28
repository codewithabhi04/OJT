# 💼 JobScope – Job Scraping & Market Analyzer

**JobScope** is a Python-based job scraping and analysis application that collects job listings from multiple job portals and presents them through an interactive **Streamlit dashboard**.

The application allows users to search for jobs by **role and location**, collect job information from **Naukri and Foundit**, filter the results, analyze job-market data, and download the collected information as a CSV file.

---

## 🚀 Features

* 🔍 Search jobs by **Job Role** and **Location**
* 🌐 Scrape job listings from:

  * Naukri
  * Foundit
* 📄 Collect important job details:

  * Job Title
  * Company
  * Location
  * Experience
  * Salary
  * Job Link
  * Job Source
* 🧹 Remove duplicate job listings
* 🔎 Search and filter jobs by company and location
* 📊 Interactive job-market dashboard
* 📈 Jobs by platform analysis
* 🏢 Top companies analysis
* 📍 Top job locations analysis
* 📥 Download job data as CSV
* 💻 Simple and user-friendly Streamlit interface

---

## 🛠️ Technologies Used

| Technology           | Purpose                          |
| -------------------- | -------------------------------- |
| **Python**           | Core programming language        |
| **Streamlit**        | Web dashboard and user interface |
| **Selenium**         | Automated web scraping           |
| **Pandas**           | Data processing and cleaning     |
| **BeautifulSoup4**   | HTML parsing support             |
| **Requests**         | HTTP requests                    |
| **Chrome WebDriver** | Browser automation               |

---

## 🏗️ Project Architecture

```text
JobScope
│
├── app.py
│
├── scraper/
│   ├── __init__.py
│   ├── naukri_scraper.py
│   └── foundit_scraper.py
│
├── src/
│   ├── __init__.py
│   ├── controller.py
│   ├── data_cleaning.py
│   └── analyzer.py
│
├── data/
│
├── .streamlit/
│   └── config.toml
│
└── requirements.txt
```

---

## 📌 Project Workflow

```text
User enters Job Role & Location
              ↓
        Search Jobs
              ↓
     ┌────────┴────────┐
     ↓                 ↓
  Naukri            Foundit
 Scraper            Scraper
     ↓                 ↓
     └────────┬────────┘
              ↓
       Combine Job Data
              ↓
        Data Cleaning
              ↓
       Remove Duplicates
              ↓
       Streamlit Dashboard
              ↓
   ┌──────────┼──────────┐
   ↓          ↓          ↓
 Filters    Charts    Job Search
              ↓
        Download CSV
```

---

## ⚙️ How It Works

### 1. User Input

The user enters:

* Job Role
* Location

For example:

```text
Job Role: Data Scientist
Location: India
```

### 2. Web Scraping

When the user clicks **Search Jobs**, Selenium opens the job portals and extracts available job listings.

The project currently uses:

* **Naukri**
* **Foundit**

### 3. Data Collection

The application extracts information such as:

```text
Job Title
Company
Location
Experience
Salary
Job Link
Source
```

### 4. Data Cleaning

The collected data is converted into a Pandas DataFrame.

Duplicate jobs are removed based on:

```text
Job Title + Company
```

Missing values are replaced with:

```text
N/A
```

### 5. Dashboard

The cleaned data is displayed in the Streamlit dashboard.

Users can:

* Filter by company
* Filter by location
* Search job listings
* View job statistics
* Open job links

### 6. Data Analysis

The dashboard provides visualizations for:

* Jobs by platform
* Top companies
* Top locations

### 7. CSV Export

Users can download the filtered job listings as:

```text
jobs_data.csv
```

---

## 📊 Dashboard

The dashboard provides key metrics including:

* **Total Jobs**
* **Number of Companies**
* **Number of Locations**

It also provides visual charts for understanding the collected job-market data.

---

## 🔧 Installation

### Prerequisites

Make sure the following are installed:

* Python 3.x
* Google Chrome
* Chrome WebDriver
* Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/JobScope.git
```

### Step 2: Open the Project Folder

```bash
cd JobScope
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📦 Requirements

The project uses the following Python packages:

```text
selenium
pandas
beautifulsoup4
requests
streamlit
```

You can install them using:

```bash
pip install -r requirements.txt
```

---

## 📁 Main Modules

### `app.py`

The main Streamlit application.

It handles:

* User input
* Job search
* Filtering
* Dashboard metrics
* Job listings
* Charts
* CSV download

### `scraper/naukri_scraper.py`

Responsible for collecting job listings from Naukri using Selenium.

### `scraper/foundit_scraper.py`

Responsible for collecting job listings from Foundit using Selenium.

### `src/controller.py`

Controls the scraping process and combines the results from both job portals.

### `src/data_cleaning.py`

Performs basic data cleaning and duplicate removal.

### `src/analyzer.py`

Contains functionality for extracting commonly required skills from job-related information.

---

## 🎯 Project Objectives

The main objectives of JobScope are:

1. Automate the process of collecting job listings.
2. Reduce the time required to search multiple job portals.
3. Combine job information from different sources.
4. Clean and organize the collected job data.
5. Provide an easy-to-use dashboard for job analysis.
6. Allow users to download job information for further analysis.

---

## 🌟 Advantages

* Saves time when searching for jobs.
* Collects information from multiple job platforms.
* Provides centralized job information.
* Makes job-market data easier to analyze.
* Supports filtering and searching.
* Allows data export for further processing.

---

## ⚠️ Limitations

* Job portals may change their website structure or HTML selectors.
* Scraping performance depends on internet speed and website response time.
* Some salary information may not be available.
* Selenium requires a compatible browser/WebDriver setup.
* Job portal anti-bot mechanisms may affect scraping.
* The application depends on the current structure of the supported job websites.

---

## 🔮 Future Enhancements

Possible future improvements include:

* Add more job portals.
* Add advanced job filters.
* Add skill-based job recommendations.
* Add experience and salary filters.
* Add machine-learning-based job recommendations.
* Store historical job data in a database.
* Add automated scheduled scraping.
* Add advanced job-market analytics.
* Add email notifications for matching jobs.
* Improve scraper reliability against website changes.

---

## 🎓 OJT Project

**Project Name:** JobScope – Job Scraping & Market Analyzer

**Project Type:** On-the-Job Training (OJT) Project

**Domain:** Web Scraping, Data Analysis & Visualization

**Technologies:** Python, Selenium, Pandas, Streamlit

---

## 👨‍💻 Author

**Abhishek Ghatmal**

This project was developed as part of an OJT project to demonstrate practical knowledge of **Python programming, web scraping, data processing, and interactive dashboard development**.

---

## 📄 License

This project is created for educational and learning purposes.
