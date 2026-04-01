# OVH S3 Bucket Cleaner

A Python script to completely empty an OVH S3 bucket, including all object versions and delete markers.

## Features
- Deletes all object versions
- Removes delete markers
- Handles large buckets with batch deletion (1000 objects at a time)
- Works with OVH's S3-compatible storage

## Prerequisites
- Python 3.x
- boto3 library (`pip install boto3`)
- OVH S3 credentials

## Configuration
Edit the `clean_bucket.py` file and replace these placeholder values:
- `BUCKET_NAME`: Your OVH S3 bucket name
- `ENDPOINT_URL`: Your OVH S3 endpoint (e.g., `https://s3.gra.io.cloud.ovh.net`)
- `ACCESS_KEY`: Your OVH access key
- `SECRET_KEY`: Your OVH secret key
- `REGION`: Your OVH region (e.g., `gra`)

## Usage
1. Install dependencies: `pip install boto3`
2. Configure your credentials in the script
3. Run the script: `python clean_bucket.py`

## Important Notes
- This script will permanently delete all objects in the specified bucket
- The bucket deletion line is commented out by default (line 48-49)
- Uncomment those lines if you want to delete the bucket itself after emptying
- Always double-check your bucket name before running

## Safety Recommendations
1. Test with a non-critical bucket first
2. Consider backing up important data before running
3. Review the code to understand what will be deleted
