from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam as beam
import os
import logging
import sys
from config import project_id, region, service_account, key_service_account, bucket_dataflow


logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(asctime)s - %(levelname)s - %(message)s")

project=project_id
region=region
serviceAccount=key_service_account #serviceAccount = r'/home/jobs/gcloud/gcloud-cli-ubuntu-20/src/keys/learn-gcp-cloud-run-328aca6c6796.json'
bucketDataflow=bucket_dataflow #'hello-dataflow-bucket'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = serviceAccount


def write_hello_word(argv=None):
    options = PipelineOptions(
        flags=argv,
        runner='DataflowRunner',
        project=project,
        temp_location=f"""'gs://{bucketDataflow}/tmp'""",
        staging_location=f"""'gs://{bucketDataflow}/stagin'""",
        region=region,
        service_account=service_account,  # Replace with your actual service account email
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

if __name__ == "__main__":
    write_hello_word()
