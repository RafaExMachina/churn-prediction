# =========================
# Imagem base
# =========================
FROM python:3.12-slim

# =========================
# Diretório de trabalho
# =========================
WORKDIR /app

# =========================
# Copiar arquivos
# =========================
COPY requirements.txt .

# =========================
# Instalar dependências
# =========================
RUN pip install --no-cache-dir -r requirements.txt

# =========================
# Copiar projeto
# =========================
COPY . .

# =========================
# Porta
# =========================
EXPOSE 8000

# =========================
# Comando de execução
# =========================
CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]