import functions_framework
from gcs2bq import GcsToDataFrame, BigQueryLoader

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):

    # Parâmetros necessários
    project_id = "dataplex-experience-6133"
    bucket_name = "bucket_new2025"
    folder_name = "pastateste"
    sheet_name = "Planilha1"
    dataset_id = "data_conjunto"
    table_id = "table_id2"
    unique_key_columns = ["id"]

    # Carregar os dados do GCS usando a classe GcsToDataFrame
    gcs_loader = GcsToDataFrame(
        project_id=project_id,
        bucket_name=bucket_name,
        folder_name=folder_name,
        sheet_name=sheet_name
    )

    # Chama o método que retorna o DataFrame com os dados carregados
    df = gcs_loader.load_all_excel_from_folder()

    # Chamar a classe BigQueryLoader e carregar os dados no BigQuery
    bq_loader = BigQueryLoader(project_id, dataset_id, table_id, unique_key_columns)
    bq_loader.upsert_to_bigquery(df)

    return "Data loaded to BigQuery successfully", 200

