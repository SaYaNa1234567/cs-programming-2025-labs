personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]

categorized = list(map(lambda p: {
    "name": p["name"],
    "clearance": p["clearance"],
    "category": "Top Secret" if p["clearance"] >= 4 else 
                "Confidential" if p["clearance"] >= 2 else 
                "Restricted"
}, personnel))
print(categorized)
