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

## 🤖 Modelo de Rede Neural (MLP)

Foi implementada uma rede neural do tipo **Multilayer Perceptron (MLP)** utilizando PyTorch:

- Arquitetura:
  - Camadas densas (64 → 32 → 1)
  - Função de ativação: ReLU
  - Saída com Sigmoid
- Treinamento:
  - Loss: Binary Cross Entropy
  - Otimizador: Adam
  - Early stopping aplicado

### 📉 Resultado

O modelo MLP apresentou desempenho **ligeiramente inferior à Regressão Logística**, tanto em métricas quanto em lucro.

### 📌 Análise

- O dataset é **tabular e relativamente pequeno**
- Modelos lineares e baseados em árvore tendem a performar melhor nesse cenário
- A rede neural não trouxe ganho significativo, aumentando a complexidade sem benefício claro

👉 **Conclusão:** nem sempre modelos mais complexos são melhores.

---

## ⚙️ Pipeline

- StandardScaler  
- One-hot encoding  
- Train/test split estratificado  
- Pipeline Scikit-Learn  

---

## 🔬 Modelos Avaliados

- DummyClassifier  
- Logistic Regression  
- Random Forest  
- XGBoost  
- MLP (PyTorch)  

---

## 🧪 Métricas

- Accuracy  
- F1-score  
- ROC-AUC  
- PR-AUC  
- Lucro de negócio  

---

## 📊 MLflow

Todos os experimentos foram rastreados com MLflow:

- Registro de métricas e parâmetros  
- Versionamento de modelos  
- Model Registry utilizado  

Modelos registrados:
- churn_logreg  
- churn_rf  
- churn_xgb  
- churn_mlp_model  

---

## 🔁 Reprodutibilidade

- random_state=42  
- Pipeline padronizado  
- Dataset versionado em `/data/processed`  
- MLflow tracking  

---

# 🚀 Etapa 3 — Engenharia de Software e API

## 🏗️ Arquitetura do Projeto

src/

├── api/          
├── data/         
├── features/     
├── models/       
├── pipeline/     
└── utils/        

---

## 🌐 API de Inferência (FastAPI)

- GET /  
- GET /health  
- POST /predict  

---

## 🧪 Testes Automatizados (Pytest)

- Teste de saúde  
- Teste de predição  
- Teste de pipeline  
- Teste de latência  

---

## 📈 Logging

- Monitoramento de requisições  
- Debug de erros  

---

# 🚀 Etapa 4 — Documentação e Entrega Final

## 📄 Model Card

Documentação completa do modelo incluindo:

- Performance  
- Limitações  
- Vieses  
- Cenários de falha  

📁 docs/model_card.md

---

## 🏗️ Arquitetura de Deploy

Cliente → API FastAPI → Modelo MLflow → Predição  

📁 docs/architecture.md

---

## 📊 Monitoramento

- Logging estruturado  
- Medição de latência  
- Observabilidade  

📁 docs/monitoring.md

---

## 🐳 Docker

```bash
docker-compose up --build
```

Acesse: http://localhost:8000/docs

---

## 🎬 Conclusão Final

✔ Pipeline ML completo  
✔ API de produção  
✔ Testes automatizados  
✔ Monitoramento  
✔ Docker  
✔ Documentação profissional  

