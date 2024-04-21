#! Dockerfile

# https://www.debian.org/releases/bookworm/
# O Debian "bookworm" 12.5 foi lançado em 10 de Fevereiro de 2024

# baixar o diretorio do repositorio remoto para local: git clone https://github.com/RodrigoKartcheski/gcloud.git
# em variaveis (ENV) adequar os caminho porpostos para a realidade do local
# acesse o repositorio clonado
# ATENÇÃO: para executar o docker build deve-se estar no mesmo diretorio do arquivo Dockerfile - neste exemplo seria o diretorio "gcloud-cli-debian-12"
# ao acessar o conteiner estaremos no diretorio /app - para retornar a raiz e seguir para o diretorio sincronizado com o host digite <cd /> e observe o caminho definido no volume
# no volume abaixo o caminho do docker e do host estão definido para < cd /home/jobs/gcloud/gcloud-cli-debian-12/src>
# sudo chmod 777 -R /home/jobs/gcloud
# docker volume create gcloudvol
# docker build -t mgcloud:1.0 .
# docker run -it -v gcloudvol:/app/src -v /home/jobs/gcloud/gcloud-cli-debian-12/src:/home/jobs/gcloud/gcloud-cli-debian-12/src mgcloud:1.0 bash
# abaixo comandos opcionais - usar com cuidado
# cd /home/jobs/gcloud/gcloud-cli-debian-12/src
# docker run -it mgcloud:1.0 bash | opcional
# docker rm -f $(docker ps -aq)
# docker rmi -f $(docker images -q)
# docker volume prune
# gcloud version
# docker volume ls
# docker volume rm gcloudvol
# sudo ls /var/lib/docker/volumes
# https://www.youtube.com/watch?v=gU_3fW2VFPc&t=458s

FROM debian:bookworm

# Definir variáveis
ENV PATH_DIR_LOCAL="/home/jobs/gcloud/"
ENV PATH_REPO="https://github.com/RodrigoKartcheski/dataflow_repo.git"
ENV DIR_REPO="first_hello_word/hello_word"
ENV DIR_JOBS="/home/jobs/gcloud/first_hello_word/hello_word" 
ENV PROJECT_ID="learn-gcp-cloud-run"
ENV CLOUD_ZONE="us-central1"


# Definir o usuário e o diretório de trabalho padrão no container
WORKDIR /app

USER root

####
# Instalar as dependências necessárias
RUN apt-get update && apt-get -y install wget build-essential libssl-dev libffi-dev zlib1g-dev

# Instalar wget para baixar o Python
RUN apt-get install -y wget

# Baixar e instalar o Python 3.9
RUN wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz \
    && tar -xvf Python-3.9.7.tgz \
    && cd Python-3.9.7 \
    && ./configure --enable-optimizations \
    && make -j 8 \
    && make altinstall

# Verificar a versão do Python
RUN python3.9 --version

# Baixar o script get-pip.py
RUN wget https://bootstrap.pypa.io/get-pip.py

# Instalar o pip para Python 3.9
RUN python3.9 get-pip.py

# Verificar a versão do pip
RUN pip3.9 --version

# Limpar arquivos desnecessários
RUN rm -rf Python-3.9.7.tgz Python-3.9.7 get-pip.py

###
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src src

# Atualizar a lista de pacotes e instalar ferramentas básicas
RUN apt update -y && apt install -y curl wget gnupg

# Baixar e instalar a chave GPG do Google Cloud SDK
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor | tee /etc/apt/trustedsources.gpg > /dev/null

# Adicionar o repositório do Google Cloud SDK
RUN echo "deb [arch=amd64 signed-by=/etc/apt/trustedsources.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee /etc/apt/sources.list.d/google-cloud-sdk.list

# Atualizar a lista de pacotes novamente e instalar o gcloud
RUN apt update -y && apt install -y google-cloud-sdk

# Configurar o gcloud para uso não interativo
RUN echo "export GOOGLE_APPLICATION_DEFAULT_PROJECT=${PROJECT_ID}" >> ~/.bashrc \
    && echo "export CLOUD_SDK_COMPUTE_ZONE=${CLOUD_ZONE}" >> ~/.bashrc

    
# Instalar o Git
RUN apt-get update && apt-get install -y git

# Clonar o repositório e configurar o sparse-checkout
#RUN git clone --depth 1 --filter=blob:none --sparse ${PATH_REPO} \
#    && cd dataflow_repo \
#    && git sparse-checkout init --cone \
#    && git sparse-checkout set ${DIR_REPO}

# Instalar os editores de texto
RUN apt-get update && apt-get install -y nano vim vim-tiny

# (Opcional) Verificar a instalação
RUN nano --version && vim --version && vi --version

CMD ["bash"]
