import boto3

ficheroUpload = "productos.csv"
ficheroUpload1 = "tiene.csv"
ficheroUpload2 = "categorias.csv"
nombreBucket = "prdocutos-cloud-pp"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)
response1 = s3.upload_file(ficheroUpload1, nombreBucket, ficheroUpload1)
response2 = s3.upload_file(ficheroUpload2, nombreBucket, ficheroUpload2)

print("Ingesta completada")