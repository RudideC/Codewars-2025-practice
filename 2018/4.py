planets = {
    "Mercury": 88,
    "Venus": 225,
    "Earth": 365,
    "Mars": 687,
    "Jupiter": 4333,
    "Saturn": 10759,
    "Uranus": 30689,
    "Neptune": 60182    
}

print(f"{int((int(input())*planets[input()])/365)}")