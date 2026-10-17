"""Deterministic sample itineraries; no live bookings or price lookups."""

DESTINATIONS = {
    "Lisbon": [
        {"name": "Old-town walking loop", "interest": "culture", "cost": 12},
        {"name": "Riverside food market", "interest": "food", "cost": 28},
        {"name": "Ocean-view park", "interest": "nature", "cost": 8},
        {"name": "Tile museum", "interest": "culture", "cost": 15},
        {"name": "Neighborhood cafe crawl", "interest": "food", "cost": 24},
    ],
    "Kyoto": [
        {"name": "Temple garden visit", "interest": "culture", "cost": 18},
        {"name": "Canal-side stroll", "interest": "nature", "cost": 0},
        {"name": "Local noodle lunch", "interest": "food", "cost": 20},
        {"name": "Craft market browse", "interest": "culture", "cost": 10},
        {"name": "Forest trail walk", "interest": "nature", "cost": 6},
    ],
    "Vancouver": [
        {"name": "Seawall bike ride", "interest": "nature", "cost": 22},
        {"name": "Public market lunch", "interest": "food", "cost": 25},
        {"name": "City history walk", "interest": "culture", "cost": 10},
        {"name": "Harbor viewpoint", "interest": "nature", "cost": 0},
        {"name": "Local bakery stop", "interest": "food", "cost": 12},
    ],
}


def build_itinerary(destination, days, interests=()):
    if destination not in DESTINATIONS:
        raise ValueError("Choose a destination in the sample guide")
    if not 1 <= days <= 7:
        raise ValueError("days must be between 1 and 7")
    activities = DESTINATIONS[destination]
    interests = set(interests)
    preferred = [item for item in activities if not interests or item["interest"] in interests]
    pool = preferred or activities
    return [
        {"day": day + 1, **pool[day % len(pool)]}
        for day in range(days)
    ]


def estimate_total(itinerary, daily_food_allowance=35):
    if daily_food_allowance < 0:
        raise ValueError("daily_food_allowance cannot be negative")
    return sum(item["cost"] for item in itinerary) + len(itinerary) * daily_food_allowance
