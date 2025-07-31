# 🏋️ Calories Burnt Prediction Web App

A **Machine Learning web application** that predicts **calories burnt** during exercise based on user inputs such as **age, gender, height, weight, duration, heart rate, and body temperature**.  

The project leverages **XGBoost Regressor** for accurate calorie prediction and is deployed on **Render** with a **Flask + HTML frontend**.

---

## 🚀 Project Overview

- Collected and analyzed exercise data for calories burnt prediction.  
- Built and optimized an **XGBoost regression model**.  
- Conducted **Exploratory Data Analysis (EDA)** with feature plots and correlation heatmaps.  
- Improved the **Mean Absolute Error (MAE)** from **1.48 → 1.12** using **RandomizedSearchCV** for hyperparameter tuning.  
- Built a **Flask web app** where users can input their details and get **instant calorie predictions**.  
- Deployed on **Render** for public access.  

---

## 📊 Model Performance

| Model                  | MAE  |
|------------------------|------|
| XGBoost (Base)         | 1.48 |
| XGBoost (Tuned)        | 1.12 |

---

## 🖥️ Tech Stack

**Machine Learning:**  
- Python, NumPy, Pandas, Scikit-learn, XGBoost  

**Data Visualization:**  
- Matplotlib, Seaborn  

**Backend & Deployment:**  
- Flask  
- Gunicorn  
- Render (Cloud Hosting)  

---

## 🧩 Project Structure


---

## 📈 Exploratory Data Analysis (EDA)

The project includes:  
- **Distplots** of key features  
- **Feature correlation heatmap** to understand relationships  

**Example:**  

![EDA Heatmap](https://github.com/Prabhakar200216/calories-burnt/blob/main/heatmap.png)

---

## 🌐 Live Demo

🔗 **Web App:** [Render Live Link](https://calories-burnt-618i.onrender.com)  
🔗 **GitHub Repository:** [Project Repo](https://github.com/Prabhakar200216/calories-burnt)

---

## 🛠️ Installation & Usage (Local)

If you want to run the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/Prabhakar200216/calories-burnt
cd calorie-predictor

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run Flask app
python app.py
