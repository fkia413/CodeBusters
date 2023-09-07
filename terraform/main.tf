# defining Terraform settings
terraform {
  required_providers {
    # we use only aws as the provider
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.0"
    }
  }
}

# configure AWS provider
provider "aws" {
  region                  = var.aws_region
  shared_credentials_file = "~/.aws/credentials"
}

# data object that is going to be hoding all the available vailability zones in our defined region
data "aws_availability_zones" "available" {
  state = "available"
}

# creating a VPC
resource "aws_vpc" "qa_cinema_vpc" {
  # setting the CIDR block of the VPC to the vpc_cidr_block variable
  cidr_block = var.vpc_cidr_block
  # enabled DNS hostnames for this VPC
  enable_dns_hostnames = true

  # tagging the VPC with a name
  tags = {
    Name = "QA_Cinema_VPC"
  }
}

# creating the Internet Gateway and attaching it to the VPC
resource "aws_internet_gateway" "qa_cinema_igw" {
  # attach the IGW to the VPC
  vpc_id = aws_vpc.qa_cinema_vpc.id

  # tagging the IGW with a name
  tags = {
    Name = "QA_Cinema_IGW"
  }
}

# creating the subnets
# RDS requires 2 subnets for a database
# and our database is goig to be in a private subnet

# create a group of public subnets based on the variable subnet_count.public
resource "aws_subnet" "qa_cinema_public_subnet" {
  # count is the number of resources we want to create (1)
  count = var.subnet_count.public

  # put the subnet into the VPC
  vpc_id = aws_vpc.qa_cinema_vpc.id

  # grab CIDR block from list set in variables.tf
  cidr_block = var.public_subnet_cidr_blocks[count.index]

  # grab availability zone from the data object created earlier
  availability_zone = data.aws_availability_zones.available.names[count.index]

  # tagging the subnet with a name
  tags = {
    Name = "QA_Cinema_public_subnet_${count.index}"
  }
}

# create a group of private subnets baed on the variable subnet_count.private
resource "aws_subnet" "qa_cinema_private_subnet" {
  # count is the number of resources we want to create (2)
  count = var.subnet_count.private

  # put the subnet into the VPC
  vpc_id = aws_vpc.qa_cinema_vpc.id

  # grab CIDR block from list set in variables.tf
  cidr_block = var.private_subnet_cidr_blocks[count.index]

  # grab availability zone from the data object created earlier
  availability_zone = data.aws_availability_zones.available.names[count.index]

  # tagging the subnet with a name
  tags = {
    Name = "QA_Cinema_private_subnet_${count.index}"
  }
}

# creating the route tables
# create a public route table
resource "aws_route_table" "qa_cinema_public_rt" {
  # put the route table in the VPC
  vpc_id = aws_vpc.qa_cinema_vpc.id

  # public route table, it will need access to the internet
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.qa_cinema_igw.id
  }
}

# add the public subnets to the public route table
resource "aws_route_table_association" "public" {
  # count is the number of subnets we want to associate with this route table (1)
  count = var.subnet_count.public

  # making sure that the route table is the qa_cinema_public_rt from above
  route_table_id = aws_route_table.qa_cinema_public_rt.id

  # subnet ID
  subnet_id = aws_subnet.qa_cinema_public_subnet[count.index].id
}

# create a private route table
resource "aws_route_table" "qa_cinema_private_rt" {
  # put the route table in the VPC
  vpc_id = aws_vpc.qa_cinema_vpc.id

  # private route table, no need to add a route
}

# add the private subnets to the private route table
resource "aws_route_table_association" "private" {
  # count is the number of subnets we want to associate with this route table (2)
  count = var.subnet_count.private

  # making sure that the route table is the qa_cinema_private_rt from above
  route_table_id = aws_route_table.qa_cinema_private_rt.id

  # subnet ID
  subnet_id = aws_subnet.qa_cinema_private_subnet[count.index].id
}

