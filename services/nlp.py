from typing import Optional

# Define keywords for each category
CATEGORY_KEYWORDS = {
    "Plumbing": ["leak", "pipe", "clog", "faucet", "toilet", "drain"],
    "Electrical": ["electric", "wiring", "outlet", "breaker", "light", "power"],
    "HVAC": ["ac", "air conditioner", "heater", "hvac", "cooling", "heating"],
    "Pest Control": ["rat", "mouse", "insect", "roach", "bug", "pest"],
    "House Cleaning": ["clean", "maid", "sweep", "vacuum", "dust"],
    "Lawn Care": ["mow", "grass", "lawn", "snow", "yard"],
    "Appliance Installation": ["appliance", "install", "washer", "dryer", "stove"],
    "Painting": ["paint", "roller", "wall", "color"],
}

def classify_service(description: str) -> Optional[str]:
    """
    Classify the service category based on keywords found in the description.
    Returns the matched category or None if no match found.
    """
    description = description.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in description for keyword in keywords):
            return category
    return None
