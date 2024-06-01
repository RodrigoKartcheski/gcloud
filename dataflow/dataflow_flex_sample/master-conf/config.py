#! config

project_id='learn-dataflow-420912'
region='us-east4' #'us-central1'
user_email='rodrigo.kartcheski@gmail.com'
service_account='dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com'
key_service_account = r'/home/jobs/gcloud/gcloud-cli-ubuntu-20/src/keys/learn-dataflow-420912-4e287b165003.json'
bucket_dataflow='hello-dataflow-bucket'
path_full_requirements='/home/jobs/gcloud/gcloud-cli-ubuntu-20/src/hello_word/requirements.txt'

# Comandos a serem executados usando as variáveis
comandos_iam = [
    f'gcloud projects add-iam-policy-binding learn-dataflow-420912 --member=user:{user_email} --role=roles/iam.serviceAccountUser',
    f'gcloud projects add-iam-policy-binding learn-dataflow-420912 --member=serviceAccount:{service_account} --role=roles/dataflow.admin',
    f'gcloud projects add-iam-policy-binding learn-dataflow-420912 --member="serviceAccount:{service_account}" --role=roles/iam.serviceAccountUser',
    f'gcloud projects add-iam-policy-binding learn-dataflow-420912 --member="serviceAccount:{service_account}" --role=roles/storage.objectAdmin'
]




################## exemplo do comando comandos_iam fixo ##################
"""
#! gcp_iam_management.py
import subprocess


# Comandos a serem executados
comandos = [
    'gcloud projects add-iam-policy-binding learn-dataflow-420912 --member=user:rodrigo.kartcheski@gmail.com --role=roles/iam.serviceAccountUser',
    'gcloud projects add-iam-policy-binding learn-dataflow-420912 --member=serviceAccount:dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com --role=roles/dataflow.admin',
    'gcloud projects add-iam-policy-binding learn-dataflow-420912 --member="serviceAccount:dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com" --role=roles/iam.serviceAccountUser',
    'gcloud projects add-iam-policy-binding learn-dataflow-420912 --member="serviceAccount:dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com" --role=roles/storage.objectAdmin'
]

# Executar cada comando
for comando in comandos:
    processo = subprocess.Popen(comando, shell=True)
    processo.wait()  # Aguardar o término do processo

print("Todos os comandos foram executados.")
"""
