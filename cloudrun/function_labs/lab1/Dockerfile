# Dockerfile

# Usa uma imagem Python leve
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos para o contêiner
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8080 (usada pelo Cloud Functions)
ENV PORT=8080

# Comando para rodar a função
CMD ["functions-framework", "--target=home", "--port=8080"]
