#! Dockerfile

## baixar o diretorio do repositorio remoto para local: git clone https://github.com/RodrigoKartcheski/gcloud.git
# acesso ao console GCP: https://console.cloud.google.com/
# criar projeto: <learn-dataflow-420912>
# criar a conta de serviço: <dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com>
# criar a chave de serviço
# habilitar Dataflow API
# crie o bucket <hello-dataflow-bucket>
# em variaveis (ENV) adequar os caminho porpostos para a realidade do local
# acesse o repositorio clonado
# ATENÇÃO: para executar o docker build deve-se estar no mesmo diretorio do arquivo Dockerfile - neste exemplo seria o diretorio "gcloud-cli-debian-12"
# Python reconhece python3.9 main.py
# ao acessar o conteiner estaremos no diretorio /app - para retornar a raiz e seguir para o diretorio sincronizado com o host digite <cd /> e observe o caminho definido no volume
# no volume abaixo o caminho do docker e do host estão definido para < cd /home/jobs/gcloud/gcloud-cli-ubuntu-20/src>
# a pasta keys é reservada para colocar a chave json do Google, está vazia por que a chave é de uso confidencial
# sudo chmod 777 -R /home/jobs/gcloud
# docker volume create gcloud_ubuvol
# ir até a pasta do Dockerfile desejada <gcloud-cli-ubuntu-20>
# docker build -t mgcloud:1.0 .
# docker run -it -v gcloud_ubuvol:/app/src -v /home/jobs/gcloud/gcloud-cli-ubuntu-20/src:/home/jobs/gcloud/gcloud-cli-ubuntu-20/src mgcloud:1.0 bash
# abaixo comandos opcionais - usar com cuidado
# cd /home/jobs/gcloud/gcloud-cli-ubuntu-20/src
# cole a chave json do serviçe account no diretorio keys
# No arquivo config.py alterar as condições do projeto
# gcloud init
# excute o arquivo <python3 gcp_iam_management.py> ou os comandos abaixo
# gcloud projects add-iam-policy-binding learn-dataflow-420912 --member=user:rodrigo.kartcheski@gmail.com --role=roles/iam.serviceAccountUser
# gcloud projects add-iam-policy-binding learn-dataflow-420912 --member=serviceAccount:dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com --role=roles/dataflow.admin
# gcloud projects add-iam-policy-binding learn-dataflow-420912 --member="serviceAccount:dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com" --role=roles/iam.serviceAccountUser
# gcloud projects add-iam-policy-binding learn-dataflow-420912 --member="serviceAccount:dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com" --role=roles/storage.objectAdmin
# gcloud projects add-iam-policy-binding learn-dataflow-420912 --member="serviceAccount:dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com" --role=roles/storage.objectViewer
# opcional: gcloud projects add-iam-policy-binding learn-dataflow-420912 --member=serviceAccount:dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com --role=roles/storage.admin

# gcloud projects add-iam-policy-binding learn-dataflow-420912 --member=serviceAccount:dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com --role=roles/dataflow.worker
# gcloud projects add-iam-policy-binding learn-dataflow-420912 --member=serviceAccount:dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com --role=roles/storage.objectAdmin
# gcloud projects add-iam-policy-binding learn-dataflow-420912 --member=serviceAccount:dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com --role=roles/artifactregistry.reader
# roles/dataflow.worker
# roles/storage.objectAdmin
# roles/artifactregistry.reader

FROM ubuntu:20.04

USER root

# Definir variáveis
ENV PATH_DIR_LOCAL="/home/jobs/gcloud/"
ENV PATH_REPO="https://github.com/RodrigoKartcheski/dataflow_repo.git"
ENV DIR_REPO="first_hello_word/hello_word"
ENV DIR_JOBS="/home/jobs/gcloud/first_hello_word/hello_word" 
ENV PROJECT_ID="learn-gcp-cloud-run"
ENV CLOUD_ZONE="us-central1"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /app

# Atualizar lista de pacotes e instalar dependências
RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    libssl-dev \
    libffi-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncursesw5-dev \
    libgdbm-dev \
    libnss3-dev \
    liblzma-dev \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    xz-utils \
    libffi-dev \
    liblzma-dev \
    curl \
    git \
    nano \
    vim \
    vim-tiny

# Baixar e instalar Python 3.10
RUN wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz \
    && tar -xf Python-3.10.0.tgz \
    && cd Python-3.10.0 \
    && ./configure --enable-optimizations \
    && make -j$(nproc) \
    && make altinstall \
    && cd .. \
    && rm -rf Python-3.10.0 Python-3.10.0.tgz

# Definir Python 3.10 como padrão
RUN update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.10 1

# Verificar a versão do Python
RUN python3 --version

# Instalar o pip para Python 3.10
RUN wget https://bootstrap.pypa.io/get-pip.py \
    && python3.10 get-pip.py \
    && rm get-pip.py

# Instale as dependências do Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o conteúdo do diretório src para o diretório de trabalho no contêiner
COPY src/ src/

# Baixar e instalar a chave GPG do Google Cloud SDK
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor | tee /etc/apt/trustedsources.gpg > /dev/null

# Adicionar o repositório do Google Cloud SDK
RUN echo "deb [arch=amd64 signed-by=/etc/apt/trustedsources.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee /etc/apt/sources.list.d/google-cloud-sdk.list

# Atualizar a lista de pacotes novamente e instalar o gcloud
RUN apt update -y && apt install -y google-cloud-sdk

# Configurar o gcloud para uso não interativo
RUN echo "export GOOGLE_APPLICATION_DEFAULT_PROJECT=${PROJECT_ID}" >> ~/.bashrc \
    && echo "export CLOUD_SDK_COMPUTE_ZONE=${CLOUD_ZONE}" >> ~/.bashrc

CMD ["bash"]

