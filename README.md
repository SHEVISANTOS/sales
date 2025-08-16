# 📦 Warehouse Sales Prediction App

A machine learning web application that predicts **warehouse sales** based on retail performance and time of year.  
Built with **Python**, **Random Forest**, and **Streamlit** for an interactive UI.

![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

## 🚀 Features
- ✅ Predicts warehouse sales using retail data
- 📊 Uses **Random Forest** for high accuracy
- 🖥️ Interactive web interface with **Streamlit**
- 📅 Time-based features (month, year) for seasonality

## 📂 Project Structure
\`\`\`
sales/
├── app.py                          # Streamlit web app
├── sales.ipynb                     # Training notebook
├── model/
│   ├── best_model_random_forest.pkl  # Saved ML model
│   └── scaler.pkl                    # StandardScaler
├── data/
│   └── Warehouse_and_Retail_Sales.csv  # Dataset
├── requirements.txt                # Python dependencies
├── .gitignore                      # Ignores virtual env
└── README.md                       # This file
\`\`\`

## 🖥️ How to Run Locally

1. **Clone the repo:**
   \`\`\`bash
   git clone https://github.com/your-username/sales.git
   cd sales
   \`\`\`

2. **Create virtual environment:**
   \`\`\`bash
   python -m venv sales_env
   source sales_env/bin/activate    # Linux/Mac
   # sales_env\Scripts\activate     # Windows
   \`\`\`

3. **Install dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Run the app:**
   \`\`\`bash
   streamlit run app.py
   \`\`\`

👉 Open your browser at: [http://localhost:8501](http://localhost:8501)

## 🧠 Model Info
- **Algorithm**: Random Forest Regressor
- **Target**: \`WAREHOUSE SALES\`
- **Key Features**: Retail Sales, Transfers, Month, Year
- **Performance**: R² ~34% (can improve with more data)

## 🛠️ Built With
- [Python](https://www.python.org/)
- [Scikit-learn](https://scikit-learn.org) – Machine Learning
- [Streamlit](https://streamlit.io) – Web App Framework
- [Pandas](https://pandas.pydata.org) – Data Processing

---

> 💡 **Note**: The \`.pkl\` files are included so the app works **out of the box** after cloning.
