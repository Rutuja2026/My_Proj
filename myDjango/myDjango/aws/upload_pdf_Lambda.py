import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'
    file_content = event['file_content']  # Base64-encoded file content
    file_name = event['file_name']

    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=file_content,
        ContentType='application/pdf'
    )

    return {
        'statusCode': 200,
        'message': 'File uploaded successfully'
    }
