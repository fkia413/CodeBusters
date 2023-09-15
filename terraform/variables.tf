# setting up the region
variable "aws_region" {
  default = "eu-west-2"
}

# setting the CIDR block for the VPC
variable "vpc_cidr_block" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

# setting the number of public and private subnets
variable "subnet_count" {
  description = "Number of subnets"
  type        = map(number)
  default = {
    public  = 2
    private = 2
  }
}

# setting the configuration settings for the EC2 and RDS instances
variable "settings" {
  description = "Configuration settings"
  type        = map(any)
  default = {
    "database" = {
      allocated_storage   = 20             # storage in 
      engine              = "mysql"        # engine type
      engine_version      = "8.0.33"       # engine version
      instance_class      = "db.t2.micro"  # rds instance type
      db_name             = "qa_cinema_db" # database name
      skip_final_snapshot = true
      publicly_accessible = true
    },
    "web_app" = {
      count         = 2 # number of EC2 instances
      instance_type = "t2.micro"
    }
  }
}

# setting the CIDR blocks for the public subnet
variable "public_subnet_cidr_blocks" {
  description = "Available CIDR blocks for public subnets"
  type        = list(string)
  default = [
    "10.0.1.0/24",
    "10.0.2.0/24",
    "10.0.3.0/24",
    "10.0.4.0/24"
  ]
}

# setting the CIDR blocks for the private subnet
variable "private_subnet_cidr_blocks" {
  description = "Available CIDR blocks for private subnets"
  type        = list(string)
  default = [
    "10.0.101.0/24",
    "10.0.102.0/24",
    "10.0.103.0/24",
    "10.0.104.0/24"
  ]
}

# IP address of the terraform server instance
# used when setting up the SSH rule on the web security group
variable "terraform_server_ip" {
  description = "Terraform server IP address"
  type        = string
  sensitive   = true
}

# setting the database master user
variable "db_username" {
  description = "Database master user"
  type        = string
  sensitive   = true
}

# setting the database master password
variable "db_password" {
  description = "Database master user password"
  type        = string
  sensitive   = true
}
