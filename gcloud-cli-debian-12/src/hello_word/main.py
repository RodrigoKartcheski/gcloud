from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam as beam
import os
import logging
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(asctime)s - %(levelname)s - %(message)s")

serviceAccount = r'/home/jobs/dataflow/first_hello_word/keys/learn-gcp-cloud-run-328aca6c6796.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = serviceAccount


def write_hello_word(argv=None):
    options = PipelineOptions(
        flags=argv,
        runner='DataflowRunner',
        project='learn-gcp-cloud-run',
        temp_location='gs://hello-word-bucket/tmp',
        staging_location='gs://hello-word-bucket/stagin',
        region='us-central1',
        service_account='dataflow-teste@learn-gcp-cloud-run.iam.gserviceaccount.com',  # Replace with your actual service account email
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
