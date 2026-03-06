# 📱 PhonePe Pulse Transaction Insights Dashboard

## 🧾 Project Overview

The **PhonePe Pulse Transaction Insights Dashboard** is a data analytics project designed to analyze India's digital payment ecosystem using the PhonePe Pulse dataset.

The project extracts raw JSON data from the PhonePe Pulse GitHub repository, processes the data using Python, stores it in a PostgreSQL database, and visualizes insights through an interactive Streamlit dashboard.

The dashboard enables users to explore transaction patterns, user growth, insurance activity, and regional performance across different states and districts of India.

---

# 🎯 Objectives

The main objectives of this project are:

• Analyze digital payment transaction trends in India
• Understand user engagement and platform adoption
• Identify high-performing states and districts
• Analyze insurance service adoption patterns
• Generate business insights for fintech strategy

---

# 🧠 Skills Demonstrated

This project demonstrates the following data analytics and engineering skills:

• Data Extraction (JSON processing)
• ETL Pipeline Development
• SQL Database Design
• Data Cleaning & Transformation
• Data Analysis using Pandas
• Interactive Data Visualization
• Streamlit Dashboard Development
• Business Insight Generation
• GitHub Project Documentation

---

# 🛠️ Technologies Used

| Technology   | Purpose                            |
| ------------ | ---------------------------------- |
| Python       | Data extraction and transformation |
| PostgreSQL   | Database storage                   |
| SQL          | Data querying                      |
| Pandas       | Data processing                    |
| Plotly       | Data visualization                 |
| Streamlit    | Dashboard interface                |
| Git & GitHub | Version control                    |

---

# 📂 Dataset

Data Source:
PhonePe Pulse GitHub Repository

Dataset includes multiple categories of digital payment data:

• Aggregated Transactions
• Aggregated Users
• Aggregated Insurance
• Map Level Transactions
• Map Level Users
• Map Level Insurance
• Top Performing Regions

The dataset contains information about:

• Transaction counts
• Transaction amounts
• User registrations
• App opens
• Insurance transactions
• State and district level data

---

# ⚙️ Project Architecture (ETL Pipeline)

The project follows a complete **ETL pipeline architecture**.

## 1️⃣ Extract

• Clone PhonePe Pulse GitHub repository
• Read raw JSON files from dataset directories

## 2️⃣ Transform

• Parse JSON data using Python
• Convert structured data into Pandas DataFrames
• Clean and organize dataset columns

## 3️⃣ Load

• Create PostgreSQL database tables
• Insert transformed data into SQL tables

---

# 🗄️ Database Schema

The project stores processed data in **9 SQL tables**.

## Aggregated Tables

These tables contain summarized data at the state level.

• aggregated_transaction
• aggregated_user
• aggregated_insurance

---

## Map Tables

These tables contain district-level information.

• map_transaction
• map_user
• map_insurance

---

## Top Tables

These tables contain top performing regions.

• top_transaction
• top_user
• top_insurance

---

# 📊 Dashboard Features

The Streamlit dashboard provides interactive analysis features.

### 🌍 Geographic Visualization

• State-wise transaction choropleth map
• Interactive map visualization

### 📈 Transaction Analytics

• Top performing states
• District-level transaction insights
• Pincode transaction analysis

### 👥 User Analytics

• User growth analysis
• App engagement tracking
• Registered user distribution

### 🛡️ Insurance Analytics

• Insurance transaction analysis
• Premium growth trends

### 📊 Interactive Filters

• Year filter
• Quarter filter
• Metric selection

---

# 💼 Business Case Studies

The dashboard includes five business-focused analytical case studies.

---

## 1️⃣ Transaction Dynamics Analysis

### Problem

Understand how digital payment transactions vary across regions and time.

### Analysis

• Top states by transaction value
• Transaction type distribution
• Yearly transaction growth
• Quarterly transaction trends
• Transaction count spread

### Business Value

Helps businesses identify:

• High transaction regions
• Popular payment categories
• Growth trends in digital payments

---

## 2️⃣ Device & User Dominance

### Problem

Understand user adoption and platform engagement.

### Analysis

• User type distribution
• User growth over time
• State-wise user base
• App open frequency
• User engagement ratio

### Business Value

Helps companies:

• Identify high engagement markets
• Track platform adoption
• Improve customer engagement strategy

---

## 3️⃣ Insurance Growth Analysis

### Problem

Analyze adoption of digital insurance services.

### Analysis

• State-wise insurance premium values
• Yearly insurance growth
• Quarterly insurance trends
• Policy count distribution
• Average premium analysis

### Business Value

Helps organizations:

• Identify insurance adoption regions
• Improve financial product strategies

---

## 4️⃣ Market Expansion Analysis

### Problem

Identify regions where digital payment services can expand.

### Analysis

• State transaction volume
• District transaction values
• Market growth trends
• Quarterly activity patterns
• Average transaction values

### Business Value

Helps fintech companies:

• Discover new market opportunities
• Understand district-level adoption

---

## 5️⃣ User Engagement Analysis

### Problem

Measure user interaction with the platform.

### Analysis

• Registered user distribution
• Application open frequency
• Engagement ratio
• Yearly engagement growth
• Quarterly activity trends

### Business Value

Helps companies:

• Improve user retention
• Optimize user experience

---

# 📈 Key Insights

From the analysis, several patterns were identified:

• Some states dominate digital payment adoption
• Transaction volume shows consistent yearly growth
• User engagement varies across regions
• Insurance transactions show emerging growth

---

# 📁 Project Structure

```
PhonePe_Pulse_Project
│
├── data_extraction.ipynb
├── database_creation.py
├── etl_process.py
├── app.py
├── requirements.txt
└── README.md
```

---

# ▶️ How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/PhonePe/pulse.git
```

---

### 2️⃣ Install Required Libraries

```bash
pip install pandas psycopg2 streamlit plotly sqlalchemy
```

---

### 3️⃣ Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

# 📊 Dashboard Preview

The dashboard provides:

• Interactive transaction maps
• Business case analysis
• Real-time data filtering
• Multiple visualization charts

---

# 🚀 Business Impact

The insights generated from this project can help fintech companies:

• Identify high-growth markets
• Improve digital payment adoption strategies
• Expand financial services like insurance
• Optimize marketing campaigns
• Enable data-driven decision making

---

# 🔮 Future Improvements

Possible enhancements for the project include:

• Real-time data integration
• Machine learning based prediction models
• Fraud detection analytics
• Advanced KPI dashboards
• Mobile responsive dashboard

---

# 👩‍💻 Author

Data Analytics Project

PhonePe Pulse Transaction Insights Dashboard
