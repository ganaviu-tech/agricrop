# 🌱 AgriCrop – Soil Health Analyzer

AgriCrop is a simple AI-powered soil analysis web application that helps farmers determine soil health and fertilizer recommendations for different crops.

The system analyzes soil nutrients and provides:

* Soil health status
* Critical nutrient deficiencies
* Fertilizer recommendations
* Crop suitability score
* AI explanation of soil condition

---

## 🚀 Features

✅ Manual soil entry (N, P, K, pH)
✅ Bulk soil dataset upload (CSV)
✅ AI explanation for soil results
✅ Fertilizer recommendation system
✅ Crop-specific soil analysis

Supported crops:

* 🍅 Tomato
* 🌾 Wheat
* 🌾 Rice
* 🌽 Maize

---

## 🧠 How It Works

The system calculates an **AgriPulse Score** based on soil nutrients:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Soil pH

Based on nutrient thresholds, the system determines:

* Soil health level
* Nutrient deficiencies
* Recommended fertilizers

---

## 📂 Project Structure

```
agricrop
│
├── app.py
├── agripulse_logic.py
├── processor.py
├── requirements.txt
│
└── templates
    ├── index.html
    └── results.html
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/agricrop.git
```

Move into the project folder:

```
cd agricrop
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

---

## 🌐 Deployment

The application can be deployed easily on:

* Render
* Replit
* Railway
* Python hosting platforms

---

## 📊 CSV Format for Bulk Upload

Example dataset format:

```
soil_id,nitrogen,phosphorus,potassium,ph_level
S1,22,18,210,6.5
S2,15,10,120,5.8
S3,35,28,250,6.8
```

---

## 👨‍💻 Technologies Used

* Python
* Flask
* Pandas
* HTML / CSS
* Gunicorn

---

## 🌍 Goal

The goal of AgriCrop is to support **sustainable farming** by helping farmers make better fertilizer and crop decisions using soil data.

---

## 📜 License

This project is open source and free to use for educational purposes.
