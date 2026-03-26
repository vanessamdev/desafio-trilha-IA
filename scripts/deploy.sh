#!/bin/bash
# Deploy Script

set -e

APP_DIR=/home/ec2-user/app

echo "=== Deploying application ==="

cd $APP_DIR

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '#' | xargs)
fi

# Pull latest changes (if using git)
# git pull origin main

# Build and start containers
docker-compose down
docker-compose build --no-cache
docker-compose up -d

echo "=== Deployment complete ==="
docker-compose ps
