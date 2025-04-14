from scraper.eva_scraper import fetch_opportunities
from pprint import pprint

def main():
    print("🔍 Fetching latest eVA opportunities...\n")
    opportunities = fetch_opportunities(limit=5)
    
    for i, opp in enumerate(opportunities, 1):
        print(f"🧾 Opportunity #{i}")
        print(f"ID: {opp['id']}")
        print(f"Title: {opp['title']}")
        print(f"Description: {opp['description']}\n")
        print("-" * 50)

if __name__ == "__main__":
    main()
