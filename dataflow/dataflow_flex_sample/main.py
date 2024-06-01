#########################################
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam as beam
import os
import sys
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(asctime)s - %(levelname)s - %(message)s")

# Caminho para o arquivo de credenciais do Google Cloud
serviceAccount1 = '/src2/hello_word/learn-dataflow-420912-4e287b165003.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = serviceAccount1

#Configurações de conexão
DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'

now = datetime.now()

# Formatea la fecha en el formato deseado directamente en la cadena de formato
formatted_date = now.strftime("%Y-%m-%d-%H-%m-%s")

def main(argv=None):
    options = PipelineOptions(
        flags=argv,
        project='learn-dataflow-420912',
        region='us-east4',
        runner='DataflowRunner',
        streaming=False,
        job_name = f'ingest-teste1-{formatted_date}',
        temp_location= f"""gs://hello-dataflow-bucket/temp""",
        staging_locations= f"""gs://hello-dataflow-bucket/staging""",
        #template_location='gs://hello-dataflow-bucket/template/balneario', #para dev comentar (rodar python3 main.py) para prod descomentar
        autoscaling_algorithm='THROUGHPUT_BASED',
        worker_machine_type='n2-highmem-16',
        #service_account_key_file='./keys', #tem que estar na raiz
        num_workers=1,
        #max_num_workers=50,
        #number_of_worker_harness_threads=2,
        #experiments='use_runner_v2',
        disk_size_gb=25,
        save_main_session=True,
        sdk_container_image='us-east4-docker.pkg.dev/learn-dataflow-420912/repo-dataflow/dataflex-dev:latest',
        sdk_location='container',
        requirements_file='./requirements.txt',
        metabase_file='./metadata.json',
        setup_file='./setup.py',
        service_account_email='dataflow-teste@learn-dataflow-420912.iam.gserviceaccount.com',
        #subnetwork='https://www.googleapis.com/compute/v1/projects/vpc-host-prod-eh839-gx617/regions/us-central1/subnetworks/us-grp-jacto-data-analytics-subnet',
    )

    class PrintHelloWorld(beam.DoFn):
        def process(self, element):
            element = 'Hello World'
            # print(element)
            yield element

    with beam.Pipeline(options=options) as pipeline:
        (
            pipeline
            | beam.Create([None])
            | beam.ParDo(PrintHelloWorld())
            | beam.Map(print)
        )
        
if __name__ == '__main__':
    main()