# Dockerfile

# Usa uma imagem Python leve
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos para o contêiner
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8080 (necessário para o Cloud Run)
EXPOSE 8080

# Define a variável de ambiente para o Flask rodar na porta correta
ENV PORT=8080

# Comando para rodar a aplicação
CMD ["python", "main.py"]
