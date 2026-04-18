# 📊 Model Card — Churn Prediction

## 🎯 Objetivo
Prever churn de clientes para apoiar estratégias de retenção e maximizar lucro.

## 📦 Dataset
- Fonte: Telco Customer Churn
- ~7.000 amostras
- Variáveis: demográficas, serviços e faturamento
- Target: churn (0 = não, 1 = sim)

## ⚙️ Modelo
- Logistic Regression (Scikit-Learn)
- Pipeline: StandardScaler + modelo

## 📊 Performance
- Accuracy: 0.80
- F1-score: 0.59
- ROC-AUC: 0.84
- Lucro estimado: R$ 82.000

## ⚠️ Limitações
- Dataset relativamente pequeno
- Possível overfitting em padrões específicos
- Pode não generalizar para outras regiões ou empresas

## ⚖️ Viés
- Reflete distribuição original dos dados
- Grupos minoritários podem ter menor precisão

## 🚨 Cenários de falha
- Dados fora do padrão
- Mudanças no comportamento dos clientes
- Valores extremos ou inconsistentes

## 💰 Impacto de negócio
- Redução de churn
- Aumento de retenção
- Melhor direcionamento de campanhas

## 🔁 Manutenção
- Monitoramento contínuo
- Retreinamento periódico recomendado
