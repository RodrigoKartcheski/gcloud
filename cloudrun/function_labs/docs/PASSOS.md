#

minha-app vai se chamar fct-lab1-app
meu repositorio do Artifacty fct-lab1-repo


✅ 1. Criar o diretorio
	mkdir lab1

✅ 2. Criar o cloudbuild,yaml
	exemplo na pasta lab1


✅ 3. Criar o requeriments.txt
	exemplo na pasta lab1
✅ 4. Criar o arquivo main.py
	exemplo na pasta lab1

✅ 5. Testar localmente
	docker build -t fct-lab1-app .
	docker run -p 8080:8080 fct-lab1-app


✅ 6. Autenticar no Gcloud

	gcloud auth login
	
	gcloud config set project [SEU_PROJETO]


## Criar o repositório no Artifact Registry

gcloud artifacts repositories create fct-lab1-repo \
    --repository-format=docker \
    --location=us-east1 \
    --description="DESCRIPTION"
    
 
## Verificar se o repositorio foi criado
 
gcloud artifacts repositories list
    

## Criar uma função remotamente usando gcloud para enviar o código-fonte do aplicativo para o Cloud Build

gcloud builds submit --pack image=us-east1-docker.pkg.dev/dataplex-experience-6133/fct-lab1-repo
gcloud builds submit --pack image=us-east1-docker.pkg.dev/dataplex-experience-6133/fct-lab1-repo/fct-lab1-app


## Crie o aplicativo com Dockerfile

gcloud builds submit .

## Verifique se a função de amostra foi publicada em REPO_NAME

gcloud artifacts docker images list us-east1-docker.pkg.dev/dataplex-experience-6133/fct-lab1-repo


gcloud functions deploy myfunction-lab1 \
   --entry-point myFunctionHandler \
   --gen2 \
   --runtime python310 \
   --trigger-http \
   --allow-unauthenticated \
   --docker-repository projects/dataplex-experience-6133/locations/us-east1/repositories/fct-lab1-repo \
   --region us-east1



## fonte

https://cloud.google.com/run/docs/building/functions?hl=pt-br#python
https://cloud.google.com/sdk/gcloud/reference/functions/deploy

