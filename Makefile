# =========================
# VARIÁVEIS
# =========================

PYTHON=.env/bin/python
PIP=.env/bin/pip

# =========================
# INSTALAÇÃO
# =========================

install:
	pip install -r requirements.txt

# =========================
# TESTES
# =========================

test:
	pytest -v

# =========================
# LINT (QUALIDADE)
# =========================

lint:
	ruff check .

format:
	ruff check . --fix

# =========================
# RODAR API
# =========================

run:
	uvicorn src.api.app:app --reload

# =========================
# LIMPEZA
# =========================

clean:
	rm -rf __pycache__ .pytest_cache

# =========================
# PIPELINE COMPLETO
# =========================

all: lint test