#! Dockerfile

## baixar o diretorio do repositorio remoto para local: git clone https://github.com/RodrigoKartcheski/gcloud.git
# em variaveis (ENV) adequar os caminho porpostos para a realidade do local
# acesse o repositorio clonado
# ATENÇÃO: para executar o docker build deve-se estar no mesmo diretorio do arquivo Dockerfile - neste exemplo seria o diretorio "gcloud-cli-debian-12"
# Python reconhece python3.9 main.py
# ao acessar o conteiner estaremos no diretorio /app - para retornar a raiz e seguir para o diretorio sincronizado com o host digite <cd /> e observe o caminho definido no volume
# no volume abaixo o caminho do docker e do host estão definido para < cd /home/jobs/gcloud/gcloud-cli-ubuntu-20/src>
# a pasta keys é reservada para colocar a chave json do Google, está vazia por que a chave é de uso confidencial
# sudo chmod 777 -R /home/jobs/gcloud
# docker volume create gcloud_ubuvol
# docker build -t mgcloud:1.0 .
# docker run -it -v gcloud_ubuvol:/app/src -v /home/jobs/gcloud/gcloud-cli-ubuntu-20/src:/home/jobs/gcloud/gcloud-cli-ubuntu-20/src mgcloud:1.0 bash
# abaixo comandos opcionais - usar com cuidado
# cd /home/jobs/gcloud/gcloud-cli-ubuntu-20/src


FROM ubuntu:20.04


WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip

# Copie o conteúdo do diretório src para o diretório de trabalho no contêiner
COPY src/ src/

# Instale as dependências do Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt




CMD ["bash"]
