import boto3

ficheroUpload = "productos.csv"
ficheroUpload1 = "tiene.csv"
ficheroUpload2 = "categorias.csv"
nombreBucket = "prdocutos-cloud-pp"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, "productos/productos.csv")
response1 = s3.upload_file(ficheroUpload1, nombreBucket, "tiene/tiene.csv")
response2 = s3.upload_file(ficheroUpload2, nombreBucket, "categorias/categorias.csv")

print("Ingesta completada")
