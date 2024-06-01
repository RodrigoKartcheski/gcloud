# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

############################################################################
# checar as permissões: service account, permissões
# checar a rede e subnet (vcp)

# criar o diretorio "project"
# criar o arquivo Setup.py
# Criar o arquivo config.py com os parametros necessarios para passar para main.
# criar o arquivo main.py com os codigos necessarios
# Criar os templates (scripts python)
# criar o arquivo Dockerfile
# Criar o arquivo Requeriments.txt

# Rodar os comandos abaixo para criar o repositorio e fazer o build
# gcloud artifacts repositories create repo-dataflow --repository-format=docker --location=us-east4 --async --project=learn-dataflow-420912
# gcloud auth configure-docker us-east4-docker.pkg.dev
# gcloud builds submit --tag us-east4-docker.pkg.dev/learn-dataflow-420912/repo-dataflow/dataflex-dev:latest .
# Comando para rodar o job no Dataflow
# gcloud dataflow flex-template run "getting-started-`date +%Y%m%d-%H%M%S`" --template-file-gcs-location "gs://hello-dataflow-bucket/templates/getting_started-java.json" --parameters output="gs://hello-dataflow-bucket/output-" --region "us-east4"
# abrir o arquivo main.py e rodar <python3 main.py> com a seguinte linha comentada: template_location='gs://hello-dataflow-bucket/template', #para dev comentar (rodar python3 main.py) para prod descomentar


	

# Fazer o build do Dockerfile

#FROM gcr.io/dataflow-templates-base/python3-template-launcher-base

#[17:05] Michel Souza Santana
#Pegando uma imagem mais leve do python
FROM python:3.10-slim

COPY --from=apache/beam_python3.10_sdk:2.55.0 /opt/apache/beam /opt/apache/beam
COPY --from=gcr.io/dataflow-templates-base/python310-template-launcher-base:20230622_RC00 /opt/google/dataflow/python_template_launcher /opt/google/dataflow/python_template_launcher
 


# Diretório de trabalho
#ARG WORKDIR=/dataflow/template
ARG WORKDIR=/template
RUN mkdir ${WORKDIR}
WORKDIR ${WORKDIR}

# Instalando dependências
WORKDIR /opt
RUN apt-get update \
    && pip install apache-beam[gcp]==2.55.0 \
    #&& pip install -U -r ${WORKDIR}/requirements.txt \
    #&& apt-get install -y libffi-dev git \
    #&& rm -rf /var/lib/apt/lists/* \
    # Upgrade pip e instalação de requisitos
    && pip install --no-cache-dir --upgrade pip \
    # Limpeza de cache
    && apt-get clean \
    && rm -rf /tmp/*

# Desabilitando a instalação de dependências
#ENV PIP_NO_DEPS=True

# Definição de variáveis de ambiente
ENV FLEX_TEMPLATE_PYTHON_PY_FILE="${WORKDIR}/main.py"
ENV FLEX_TEMPLATE_PYTHON_SETUP_FILE="${WORKDIR}/setup.py"

# Copiando arquivos
COPY . ${WORKDIR}

# instalando requirements.txt
RUN pip install -U -r ${WORKDIR}/requirements.txt

ENTRYPOINT ["/opt/apache/beam/boot"]
