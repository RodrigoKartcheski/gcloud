from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions
import apache_beam as beam
import os
import logging
import sys
from config import project_id, region, key_service_account, path_full_requirements, bucket_dataflow

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(asctime)s - %(levelname)s - %(message)s")

serviceAccount=key_service_account #serviceAccount = r'/home/jobs/gcloud/gcloud-cli-ubuntu-20/src/keys/learn-gcp-cloud-run-328aca6c6796.json'
bucketDataflow=bucket_dataflow
project=project_id
region=region
bucketDataflow=bucket_dataflow
service_account=service_account
requirements_file=path_full_requirements
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = serviceAccount

# Parametros da Pipeline Options
options = PipelineOptions(
        flags=argv,
        project=project,
        runner='DataflowRunner',
        streaming=False,
        job_name='load-get_hello',
        temp_location=f"""'gs://{bucketDataflow}/tmp'""",
        staging_locations=f"""'gs://{bucketDataflow}/stagin'""",
        autoscaling_algorithm='THROUGHPUT_BASED',
        num_workers=5,
        region=region,
        #template_location='gs://hello-word-bucket/templates/tplt-hello-word-v2',
        #subnetwork='https://www.googleapis.com/compute/v1/projects/vpc-host-prod-eh839-gx617/regions/us-central1/subnetworks/us-grp-jacto-data-analytics-subnet',
        disk_size_gb=30,
        service_account_email=service_account,
        requirements_file=requirements_file,
        save_main_session = False
)

#*********************************************************************************************************

# Configurando pipeline options
#pipeline = beam.Pipeline(options=options)
#pipeline = beam.Pipeline()


class PrintHelloWorld(beam.DoFn):
  def process(self, element):
    element = 'Hello World'
    #print(element)
    yield element
    
#with beam.Pipeline(options=options) as pipeline: executa na rede
#with beam.Pipeline() as pipeline: executa local
def main(argv=None):
  with beam.Pipeline(options=options) as pipeline:
    _ = (
      pipeline
      | beam.Create([None])
      | beam.ParDo(PrintHelloWorld())
      | beam.Map(print)
    )
if __name__ == '__main__':
  main()
  
  
 
