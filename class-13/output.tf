output "ec2_public_ip" {
  value = aws_instance.mcit_instance.public_ip
}