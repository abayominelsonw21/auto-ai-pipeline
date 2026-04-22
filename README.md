# 🚗 AUTOMARKET AI
**Enterprise-Grade Vehicle Valuation Microservice**

### 📊 Model Performance
- **R-Squared Score:** 0.8295
- **Mean Absolute Error (MAE):** $4,722.82
- **Training Set:** 24,000+ validated records (Partitioned Carfax Data)

### 🛠 Tech Stack
- **AI/ML:** XGBoost (Native Categorical Support), Scikit-Learn
- **Data Engineering:** Pandas, Parquet, Regex-based ETL
- **Interface:** Streamlit (Stealth Monochrome Design)
- **DevOps:** Docker, Python 3.9

### 🚀 Key Features
- **Triple-Tier Cascading Logic:** Dynamic Make > Model > Body Style state management.
- **Artifact Decoupling:** Inference engine runs independently of the training pipeline via joblib persistence.
- **Robust Cleaning:** Automated handling of non-numerical "Premium" scraped data.
