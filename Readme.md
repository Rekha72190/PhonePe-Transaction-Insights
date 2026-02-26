 🧾 Project Overview

The **PhonePe Transaction Insights** project analyzes digital payment transaction data to understand user engagement, payment trends, geographical performance, and insurance activity across India.

The project extracts raw JSON data from the PhonePe Pulse GitHub repository, transforms it using Python, stores it in PostgreSQL, and visualizes insights through an interactive Streamlit dashboard.

---

## 🎯 Objectives

* Analyze digital payment transaction behavior
* Visualize state and district level transaction performance
* Identify top-performing regions and categories
* Understand user engagement trends
* Generate business insights for strategic decisions

---

## 🧠 Skills Demonstrated

* Data Extraction (ETL Process)
* SQL Database Management
* Data Cleaning & Transformation
* Data Visualization
* Streamlit Dashboard Development
* Analytical Thinking
* Documentation

---

## 🛠️ Technologies Used

* Python
* PostgreSQL
* SQL
* Pandas
* Plotly
* Streamlit
* Git & GitHub

---

## 📂 Dataset

Data Source: PhonePe Pulse GitHub Repository

Contains:

* Aggregated Transactions
* User Data
* Insurance Data
* Map Level Insights
* Top Performing Regions

---

## ⚙️ Project Architecture (ETL Flow)

### 1️⃣ Extract

* Clone PhonePe Pulse repository using Python
* Read JSON files from dataset folders

### 2️⃣ Transform

* Convert JSON data into Pandas DataFrames
* Clean and structure columns

### 3️⃣ Load

* Create PostgreSQL database and tables using Python
* Insert processed data into SQL tables

---

## 🗄️ Database Tables

### Aggregated Tables

* aggregated_transaction
* aggregated_user
* aggregated_insurance

### Map Tables

* map_transaction
* map_user
* map_insurance

### Top Tables

* top_transaction
* top_user
* top_insurance

---

## 📊 Dashboard Features (Streamlit)

* State-wise transaction analysis
* District-level payment insights
* User engagement visualization
* Insurance performance tracking
* Interactive filters and charts

---

## 📈 Business Use Cases

* Customer Segmentation
* Fraud Detection Support
* Marketing Optimization
* Payment Category Analysis
* Geographic Trend Analysis
* Product Strategy Improvement

---

## 🔍 Key Insights

* Certain states dominate digital payment adoption
* User engagement grows consistently over time
* Insurance transactions show emerging growth patterns
* District-level analysis reveals regional payment behavior

---

## ▶️ How to Run the Project

### Clone Repository

```bash
git clone https://github.com/PhonePe/pulse.git
```

### Install Requirements

```bash
pip install pandas psycopg2 streamlit plotly
```

### Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
PhonePe_Project/
│
├── data_extraction.ipynb
├── database_creation.py
├── etl_process.py
├── app.py
├── requirements.txt
└── README.md
```

---

## ✅ Project Outcomes

* Built complete ETL pipeline
* Developed SQL analytical queries
* Created interactive business dashboard
* Generated actionable business insights

---

## 👩‍💻 Author

Data Science Project – PhonePe Transaction Insights

---

## ⭐ Future Improvements

* Real-time API integration
* Machine Learning prediction models
* Fraud detection system
* Advanced KPI dashboards

---
