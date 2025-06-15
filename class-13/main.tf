provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "mcit_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = {
    Name = "mcit-network"
  }
}

resource "aws_subnet" "mcit_subnet" {
  vpc_id                  = aws_vpc.mcit_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true
  tags = {
    Name = "mcit-subnet"
  }
}

resource "aws_internet_gateway" "mcit_igw" {
  vpc_id = aws_vpc.mcit_vpc.id
  tags = {
    Name = "mcit-igw"
  }
}

resource "aws_route_table" "mcit_rt" {
  vpc_id = aws_vpc.mcit_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.mcit_igw.id
  }
  tags = {
    Name = "mcit-route-table"
  }
}

resource "aws_route_table_association" "mcit_rta" {
  subnet_id      = aws_subnet.mcit_subnet.id
  route_table_id = aws_route_table.mcit_rt.id
}

resource "aws_security_group" "mcit_sg" {
  name        = "mcit-sg"
  description = "Allow SSH and HTTP"
  vpc_id      = aws_vpc.mcit_vpc.id

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "mcit-sg"
  }
}

resource "aws_instance" "mcit_instance" {
  ami                    = "ami-0c2b8ca1dad447f8a" # Amazon Linux 2 in us-east-1
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.mcit_subnet.id
  vpc_security_group_ids = [aws_security_group.mcit_sg.id]
  associate_public_ip_address = true
  key_name               = var.key_name

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl enable httpd
              systemctl start httpd
              echo "Hello Nicolas, Delisle" > /var/www/html/index.html
              EOF

  tags = {
    Name = "mcit-ec2-test"
  }
}