# Deploy na AWS EC2

## Pré-requisitos

- Instância EC2 (Amazon Linux 2023)
- Security Group com portas 22, 80, 8000 abertas
- IAM Role com permissões para Textract, Rekognition, Bedrock

## 1. Configurar IAM Role

Anexe uma IAM Role à instância EC2 com as políticas:
- `AmazonTextractFullAccess`
- `AmazonRekognitionFullAccess`
- `AmazonBedrockFullAccess`

## 2. Setup da Instância

```bash
# Conectar via SSH
ssh -i sua-chave.pem ec2-user@<EC2_PUBLIC_IP>

# Clonar repositório
git clone <REPO_URL> app
cd app

# Executar setup
chmod +x scripts/setup.sh
./scripts/setup.sh

# Relogar para aplicar grupo docker
exit
ssh -i sua-chave.pem ec2-user@<EC2_PUBLIC_IP>
```

## 3. Configurar AWS CLI

```bash
aws configure
```

Informar:
- AWS Access Key ID
- AWS Secret Access Key
- Default region: us-east-1
- Default output format: json

## 4. Configurar Variáveis de Ambiente

```bash
cd app
cp .env.example .env
nano .env
```

Configurar:
```
DEBUG=false
AWS_REGION=us-east-1
ALLOWED_ORIGINS=http://<EC2_PUBLIC_IP>:3000
```

## 5. Deploy

```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

## 6. Verificar

```bash
# Status dos containers
docker-compose ps

# Logs
docker-compose logs -f backend

# Testar API
curl http://localhost:8000/api/v1/health
```

## Acessar

- API: `http://<EC2_PUBLIC_IP>:8000/docs`
- Frontend: `http://<EC2_PUBLIC_IP>:3000`

## Comandos Úteis

```bash
# Reiniciar
docker-compose restart

# Parar
docker-compose down

# Logs
docker-compose logs -f

# Rebuild
docker-compose up -d --build
```
