# capstone_project
# Data Engineering Project README

## Table of Contents
- [Project By](#By)
- [Overview](#overview)
- [Necessary Libraries, Tools, and Frameworks](#necessary-libraries-tools-and-frameworks)
- [Project Components](#project-components)
- [Running the Pipeline](#running-the-pipeline)
- [Setup Instructions](#Setup-Instructions)
- [Usage](#usage)
- [License](#license)


## Project By
Abigail Akua Sika Boateng

## Overview
This project aims to streamline the data pipeline for ingesting aviation data from the openweathermap API, persisting it in CSV format, setting up infrastructure using Terraform, utilizing AWS Glue for data processing, and loading the data into Amazon Redshift.

## Necessary Libraries, Tools, and Frameworks
- Python: Core programming language.
- Pandas: For data manipulation and analysis.
- Boto3: AWS SDK for Python, to interact with S3 and other AWS services.
- Psycopg2: PostgreSQL adapter for Python.
- AWS CLI: For managing AWS resources from the command line.
- Amazon S3 Bucket: Storage service.
- Amazon Redshift: Data warehouse service.
- PostgreSQL: Relational database management system.

## Project Components
1. **API Data Retrieval**: Fetch weather data from the openweathermap API and store it in CSV format.
2. **Infrastructure as Code (IaC)**:
   - Utilize Terraform for provisioning AWS resources including S3 bucket and Redshift cluster.
   - Configure permissions and access using Terraform IAM roles and policies.
3. **Environment Variables**:
   - Set up environment variables for AWS access key and secret access key to facilitate easy execution of the pipeline.
4. **Load data into s3 bucket using the command**:
   - aws s3 cp <local_file_path> s3://<bucket_name>/<key_name>
   - Replace <local_file_path> with the path to your local file and <bucket_name>/<key_name> with the S3 bucket and key where you want to store the file. The key represents the object's name within the bucket.
4. **AWS Glue Jobs**:
   - Employ AWS Glue for data transformation and preparation tasks as needed.
   - But the file for the glue job in the s3 bucket in a temp directory
5. **Data Loading to Redshift**:
   - Use AWS Redshift COPY command to load data from S3 into Redshift tables.


## Running the Pipeline
### Prerequisites
- Python 3.8+
- Pandas
- Boto3
- Psycopg2
- Python-dotenv
- Requests


## Setup Instructions
1. **Clone the Repository**:
   - git clone <repository-url>
   - cd <repository-folder>
2. **Install Dependencies**:
- Ensure Terraform is installed on your local machine.
- Install required Python packages for Glue jobs if applicable.
3. **Set Environment Variables**:
- set AWS access key, secret access key and default region as environment variables:
  ```
  set AWS_ACCESS_KEY_ID=<your-access-key>
  set AWS_SECRET_ACCESS_KEY=<your-secret-key>
  ```
4. **Terraform Setup**:
- Navigate to the `terraform` directory.
- Run `terraform init` to initialize Terraform.
- Run `terraform apply` to apply the Terraform configuration and provision infrastructure.
5. **AWS Glue Configuration**:
- Configure AWS Glue jobs as necessary for data transformation tasks.
6. **Data Loading to Redshift**:
- Execute Redshift COPY command to load data from S3 into Redshift tables.

## Usage
- Ensure all dependencies and environment variables are set up correctly before running the pipeline.
- Monitor pipeline execution and logs for any errors or issues.
- Troubleshoot and debug as needed to ensure smooth data pipeline operation.

## License
This project is licensed under the [MIT License](LICENSE).
