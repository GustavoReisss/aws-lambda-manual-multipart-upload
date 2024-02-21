import boto3

def get_s3_object_metadata(bucket_name, key):
    # Crie uma instância do recurso S3
    s3_resource = boto3.resource('s3')
    metadata = {}

    try:
        # Obtenha uma referência para o objeto S3
        s3_object = s3_resource.Object(bucket_name, key)

        # Obtenha os metadados do objeto S3
        metadata = s3_object.metadata

    except Exception as e:
        print(f"Erro ao obter metadados: {e}")

    return metadata

def extract_bucket_and_key(event):
    # Obtenha o primeiro registro, se existir
    first_record = event.get('Records', [])[0]
    object_key = None
    bucket_name = None
    
    # Verifique se o registro existe e se o evento é do tipo desejado
    if first_record and 'eventName' in first_record and ('ObjectCreated' in first_record['eventName'] or 'ObjectRemoved' in first_record['eventName']):
        # Obtenha o nome do bucket e a chave do objeto
        bucket_name = first_record['s3']['bucket']['name']
        object_key = first_record['s3']['object']['key']
        
    return bucket_name, object_key