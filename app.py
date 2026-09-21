from flask import Flask, render_template

app = Flask(__name__)

roads = {
    "Main Road": 120,
    "Hospital Road": 35,
    "School Road": 90,
    "Market Road": 150,
    "Bus Station Road": 70,
    "Railway Road": 180
}

traffic_data = []

for road, vehicles in roads.items():

    if vehicles > 100:
        status = "HIGH CONGESTION"
    elif vehicles > 50:
        status = "MEDIUM CONGESTION"
    else:
        status = "LOW CONGESTION"

    traffic_data.append({
        "road": road,
        "vehicles": vehicles,
        "status": status
    })

@app.route("/")
def dashboard():
    return render_template("index.html", data=traffic_data)

if __name__ == "__main__":
    app.run(debug=True)