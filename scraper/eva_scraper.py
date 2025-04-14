from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

EVA_URL = "https://mvendor.cgieva.com/Vendor/public/AllOpportunities.jsp"

def fetch_opportunities(limit=5):
    # Set Chrome options for headless mode (can remove headless for debugging)
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    # Path to your chromedriver.exe
    driver_path = os.path.join(os.getcwd(), "chromedriver.exe")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    print("🌐 Opening browser to eVA site...")
    driver.get(EVA_URL)

    # Wait for JS to render (you can tune this later with WebDriverWait)
    time.sleep(5)

    print("✅ Page loaded, parsing...")

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # Look for all opportunity cards
    cards = soup.find_all("div", class_="card-body")
    opportunities = []

    for card in cards:
        title_el = card.find("div", class_="card-title")
        desc_el = card.find("div", class_="card-text")
        if not title_el or not desc_el:
            continue

        opp_id_el = card.find_previous_sibling("div")
        opp = {
            "id": opp_id_el.get_text(strip=True) if opp_id_el else "Unknown",
            "title": title_el.get_text(strip=True),
            "description": desc_el.get_text(strip=True),
        }
        opportunities.append(opp)

        if len(opportunities) >= limit:
            break

    return opportunities

# For test run
if __name__ == "__main__":
    from pprint import pprint
    pprint(fetch_opportunities())
