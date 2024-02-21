import json
from s3 import extract_bucket_and_key, get_s3_object_metadata
from upload_utils import check_last_chunk, get_chunk_range, create_joined_file

def lambda_handler(event, context):
    bucket_name, object_key = extract_bucket_and_key(event)
    object_metadata = get_s3_object_metadata(bucket_name, object_key)
    
    if check_last_chunk(object_metadata):
        _, chunks = get_chunk_range(object_metadata)
        create_joined_file(bucket_name, object_key, chunks)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
