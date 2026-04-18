# 📈 Monitoramento do Modelo — Churn Prediction

## 🎯 Objetivo

Garantir que a API de predição de churn opere de forma confiável, eficiente e segura, permitindo:

- Detectar falhas rapidamente
- Monitorar desempenho da API
- Acompanhar qualidade dos dados de entrada
- Suportar decisões de manutenção e retraining do modelo

---

## 🧱 Arquitetura de Monitoramento

O monitoramento está implementado diretamente na API (FastAPI) através de:

- Logging estruturado
- Middleware de latência
- Monitoramento de erros
- Monitoramento de dados de entrada

---

## 📊 Métricas Monitoradas

### ⚡ Latência da API

Tempo de resposta de cada requisição:

POST /predict - 0.034s

Objetivo:
- Garantir respostas rápidas
- Identificar gargalos

---

### ❌ Taxa de erro

Erros são registrados automaticamente:

ERROR | Erro na predição: ...

Objetivo:
- Detectar falhas no modelo ou entrada inválida
- Monitorar estabilidade da API

---

### 📥 Dados de entrada

Os inputs são registrados:

INFO | Input recebido: {...}

Objetivo:
- Auditoria de requisições
- Identificação de padrões inesperados

---

### ⚠️ Detecção de anomalias

Exemplo implementado:

WARNING | Valor anômalo detectado em ContaMensal

Objetivo:
- Detectar valores fora do padrão
- Indicar possível data drift

---

## 🔁 Monitoramento do Modelo

### 📌 Status do modelo

Endpoint:

GET /health

Retorna:

{
  "status": "ok",
  "model_loaded": true
}

Objetivo:
- Verificar se o modelo está carregado corretamente

---

## 🧪 Testes de Monitoramento

O sistema é validado através de:

- Testes automatizados (pytest)
- Teste de latência básica
- Testes de endpoint (/health, /predict)

---

## 🚨 Estratégia de Alertas

(Conceitual — não automatizado nesta etapa)

Sugestões:

- Latência > 500ms → alerta
- Erros > 5% → alerta
- Inputs fora do padrão → alerta

---

## 🔁 Estratégia de Retreinamento

O modelo deve ser atualizado quando:

- Queda de performance observada
- Mudança significativa nos dados (data drift)
- Mudanças no comportamento dos clientes

Frequência sugerida:
- Mensal ou sob demanda

---

## 🛠️ Ferramentas Futuras

Para ambientes de produção, recomenda-se integrar:

- Prometheus
- Grafana
- MLflow Monitoring
- ELK Stack

---

## 🧠 Considerações Finais

O monitoramento implementado permite:

✔ Observabilidade básica do sistema  
✔ Identificação rápida de erros  
✔ Controle de desempenho da API  
✔ Base para evolução para MLOps completo  

---

## 🚀 Próximos Passos

- Adicionar coleta de métricas com Prometheus  
- Criar dashboards com Grafana  
- Implementar alertas automáticos  
- Monitorar drift de dados automaticamente  
