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

FROM gcr.io/dataflow-templates-base/python3-template-launcher-base

# Diretório de trabalho
ARG WORKDIR=/dataflow/template
RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}

# Copiando arquivos
COPY . ${WORKDIR}

# Instalando dependências
WORKDIR /opt
RUN apt-get update \
    && pip install apache-beam[gcp]==2.55.0 \
    && pip install -U -r ${WORKDIR}/requirements.txt \
    && apt-get install -y libffi-dev git \
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

CMD [ "main.py" ]
