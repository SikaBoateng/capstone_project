import psycopg2
import boto3

# Replace these values with your Redshift cluster details
redshift_cluster_endpoint = 'my-redshift-cluster.cqcffu7md9i7.us-west-2.redshift.amazonaws.com:5439/dev'
redshift_database = 'dev'
redshift_user = 'awsuser'
redshift_password = ' '
redshift_port = '5439'

# Replace these values with your IAM role and S3 bucket details
iam_role_arn = 'arn:aws:iam::654654163000:role/MyRedshiftRole'
s3_bucket_name = 'my-capstone-project-bucket-sika'
s3_file_path = 'PRE folder/'  # This is the path in your S3 bucket

# Connect to Redshift
try:
    conn = psycopg2.connect(
        dbname=redshift_database,
        user=redshift_user,
        password=redshift_password,
        host=redshift_cluster_endpoint,
        port=redshift_port
    )
    print("Connected to Redshift successfully")
except Exception as e:
    print("Unable to connect to Redshift")
    print(e)
    exit(1)

cur = conn.cursor()

# SQL command to create the table
create_table_query = """
CREATE TABLE IF NOT EXISTS weather_data (
    lon FLOAT,
    lat FLOAT,
    temp FLOAT,
    feels_like FLOAT,
    humidity INT,
    pressure INT,
    wind_speed FLOAT,
    cloudiness INT,
    country VARCHAR(2),
    name VARCHAR(50),
    last_modified_timestamp TIMESTAMP
);
"""

# Execute the SQL command to create the table
try:
    cur.execute(create_table_query)
    conn.commit()
    print("Table created successfully")
except Exception as e:
    print("Error creating table")
    print(e)
    conn.rollback()

# Copy data from S3 to Redshift
copy_query = f"""
COPY weather_data
FROM 's3://{s3_bucket_name}/{s3_file_path}'
IAM_ROLE '{iam_role_arn}'
CSV
IGNOREHEADER 1;
"""

try:
    cur.execute(copy_query)
    conn.commit()
    print("Data loaded from S3 to Redshift successfully")
except Exception as e:
    print("Error loading data from S3 to Redshift")
    print(e)
    conn.rollback()

# Close the cursor and connection
cur.close()
conn.close()
