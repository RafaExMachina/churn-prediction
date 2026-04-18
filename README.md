# 📊 Churn Prediction — Tech Challenge

## 🎯 Objetivo
Desenvolver um modelo de Machine Learning para prever churn de clientes, considerando impacto financeiro e tomada de decisão de negócio.

---

## 🧠 Problema de Negócio
- Custo churn: R$ 500  
- Custo retenção: R$ 100  
- Lucro por cliente retido: R$ 400  

---

## 📁 Dataset
- Fonte: Telco Customer Churn  
- Amostras: ~7.000  
- Variáveis: demográficas, serviços contratados e faturamento  
- Target: churn (0 = não, 1 = sim)

---

## 💰 Função de Custo

- Verdadeiro Positivo (TP): +R$400  
- Falso Positivo (FP): -R$100  
- Falso Negativo (FN): -R$500  
- Verdadeiro Negativo (TN): R$0  

**Lucro = TP × 400 - FP × 100 - FN × 500**

---

## 📊 Resultados dos Modelos

| Modelo | Accuracy | F1-score | ROC-AUC | PR-AUC | Lucro (R$) |
|--------|---------|---------|---------|--------|------------|
| Logistic Regression | **0.80** | **0.59** | **0.84** | **0.63** | **82.000** |
| XGBoost | 0.79 | 0.57 | 0.83 | 0.63 | 79.200 |
| Random Forest | 0.78 | 0.55 | 0.81 | 0.60 | 75.600 |
| MLP (PyTorch) | 0.79 | 0.56 | 0.83 | 0.61 | 80.600 |
| Dummy Baseline | 0.73 | 0.00 | 0.50 | 0.27 | 0 |

---

## 🏆 Melhor Modelo
**Logistic Regression**

- Melhor equilíbrio entre precisão e recall  
- Maior lucro financeiro  
- Maior ROC-AUC  
- Modelo simples, interpretável e robusto  

---

## 🚀 Etapa 4 — Documentação e Entrega Final

## 📄 Model Card
Documentação completa do modelo: desempenho, limitações, vieses e cenários de falha.  
Arquivo: docs/model_card.md

## 🏗️ Arquitetura de Deploy
Cliente → API FastAPI → Modelo MLflow → Predição  
Arquivo: docs/architecture.md

## 📊 Monitoramento da API
- Logging estruturado
- Medição de latência
- Registro de erros

Arquivo: docs/monitoring.md

## 🐳 Containerização

```bash
docker-compose up --build
```

Acesse: http://localhost:8000/docs

---

## 🎬 Conclusão Final

✔ Pipeline completo de ML  
✔ API pronta para produção  
✔ Testes automatizados  
✔ Monitoramento  
✔ Docker  
✔ Documentação profissional  
