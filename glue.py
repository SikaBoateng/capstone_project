import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

# Initialize Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Define Redshift connection parameters
redshift_connection_options = {
    "url": "jdbc:redshift://your-redshift-cluster.cqcffu7md9i7.us-west-2.redshift.amazonaws.com:5439/dev",
    "dbtable": "weather_data",
    "user": "awsuser",
    "password": "YourPassword123",
    "redshiftTmpDir": "s3://PRE folder/",
    "forward_spark_s3_credentials": "true"
}

# Load data from S3 into a DynamicFrame
s3_path = "s3://my-capstone-project-bucket-sika/PRE folder/"
dynamic_frame = glueContext.create_dynamic_frame.from_options(
    "s3", {"paths": [s3_path]}, format="csv")

# Write DynamicFrame to Redshift
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame,
    connection_type="redshift",
    connection_options=redshift_connection_options,
    transformation_ctx="redshift_sink"
)

# Job execution completed
print("Data loaded into Redshift successfully")
