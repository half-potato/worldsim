"""
Format:
Activity
Description
Resources Gained (prob) (can be modified by environment)
Resources Used (prob) (can be modified by environment)
Time (in minutes)
Location (environment)
"""

activities = {
    "smith-armor": {
        "desc": "Create armor",
        "time": 60*3,
        "resource-used": {"iron bar": 3},
        "resource-gained": {"armor": 0.50},
        "location": "smith"
    }
}
