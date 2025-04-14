class EvaAgent:
    def __init__(self):
        print("[EvaAgent] Initialized")

    def run(self, opportunities):
        print(f"[EvaAgent] Received {len(opportunities)} opportunities")
        for i, opp in enumerate(opportunities[:3]):  # Just previewing the first 3 for now
            print(f"Opportunity #{i+1}: {opp.get('title', 'No Title')}")
