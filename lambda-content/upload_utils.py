import boto3

def get_chunk_range(object_metadata: dict):
    current_chunk, last_chunk = object_metadata.get("chunk-range").split("/")
    return current_chunk, last_chunk


def check_last_chunk(object_metadata: dict):
    try:
        current_chunk, last_chunk = get_chunk_range(object_metadata)
        return current_chunk == last_chunk
    except Exception as err:
        print(err, err.__class__)
        print("[DEBUG] object_metadata ==>", object_metadata)
        return False


def get_object_bytes(bucket_name, object_key):
    s3_client = boto3.client('s3')

    try:
        # Obtenha o conteúdo do objeto S3
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        # Leia o conteúdo em bytes
        object_bytes = response['Body'].read()
        return object_bytes

    except Exception as e:
        print(f"Erro ao ler o objeto S3: {e}")
        return None


def upload_to_s3(file_path, bucket_name, object_key):
    # Crie uma instância do cliente S3
    s3_client = boto3.client('s3')

    try:
        # Faça o upload do arquivo para o S3
        s3_client.upload_file(file_path, bucket_name, object_key)

        print(f"Upload do arquivo {file_path} para {bucket_name}/{object_key} concluído com sucesso.")

    except Exception as e:
        print(f"Erro ao fazer upload do arquivo para o S3: {e}")


def create_joined_file(bucket_name, object_key, chunks):
    object_path = "/".join(object_key.split("/")[:-1])
    object_name = "-".join(object_key.split("/")[-1].split('-')[1:])
    
    if object_path != '':
        object_path += '/'
    
    joined_file_path = f"/tmp/{object_key}"
    with open(joined_file_path, 'wb') as file:
        
        for chunk in range(1, int(chunks)+1):
            chunk_s3_key = f"{object_path}{chunk}-{object_name}"
            chunk_bytes = get_object_bytes(bucket_name, chunk_s3_key)
            file.write(chunk_bytes)
    
    upload_to_s3(joined_file_path, bucket_name, f"joined_files/{object_name}")

    