import numpy as np
import pandas as pd
import mlflow.pyfunc
import logging
import time

from fastapi import FastAPI, Request
from pydantic import BaseModel

# =========================
# LOGGING CONFIG
# =========================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# =========================
# INICIALIZAÇÃO
# =========================

app = FastAPI(title="Churn Prediction API")

# =========================
# MIDDLEWARE (LATÊNCIA)
# =========================

@app.middleware("http")
async def log_latency(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time

    logger.info(f"{request.method} {request.url.path} - {duration:.4f}s")

    return response

# =========================
# CAMINHO DO MODELO
# =========================

MODEL_PATH = "/home/rafa_exmaquina/Documentos/churn-prediction/notebooks/mlruns/2/models/m-18cc7ef2b03944359d34d0c1edeaa308/artifacts"

model = None

try:
    model = mlflow.pyfunc.load_model(MODEL_PATH)
    logger.info("✅ Modelo carregado com sucesso")
except Exception as e:
    logger.error(f"❌ Erro ao carregar modelo: {e}")

# =========================
# SCHEMA (ENTRADA)
# =========================

class InputData(BaseModel):
    Conjuge: int
    Dependentes: int
    TelefoneFixo: int
    PagamentoOnline: int
    Maior65Anos: int
    MesesDeContrato: float
    ContaMensal: float
    VariasLinhasTelefonicas_Nao: bool
    VariasLinhasTelefonicas_SemServicoTelefonico: bool
    VariasLinhasTelefonicas_Sim: bool
    ServicoDeInternet_DSL: bool
    ServicoDeInternet_FibraOptica: bool
    ServicoDeInternet_Nao: bool
    SegurancaOnline_Nao: bool
    SegurancaOnline_SemServicoDeInternet: bool
    SegurancaOnline_Sim: bool
    BackupOnline_Nao: bool
    BackupOnline_SemServicoDeInternet: bool
    BackupOnline_Sim: bool
    SeguroNoDispositivo_Nao: bool
    SeguroNoDispositivo_SemServicoDeInternet: bool
    SeguroNoDispositivo_Sim: bool
    SuporteTecnico_Nao: bool
    SuporteTecnico_SemServicoDeInternet: bool
    SuporteTecnico_Sim: bool
    TVaCabo_Nao: bool
    TVaCabo_SemServicoDeInternet: bool
    TVaCabo_Sim: bool
    StreamingDeFilmes_Nao: bool
    StreamingDeFilmes_SemServicoDeInternet: bool
    StreamingDeFilmes_Sim: bool
    TipoDeContrato_DoisAnos: bool
    TipoDeContrato_Mensalmente: bool
    TipoDeContrato_UmAno: bool
    FormaDePagamento_CartaoDeCredito: bool
    FormaDePagamento_ChequeDigital: bool
    FormaDePagamento_ChequePapel: bool
    FormaDePagamento_DebitoEmConta: bool

# =========================
# ROOT
# =========================

@app.get("/")
def root():
    logger.info("Endpoint / acessado")
    return {"msg": "API funcionando 🚀"}

# =========================
# HEALTH CHECK
# =========================

@app.get("/health")
def health():
    logger.info("Health check chamado")
    return {
        "status": "ok",
        "model_loaded": model is not None
    }

# =========================
# PREDICT
# =========================

@app.post("/predict")
def predict(data: InputData):

    logger.info("Requisição de predição recebida")

    if model is None:
        logger.error("Modelo não carregado")
        return {"error": "Modelo não carregado"}

    try:
        X = pd.DataFrame([data.model_dump()])
        pred = model.predict(X)[0]

        logger.info(f"Predição realizada com sucesso: {pred}")

        return {"prediction": int(pred)}

    except Exception as e:
        logger.error(f"Erro na predição: {e}")
        return {"error": str(e)}