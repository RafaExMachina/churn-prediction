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

O projeto foi refatorado seguindo boas práticas de engenharia de software.


---

## 🌐 API de Inferência (FastAPI)

Foi desenvolvida uma API REST para servir o modelo treinado.

### 🔗 Endpoints

- `GET /` → status da API  
- `GET /health` → verificação de saúde + modelo carregado  
- `POST /predict` → predição de churn  

---

## 📥 Exemplo de requisição

```json
{
  "Conjuge": 1,
  "Dependentes": 0,
  "TelefoneFixo": 0,
  "PagamentoOnline": 1,
  "Maior65Anos": 0,
  "MesesDeContrato": 1,
  "ContaMensal": 29.85, ...
}
```
---

## 📤 Resposta

```json
{
  "prediction": 0
}
```

---

## 🤖 Integração com MLflow

O modelo é carregado diretamente do MLflow:

- Garantia de versionamento
- Reprodutibilidade
- Deploy desacoplado do treino

---

## 🧪 Testes Automatizados (Pytest)

Foram implementados testes para garantir a confiabilidade do sistema:

- Teste de saúde da API (/health)
- Teste de predição (/predict)
- Teste de formato de entrada (pipeline)
- Teste básico (sanidade)
- Teste de latência da API

---

## ▶️ Executar testes

```bash 
pytest -v
```

---

## 📈 Logging

A API possui logging estruturado para:

- Monitoramento de requisições
- Debug de erros
- Observabilidade do sistema

--- 

## ⚡ Execução da API
```
uvicorn src.api.app:app --reload
```
Acesse a documentação interativa:
 
👉 http://127.0.0.1:8000/docs

---

## Conclusão

O projeto evoluiu de um modelo de Machine Learning para um sistema completo de predição em produção, incluindo:

✔ Pipeline reprodutível

✔ Modelos versionados

✔ API de inferência

✔ Testes automatizados

✔ Arquitetura modular

