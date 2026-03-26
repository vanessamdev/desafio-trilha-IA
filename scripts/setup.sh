#!/bin/bash
# EC2 Setup Script

set -e

echo "=== Updating system ==="
sudo yum update -y

echo "=== Installing Docker ==="
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user

echo "=== Installing Docker Compose ==="
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

echo "=== Installing AWS CLI ==="
sudo yum install -y aws-cli

echo "=== Setup complete ==="
echo ""
echo "Next steps:"
echo "1. Log out and back in (for docker group)"
echo "2. Run: aws configure"
echo "3. Run: ./scripts/deploy.sh"
