import math
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Need to replace "*" for Prod with allowed domains
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Exit Ahead API is running"}

import math

def distance_miles(lat1, lng1, lat2, lng2):
    R = 3958.8
    d_lat = math.radians(lat2 - lat1)
    d_lng = math.radians(lng2 - lng1)
    a = math.sin(d_lat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lng / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

@app.get("/restaurants")
def get_restaurants(lat: float, lng: float):
    restaurants = [
        {"name": "Sunrise Biscuit Co.", "lat": 33.76, "lng": -84.39, "offer": "Free hash browns over $8"},
        {"name": "Peach pit Burgers", "lat": 33.74, "lng": -84.36, "offer": "2-for-1 fries after 2PM"},
        {"name": "Sunrise Biscuit Co.", "lat": 33.77, "lng": -84.41, "offer": "10% off banh mi"}
    ]

    for r in restaurants:
        r["dist"] = distance_miles(lat, lng, r["lat"], r["lng"])

    nearby = [r for r in restaurants if r["dist"] <= 2]
    nearby.sort(key=lambda r:["dist"])

    return nearby