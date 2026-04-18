# 🏗️ Arquitetura de Deploy — Churn Prediction

## 🎯 Objetivo
Descrever como o modelo é servido em produção.

---

## 🔹 Tipo de Deploy

API REST com FastAPI

---

## 🔄 Fluxo de Execução

Cliente → API (/predict) → Modelo MLflow → Resposta

---

## 🧱 Componentes

- FastAPI → interface HTTP
- MLflow → gerenciamento de modelo
- Scikit-learn → inferência
- Pandas → transformação de dados

---

## ⚡ Justificativa

- Baixa latência
- Simplicidade de implementação
- Fácil integração com outros sistemas

---

## 🔁 Tipo de Processamento

✔ Real-time (online)

Motivo:
- Necessidade de decisão imediata sobre churn

---

## 🛠️ Possível Evolução

- Dockerização da API
- Deploy em cloud (AWS, GCP)
- Monitoramento com Prometheus/Grafana
- CI/CD com GitHub Actions

---

## 📈 Escalabilidade

- Pode ser escalado horizontalmente (múltiplas instâncias da API)
- Balanceamento de carga possível

---

## 🧠 Considerações

Arquitetura simples, porém suficiente para:

✔ aplicações reais  
✔ prototipagem rápida  
✔ base para sistemas MLOps mais complexos  
