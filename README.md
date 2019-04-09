# hourly-etl-app

This project does ETL on hourly batches received about flats in Berlin available for rent 
for rent at immobilienscout24.de.

# Requirement

Transform and Load the hourly data batches in to Redshift.

# Assumptions

File arrives on S3 every hour

# Architecture 

The Architecture involves the following tech stack.

- Docker/Kubernetes
- AWS S3
- AWS Lambda
- Python 3.6.6

Justification on Tech Choices:

I decided to go on with this architecture based on the scope of the project as it gives us better `maintanability` and `deployability`.

 1. Docker -> is the go to choice while desigining any application 
 2. AWS S3 -> Assuming that the input data arrives in s3, the transformed data will be also stored in S3. Storing the data (raw/clean) in s3 gives us the power of having a centralized data repository (datalake).
 3. AWS Lambda -> Lambda is a wonderful serverless service that runs in response to events and automatically manages the computing resources. I have used lambda here to load (COPY) the data from s3 into redshift on arrival of transformed hourly batches.
 
# Data Pipeline Flow

![ARCHITECTURE DIAGRAM](https://github.com/ashshetty90/etl-hourly-app/blob/master/blob/master/images/architecture.jpg)


# What can be done better
1. We can schedule the entire workflow on Airflow.

2. Airflow Sensors can be used to trigger the job everytime that data is available on S3

3. SQS/Kafka could also have been used as an alternative



# How to run this application

```sh
### Python Application to do Extract and Transform hourly batches
### Clone the repository [https://github.com/ashshetty90/etl-hourly-app.git]

### First things First . Create a virtual environment and run the tests to make sure we are all set

$ virtualenv etl-hourly-app -p /usr/local/bin/python3.6
    
### and then activate the virtual environment
$ source etl-hourly-app/bin/activate

### install dependecies from Pipfile
$ pipenv install

### run the tests
$ APP_ENV=test pipenv run pytest

### Fill out the following details in /etl-hourly-app/batchprocessor/config/ for respective environments
### Output S3 Bucket
### AWS Secret key and Access Key - Ideally, we should not be storing the credentials in the applications as it not secure and should be using IAM roles 

### Having completed the preliminary steps , create a docker image by running the following command.
$ docker build -t etl-hourly-app .

### Run the docker image.
$ docker run -d --name etl-hourly-app etl-hourly-app python app.py --env=production

### Lambda function for Loading Redshift ( This has not been tested due to time constraints)
### clone the repository for lambda function which is developed on Serverless Framework.
https://github.com/ashshetty90/redshift-loader.git

### Fill out the respective details in the file Serverless.yml

### This function can be packaged and be uploaded to Lambda directly or via s3 or via Serverless commands
$ npm install -g serverless
$ sls plugin install -n serverless-python-requirements

# deploy lambda function
$ sls deploy -v --stage ${env}

```

# Screenshots

### Initial Steps

![INITIAL STEPS](https://github.com/ashshetty90/etl-hourly-app/blob/master/blob/master/images/initial-setup.png)



# Data Model

Though it leads to Query Complexities, Snowflake Schema would be a better approach in this case , as with snowflake schema (normalized) we can save lot of space in the data warehouse (Redshift) and when dimension tables require a significant amount of storage space. 

![TABLE RELATION](https://github.com/ashshetty90/etl-hourly-app/blob/master/blob/master/images/redshift-table-relation.png)
