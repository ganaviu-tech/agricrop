import os
from flask import Flask, render_template, request
import processor
from agripulse_logic import calculate_agripulse_score

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/upload_csv", methods=["POST"])
def upload_csv():

    crop = request.form.get("crop")
    file = request.files.get("file")

    if not file:
        return "No file uploaded"

    results = processor.process_csv(file, crop)

    return render_template("results.html", results=results)


@app.route("/analyze_manual", methods=["POST"])
def analyze_manual():

    crop = request.form.get("crop")

    n = float(request.form.get("N"))
    p = float(request.form.get("P"))
    k = float(request.form.get("K"))
    ph = float(request.form.get("pH"))

    score, health, deficiencies, fertilizer = calculate_agripulse_score(crop, n, p, k, ph)

    results = [{
        "soil_id": "MANUAL_ENTRY",
        "target_crop": crop,
        "health_metrics": {
            "overall_health": health,
            "critical_deficiencies": deficiencies
        },
        "recommendation": {
            "fertilizer_plan": fertilizer,
            "suitability_score": score
        },
        "ai_explanation": f"Soil analysis completed. The soil health for {crop} is {health}. Apply recommended fertilizers to improve yield."
    }]

    return render_template("results.html", results=results)


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)