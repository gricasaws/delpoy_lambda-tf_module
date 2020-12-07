import os
import boto3
def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    print(s3_client.list_buckets())
    return "{} from Lambda!".format(os.environ['greeting'])