# creating the security groups
# - EC2 instances accessible anywhere on the internet via HTTP
# - Restricted access to EC2 instances via SSH 
# - RDS is on a private subnet and inaccessible via the internet
# - Only the EC2 instances are able to communicate with the RDS
# creating a security for the EC2 instances 
resource "aws_security_group" "qa_cinema_web_sg" {
  # basic details - name and description of the SG
  name        = "qa_cinema_web_sg"
  description = "Security group for web servers"

  # we want the SG to be in the qa_cinema_vpc
  vpc_id = aws_vpc.qa_cinema_vpc.id

  # making the EC2 instances accessible from anywhere on the internet via HTTP
  ingress {
    description = "Allow all traffic through HTTP"
    from_port   = "80"
    to_port     = "80"
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # restricting access to the EC2 instances
  ingress {
    description = "Allow SSH from only this instance"
    from_port   = "22"
    to_port     = "22"
    protocol    = "tcp"
    cidr_blocks = ["${var.terraform_server_ip}/32"]
  }

  # allowing all outbound traffic with the EC2 instances
  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "QA_Cinema_web_sg"
  }
}

# creating a security group for the RDS instance 
resource "aws_security_group" "qa_cinema_db_sg" {
  # basic details - name and description of the SG
  name        = "qa_cinema_db_sg"
  description = "Security group for RDS"

  # we want the SG to be in the qa_cinema_vpc
  vpc_id = aws_vpc.qa_cinema_vpc.id

  # we do not add any inbound or outbound rules for outside traffic
  # this is to accomplish having the RDS on a private subnet and inaccessible via the internet

  # making sure that only the EC2 instances can communicate with the RDS
  # inbound rule that allows traffic from the EC2 SG through TCP port 3306 (MySQL)
  ingress {
    description     = "Allow MySQL traffic from only the web sg"
    from_port       = 3306
    to_port         = 3306
    protocol        = "tcp"
    security_groups = [aws_security_group.qa_cinema_web_sg.id]
  }

  tags = {
    Name = "QA_Cinema_db_sg"
  }
}

# creating a db subnet group
resource "aws_db_subnet_group" "qa_cinema_db_subnet_group" {
  # basic details - name and description of the subnet group
  name        = "qa_cinema_db_subnet_group"
  description = "DB subnet group for tutorial"

  # since the db subnet group requires 2 or more subnets, we loop through our private subnets
  # and add them to this db subnet group
  subnet_ids = [for subnet in aws_subnet.qa_cinema_private_subnet : subnet.id]
}

# creating a db instance
resource "aws_db_instance" "qa_cinema_db" {
  # engine we want for the db
  engine = var.settings.database.engine
  # amount of storage in gigabytes for the db
  allocated_storage = var.settings.database.allocated_storage
  # version of the database engine
  engine_version = var.settings.database.engine_version
  # instance type of the database
  instance_class = var.settings.database.instance_class
  # master user of the database
  username = var.db_username
  # password for the master user
  password = var.db_password
  # DB subnet group
  db_subnet_group_name = aws_db_subnet_group.qa_cinema_db_subnet_group.id
  # security group for the database
  vpc_security_group_ids = [aws_security_group.qa_cinema_db_sg.id]
  # whether to skip the final snapshot of the db or not  
  skip_final_snapshot = var.settings.database.skip_final_snapshot
}

# creating the EC2 instances

# create a key pair
resource "aws_key_pair" "EC2_kp" {
  # name of the key pair
  key_name = "EC2_kp"

  # public key of the SSH key
  public_key = file("~/.ssh/EC2_kp.pub")
}

# create the EC2 instance
resource "aws_instance" "web" {
  count                  = var.settings.web_app.count
  ami                    = "ami-0eb260c4d5475b901"
  instance_type          = var.settings.web_app.instance_type
  subnet_id              = aws_subnet.qa_cinema_public_subnet[count.index].id
  key_name               = aws_key_pair.EC2_kp.key_name
  vpc_security_group_ids = [aws_security_group.qa_cinema_web_sg.id]
  tags = {
    Name = "QA_Cinema_web_${count.index}"
  }
}

# creating an Elastic IP and attach it to the EC2 instance
resource "aws_eip" "qa_cinema_web_eip" {
  count    = var.settings.web_app.count
  instance = aws_instance.web[count.index].id
  vpc      = true
  tags = {
    Name = "QA_Cinema_web_eip_${count.index}"
  }
}
