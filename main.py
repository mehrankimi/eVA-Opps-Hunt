from dotenv import load_dotenv # type: ignore
import os

from scraper.eva_scraper import EvaScraper
from agent.agent import EvaAgent
from agent.filter_agent import filter_opportunities  # Optional

# Load environment variables
load_dotenv()

# Initialize scraper
scraper = EvaScraper()
opps = scraper.parse_dump_file("data/page_dump.html")

# Optional: filter results
filtered_opps = filter_opportunities(opps)

# Run the AI Agent
agent = EvaAgent()
agent.run(filtered_opps)
