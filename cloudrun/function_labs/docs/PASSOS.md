#

minha-app 
meu repositorio do Artifacty


✅ 1. Criar o diretorio
	mkdir lab1

✅ 2. Criar o Dockerfile
	exemplo na pasta lab1


✅ 3. Criar o requeriments.txt
	exemplo na pasta lab1
✅ 4. Criar o arquivo main.py
	exemplo na pasta lab1

✅ 5. Testar localmente
	docker build -t lab1-app .
	docker run -p 8080:8080 lab1-app


--------------------------------------------

✅ 6. Autenticar no Gcloud

	gcloud auth login
	
	gcloud config set project [SEU_PROJETO]


✅ 7. Atualizar o Flask e o Werkzeug

## Criar o repositório no Artifact Registry

gcloud artifacts repositories create cr-lab1-repo \
    --repository-format=docker \
    --location=us-east1

## Autenticar no Artifact Registry
gcloud auth configure-docker us-east1-docker.pkg.dev


## Construir e enviar a imagem "minha-app-art" para o Artifact Registry

gcloud builds submit --tag us-east1-docker.pkg.dev/[SEU_PROJETO]/cr-lab1-repo/lab1-app

Explicação:

	us-central1-docker.pkg.dev → Serviço e região
	[SEU_PROJETO] → Substitua pelo nome do seu projeto no Google Cloud
	cr-lab1-repo → Nome do repositório
	lab1-app → Nome da imagem
	
## Verificar se a imagem foi enviada com sucesso

gcloud artifacts docker images list us-east1-docker.pkg.dev/dataplex-experience-6133/cr-lab1-repo


✅ 8. Passos para implantação no Cloud Run:

## Verifique se a imagem foi corretamente enviada para o Artifact Registry:

gcloud artifacts docker images list us-east1-docker.pkg.dev/[SEU_PROJETO]/meu-rep-hello


## Implantar a imagem no Cloud Run:
gcloud run deploy minha-app \
    --image us-east1-docker.pkg.dev/dataplex-experience-6133/cr-lab1-repo/lab1-app \
    --platform managed \
    --region us-east1 \
    --allow-unauthenticated

Detalhes:

	--image us-east1-docker.pkg.dev/dataplex-experience-6133/meu-rep-hello/minha-app-art: Aqui você está especificando a URL da imagem no Artifact Registry.
	--platform managed: Usando a plataforma Cloud Run gerenciada.
	--region us-central1: Região onde você deseja implantar a aplicação (substitua se necessário).
	--allow-unauthenticated: Permite acesso público à aplicação.


✅ 9. Verifique o status da implantação

Verifique o status da implantação: Após executar o comando, você verá a URL pública para acessar o serviço no Cloud Run. Verifique a resposta do comando para garantir que a implantação foi bem-sucedida.
