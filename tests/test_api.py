from fastapi.testclient import TestClient
from src.api.app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    
    data = response.json()
    
    assert data["status"] == "ok"
    assert "model_loaded" in data



def test_predict():
    sample = {
        "Conjuge": 1,
        "Dependentes": 0,
        "TelefoneFixo": 0,
        "PagamentoOnline": 1,
        "Maior65Anos": 0,
        "MesesDeContrato": 1,
        "ContaMensal": 24.8,

        "VariasLinhasTelefonicas_Nao": False,
        "VariasLinhasTelefonicas_SemServicoTelefonico": True,
        "VariasLinhasTelefonicas_Sim": False,

        "ServicoDeInternet_DSL": True,
        "ServicoDeInternet_FibraOptica": False,
        "ServicoDeInternet_Nao": False,

        "SegurancaOnline_Nao": True,
        "SegurancaOnline_SemServicoDeInternet": False,
        "SegurancaOnline_Sim": False,

        "BackupOnline_Nao": True,
        "BackupOnline_SemServicoDeInternet": False,
        "BackupOnline_Sim": False,

        "SeguroNoDispositivo_Nao": True,
        "SeguroNoDispositivo_SemServicoDeInternet": False,
        "SeguroNoDispositivo_Sim": False,

        "SuporteTecnico_Nao": True,
        "SuporteTecnico_SemServicoDeInternet": False,
        "SuporteTecnico_Sim": False,

        "TVaCabo_Nao": True,
        "TVaCabo_SemServicoDeInternet": False,
        "TVaCabo_Sim": False,

        "StreamingDeFilmes_Nao": True,
        "StreamingDeFilmes_SemServicoDeInternet": False,
        "StreamingDeFilmes_Sim": False,

        "TipoDeContrato_DoisAnos": False,
        "TipoDeContrato_Mensalmente": True,
        "TipoDeContrato_UmAno": False,

        "FormaDePagamento_CartaoDeCredito": False,
        "FormaDePagamento_ChequeDigital": True,
        "FormaDePagamento_ChequePapel": False,
        "FormaDePagamento_DebitoEmConta": False
    }

    response = client.post("/predict", json=sample)

    assert response.status_code == 200
    assert "prediction" in response.json()

def test_api_response_time():
    response = client.get("/health")
    assert response.status_code == 200    