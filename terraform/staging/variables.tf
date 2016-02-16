
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Secret Variables - secret.tfvars
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
variable "access_key" {}
variable "secret_key" {}
variable "key_name" {}
variable "public_key_path" {}



########################################
# Public Variables - terraform.tfvars
########################################

variable "region" {}
variable "availability_zone" {}

# AMI
# Debian Jessie amd64 HVM EBS
# https://wiki.debian.org/Cloud/AmazonEC2Image/Jessie
variable "user" {}
variable "amis" {
    default = {
        us-east-1 = "ami-116d857a"
        us-west-2 = "ami-05cf2541"
    }
}

# Instances
variable "web_instance_type" {}
variable "shell_instance_type" {}
variable "db_instance_type" {}

# Network
variable "vpc_cidr" {}
variable "public_subnet_cidr" {}
variable "web_private_ip" {}
variable "shell_private_ip" {}
variable "db_private_ip" {}
variable "coco_db_cidr" {}
variable "home_test_db_cidr" {}

# EBS Volumes
variable "db_ebs_data_size" {}
variable "db_ebs_data_device_name" {}

# Tags
variable "year" {}
variable "environment" {}
variable "web_name" {}
variable "shell_name" {}
variable "db_name" {}
variable "db_ebs_data_name" {}

