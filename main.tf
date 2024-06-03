provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  default = "us-west-2"
}

# Create an S3 bucket
resource "aws_s3_bucket" "data_bucket" {
  bucket = "my-capstone-project-bucket-sika"
  tags = {
    Name        = "MyDataBucket"
    Environment = "Dev"
  }
}

# Define IAM policy for full access to S3 and Redshift
resource "aws_iam_policy" "full_access_policy" {
  name        = "RedshiftftS3AccessRole"
  description = "Policy that grants full access to S3 and Redshift"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = ["s3:*"],
        Effect = "Allow",
        Resource = "*"
      },
      {
        Action = ["redshift:*"],
        Effect = "Allow",
        Resource = "*"
      }
    ]
  })
}


# Create an IAM role
resource "aws_iam_role" "redshift_role" {
  name = "MyRedshiftRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "redshift.amazonaws.com"
        }
      }
    ]
  })
}

# Attach the policy to the IAM role
resource "aws_iam_role_policy_attachment" "redshift_role_policy_attachment" {
  role       = aws_iam_role.redshift_role.name
  policy_arn = aws_iam_policy.full_access_policy.arn
}

variable "vpc_id" {
  description = "The ID of the VPC where the Redshift cluster will be deployed"
  type        = string
  # You can optionally set a default value here
  default     = "vpc-02656fa6588a74294"
}

# Create a security group for Redshift
resource "aws_security_group" "redshift_sg" {
  name        = "redshift-sg"
  description = "Security group for Redshift cluster"
  vpc_id      = var.vpc_id
 

  ingress {
    from_port   = 5439
    to_port     = 5439
    protocol    = "tcp"
    cidr_blocks = ["35.83.133.88/32"]  # Replace with your IP or CIDR block
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create a Redshift cluster
resource "aws_redshift_cluster" "my_redshift_cluster" {
  cluster_identifier = "my-redshift-cluster"
  node_type          = "dc2.large"
  master_username    = "awsuser"
  master_password    = "YourPassword123"
  cluster_type       = "single-node"
  iam_roles          = [aws_iam_role.redshift_role.arn]
  database_name      = "dev"
  vpc_security_group_ids = [aws_security_group.redshift_sg.id]
}

# Add an S3 bucket policy to allow Redshift to read data from the bucket
resource "aws_s3_bucket_policy" "bucket_policy" {
  bucket = aws_s3_bucket.data_bucket.id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "redshift.amazonaws.com"
        },
        Action = "s3:GetObject",
        Resource = "${aws_s3_bucket.data_bucket.arn}/*"
      }
    ]
  })
}
