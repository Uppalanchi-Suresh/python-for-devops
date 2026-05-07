import boto3

s3 = boto3.client('s3')

response = s3.get_bucket_acl(
    Bucket='my-bucket-boto13-test',
   )


print(acl_info)