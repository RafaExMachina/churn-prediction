# 📊 Churn Prediction — Tech Challenge

## 🎯 Objetivo
Desenvolver um modelo de Machine Learning para prever churn de clientes, considerando também impacto financeiro.

---

## 🧠 Problema de Negócio
- Custo churn: R$ 500  
- Custo retenção: R$ 100  
- Lucro por cliente: R$ 400  

---

## 📊 Resultados dos Modelos

| Modelo | Accuracy | F1-score | ROC-AUC | PR-AUC | Lucro (R$) |
|--------|---------|---------|---------|--------|------------|
| Logistic Regression | **0.80** | **0.59** | **0.84** | **0.63** | **82.000** |
| XGBoost | 0.79 | 0.57 | 0.83 | 0.63 | 79.200 |
| Random Forest | 0.78 | 0.55 | 0.81 | 0.60 | 75.600 |
| Dummy Baseline | 0.73 | 0.00 | 0.50 | 0.27 | 0 |

---

## 🏆 Melhor Modelo
**Logistic Regression**
- Melhor equilíbrio geral
- Maior lucro
- Melhor ROC-AUC

---

## ⚙️ Pipeline
- StandardScaler
- One-hot encoding
- Train/test split estratificado
- Pipeline Scikit-Learn

---

## 🔬 Modelos
- DummyClassifier
- Logistic Regression
- Random Forest
- XGBoost

---

## 🧪 Métricas
- Accuracy
- F1-score
- ROC-AUC
- PR-AUC
- Business Profit

---

## 🔁 Reprodutibilidade
- random_state=42
- MLflow tracking
- Dataset versionado

---

## 🚀 Execução
```bash
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/EDA.ipynb
```

---

## 🎥 STAR

**Situation:** Prever churn  
**Task:** Criar pipeline ML  
**Action:** EDA + modelos + MLflow  
**Result:** 80% accuracy + R$82k lucro  

---

## 🏁 Conclusão
- Modelo simples venceu
- Métrica de negócio foi decisiva
- Projeto pronto para produção

---

## 📌 Próximos Passos
- SMOTE
- Feature engineering
- Deploy FastAPI
