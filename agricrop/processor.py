import pandas as pd
from agripulse_logic import calculate_agripulse_score


def generate_ai_explanation(crop, deficiencies):

    if not deficiencies:
        return f"The soil nutrients are balanced and suitable for growing {crop.lower()}."

    nutrients = ", ".join(deficiencies)

    return f"The soil is lacking {nutrients}. Adding the recommended fertilizer will help the {crop.lower()} crop grow healthier and increase yield."


def process_csv(file, crop):

    df = pd.read_csv(file)

    results = []

    for _, row in df.iterrows():

        score, health, deficiencies, fertilizer_plan = calculate_agripulse_score(
            crop,
            row["nitrogen"],
            row["phosphorus"],
            row["potassium"],
            row["ph_level"]
        )

        result = {
            "soil_id": str(row["soil_id"]),
            "target_crop": crop,
            "health_metrics": {
                "overall_health": health,
                "critical_deficiencies": deficiencies
            },
            "recommendation": {
                "fertilizer_plan": fertilizer_plan,
                "suitability_score": float(score)
            },
            "ai_explanation": generate_ai_explanation(crop, deficiencies)
        }

        results.append(result)

    return results