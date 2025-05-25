# 🚀 Crypto Transactions & Fee Analytics

Analyzed transaction trends, top assets, user activity, and platform fee structures using Python, Plotly, and Tableau.

---

## **Project Contents**

- `Senior Data Analyst Task Transactions.csv` – Dummy transaction data provided by Trust Wallet
- `cleaned_crypto_transactions.csv` – Cleaned, analysis-ready dataset  
- `crypto_transactions_profile.html` – Data profiling report  
- `trustWallet.ipynb` – Jupyter notebook (Python code, EDA, and graphs)  
- `Dashboard.twb` – Tableau workbook  
- `requirements.txt` – Python environment dependencies  
- `README.md` – Project documentation

---

## **1. Project Overview**

This project analyzes cryptocurrency transactions to identify key trends, outliers, asset and fee insights, and actionable recommendations for business growth and risk management.

---

## **2. How to Use This Project**

### **A. Python/Jupyter Analysis**
1. **Install dependencies:** 
```pip install -r requirements.txt```
2. **Open `trustWallet.ipynb`** in Jupyter Notebook or Jupyter Lab.
3. **Run all cells** to see:
   - Data cleaning steps
   - Automated profiling
   - Summary stats & KPIs
   - Visualizations (Plotly: time series, bar, histograms, correlation, outliers)
   - Advanced EDA (correlations, fee analysis, outlier detection)
4. **Outputs:**  
   - Interactive charts displayed in notebook  
   - Profiling report as `crypto_transactions_profile.html`  

### **B. Tableau Dashboard**

1. **Open `Dashboard.twb`** in Tableau Desktop or [Dashboard published on Tableau Public.](https://public.tableau.com/app/profile/meet.vaghasia6155/viz/Dashboard_17480963229760/Dashboard1)
2. **Explore the dashboards:**
   - Transaction volume over time
   - Top assets by value
   - Distribution and outliers
   - Fee metrics
   - KPI summary cards
   - Filter by platform, asset, status, type

## 3. **Key Insights**

   - Transaction volume is dominated by a few large-value trades.
   - Top crypto assets (e.g., Bitcoin, Ethereum, Solana) drive most of the activity.
   - Transaction fees show significant variation by asset and platform.
   - Outlier detection identifies high-value or potentially risky transactions.
   - User segmentation reveals a small number of “power users” responsible for large transaction volumes.

---

## **4. Recommendations**

- Optimize fee structures for high-value traders to remain competitive.
- Target loyalty programs to power users/wallets with high activity.
- Monitor and review outliers for compliance and risk.
- Promote top-performing assets, but keep an eye on emerging coins for early trends.

---

## **5. Deliverables**

- 📄 **Cleaned CSV dataset:** `cleaned_crypto_transactions.csv`
- 📊 **Jupyter notebook:** `trustWallet.ipynb`
- 📈 **Tableau dashboard:** `Dashboard.twb`
- 📋 **Profiling report:** `crypto_transactions_profile.html`
- 📚 **README documentation** (this file)

---

## **6. Advanced Features / Extra Effort**

- Full EDA including correlations and outlier detection using both boxplots and interactive scatter plots.
- Hover-enabled Plotly scatter plots display transaction details on outliers.
- Automated data profiling (using ydata-profiling).
- Tableau workbook with KPI cards and actionable filters.

---

## **7. How to Reproduce or Extend**

- Update `Senior Data Analyst Task Transactions.csv` with new data, rerun the notebook to refresh analysis and export a new dashboard.
- All scripts and steps are documented and modular for easy extension.

---

## **8. Notion**
- For more details, visit the [Notion page](https://www.notion.so/TrustWallet-Meet-Vaghasia-1fe8d53269d8804bb7f8e8b69a00c65b)



---
