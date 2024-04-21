from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions
import apache_beam as beam
import os
import logging
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(asctime)s - %(levelname)s - %(message)s")

serviceAccount = r'/home/jobs/dataflow/first_hello_word/learn-gcp-cloud-run-3ebe1a413417.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = serviceAccount

# Parametros da Pipeline Options
options = PipelineOptions(
        flags=argv,
        project='learn-gcp-cloud-run',
        runner='DataflowRunner',
        streaming=False,
        job_name='load-get_hello',
        temp_location='gs://hello-word-bucket/tmp',
        staging_locations='gs://hello-word-bucket/stagin',
        autoscaling_algorithm='THROUGHPUT_BASED',
        num_workers=1,
        region='us-central1',
        #template_location='gs://hello-word-bucket/templates/tplt-hello-word-v2',
        #subnetwork='https://www.googleapis.com/compute/v1/projects/vpc-host-prod-eh839-gx617/regions/us-central1/subnetworks/us-grp-jacto-data-analytics-subnet',
        disk_size_gb=30,
        service_account_email='dataflow-teste@learn-gcp-cloud-run.iam.gserviceaccount.com',
        requirements_file='/home/jobs/dataflow/first_hello_word/hello_word/requirements.txt',
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
  
  
 
