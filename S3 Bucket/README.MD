### Create S3 Bucket using CLI

RANDOM_ID=$(aws secretsmanager get-random-password \
--exclude-punctuation --exclude-uppercase \
--password-length 6 --require-each-included-type \
--output text \
--query RandomPassword)

#### Create S3 Bucket
aws s3api create-bucket --bucket awsml-$RANDOM_ID

Upload the file to AWS S3 Bucket: aws s3 cp file.txt s3://awsml-$RANDOM_ID 

Display Storage class: aws s3api list-objects-v2 --bucket awsml-$RANDOM_ID 

Delete files copied to S3 Bucket: aws s3 rm s3://awsml-$RANDOM_ID/file.txt

Delete S3 Bucket: aws s3api delete-bucket --bucket awsml-$RANDOM_ID 
