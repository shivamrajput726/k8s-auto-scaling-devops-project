output "public_ip" {
  description = "Public IP of the k3s EC2 instance."
  value       = aws_instance.k3s.public_ip
}

output "ssh_command" {
  description = "SSH command for the server."
  value       = "ssh -i <private-key-path> ubuntu@${aws_instance.k3s.public_ip}"
}

output "kubeconfig_scp_command" {
  description = "Command to download the generated kubeconfig."
  value       = "scp -i <private-key-path> ubuntu@${aws_instance.k3s.public_ip}:/home/ubuntu/kubeconfig ~/.kube/config"
}
