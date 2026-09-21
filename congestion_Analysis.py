roads = {
    "Main Road": 120,
    "Hospital Road": 35,
    "School Road": 90,
    "Market Road": 150,
    "Bus Station Road": 70,
    "Railway Road": 180
}

print("\nSMART CITY TRAFFIC CONGESTION ANALYSIS")
print("=" * 50)

high_count = 0
medium_count = 0
low_count = 0

for road, vehicles in roads.items():

    if vehicles > 100:
        status = "HIGH CONGESTION"
        high_count += 1

    elif vehicles > 50:
        status = "MEDIUM CONGESTION"
        medium_count += 1

    else:
        status = "LOW CONGESTION"
        low_count += 1

    print(f"{road:20} {vehicles:3} Vehicles --> {status}")

print("\nSUMMARY")
print("=" * 50)
print("High Congestion Roads   :", high_count)
print("Medium Congestion Roads :", medium_count)
print("Low Congestion Roads    :", low_count)