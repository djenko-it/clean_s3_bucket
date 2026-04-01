import boto3

# Configuration
BUCKET_NAME = 'XXXX'
ENDPOINT_URL = 'https://s3.AAA.io.cloud.ovh.net' 
ACCESS_KEY = 'XXXX'
SECRET_KEY = 'XXXX'
REGION = 'AAA'

s3 = boto3.client('s3',
                  endpoint_url=ENDPOINT_URL,
                  aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY,
                  region_name=REGION)

def empty_bucket(bucket_name):
    print(f"Nettoyage du bucket {bucket_name}...")

    # On boucle tant qu'il reste des versions ou des marqueurs
    while True:
        versions = s3.list_object_versions(Bucket=bucket_name)

        objects_to_delete = []

        # Récupérer les versions de fichiers
        if 'Versions' in versions:
            for v in versions['Versions']:
                objects_to_delete.append({'Key': v['Key'], 'VersionId': v['VersionId']})

        # Récupérer les marqueurs de suppression (IMPORTANT pour vider totalement)
        if 'DeleteMarkers' in versions:
            for m in versions['DeleteMarkers']:
                objects_to_delete.append({'Key': m['Key'], 'VersionId': m['VersionId']})

        # S'il n'y a rien, on a fini
        if not objects_to_delete:
            break

        # On supprime par lot de 1000 (limite AWS S3)
        # On découpe la liste en chunks de 1000
        for i in range(0, len(objects_to_delete), 1000):
            batch = objects_to_delete[i:i+1000]
            print(f"Suppression de {len(batch)} éléments...")
            s3.delete_objects(Bucket=bucket_name, Delete={'Objects': batch})

    print("Bucket vidé !")
    # Optionnel : supprimer le bucket lui-même à la fin
    # s3.delete_bucket(Bucket=bucket_name)
    # print("Bucket supprimé.")

empty_bucket(BUCKET_NAME)
