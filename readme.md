# OpenData oev-live to S3
fetch Data from Swiss Opendata public transport http://oev-live.ch/, and upload it to S3 compatible Storage (run in Docker) for Big-data, Machine-Learning and Analytics purposes.

More info by [LeanBI](http://www.leanbi.ch)

##Usage

- Build Docker Image : docker build -t yourBaseName:andTag .


- Run : 
```shell
docker run \ 
    -e URL_DATA_REFERENCE \
    -e URL_DATA_TRANSACTION \
    -e REST_POLLING_INTERVAL=10 \
	-e S3_HOST=s3-us-west-2.amazonaws.com \
	-e S3_PORT=443 \
	-e S3_ACCESS_KEY=mykey \
	-e S3_SECRET_KEY=mypassword \
	-e S3_BUCKET=mybucket \
	-e S3_KEY=swissmeteo/data
	yourBaseName:andTag
```