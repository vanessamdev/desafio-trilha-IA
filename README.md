# Análise de Contratos com IA

Sistema de análise de contratos utilizando serviços AWS (Textract, Rekognition, Bedrock) com arquitetura Clean Architecture.

## Funcionalidades

- Extração de texto de documentos (PDF, PNG, JPEG)
- Validação facial (opcional)
- Análise de contratos com IA
- Interface web simples

## Tecnologias

- **Backend:** Python 3.12, FastAPI
- **Frontend:** HTML5, CSS, JavaScript
- **AWS:** Textract, Rekognition, Bedrock
- **Arquitetura:** Clean Architecture, SOLID

## Estrutura do Projeto

```
├── backend/
│   └── app/
│       ├── main.py                 # Entry point FastAPI
│       ├── core/                   # Configurações e DI
│       ├── presentation/           # Routes, schemas, validators
│       ├── application/            # Use cases
│       ├── domain/                 # Entities e interfaces
│       └── infrastructure/         # AWS services, repositories
├── frontend/
│   ├── index.html
│   ├── css/
│   └── js/
├── docker/
│   └── Dockerfile
├── scripts/
│   ├── setup.sh
│   └── deploy.sh
├── requirements.txt
└── docker-compose.yml
```

## Pré-requisitos

- Python 3.12+
- Conta AWS com acesso a Textract, Rekognition e Bedrock
- Credenciais AWS (Access Key e Secret Key)

## Instalação

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd IA-desafios
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar ambiente virtual

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

## Executando o Projeto

### Backend

**Windows (PowerShell):**
```powershell
$env:DEBUG="false"
$env:AWS_ACCESS_KEY_ID="SUA_ACCESS_KEY"
$env:AWS_SECRET_ACCESS_KEY="SUA_SECRET_KEY"
$env:AWS_REGION="us-east-1"

uvicorn backend.app.main:app --reload
```

**Linux/Mac:**
```bash
export DEBUG=false
export AWS_ACCESS_KEY_ID=SUA_ACCESS_KEY
export AWS_SECRET_ACCESS_KEY=SUA_SECRET_KEY
export AWS_REGION=us-east-1

uvicorn backend.app.main:app --reload
```

### Frontend

Abra o arquivo `frontend/index.html` no navegador.

### Modo Mock (sem AWS)

Para testar sem credenciais AWS:

```powershell
$env:DEBUG="true"
uvicorn backend.app.main:app --reload
```

## Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/health` | Health check |
| POST | `/api/v1/analyze-contract` | Análise de contrato |

### Exemplo de uso

```bash
curl -X POST "http://localhost:8000/api/v1/analyze-contract" \
  -F "document=@contrato.png"
```

## Resposta da API

```json
{
  "request_id": "uuid",
  "status": "success",
  "document_filename": "contrato.png",
  "document_data": {
    "raw_text": "Texto extraído...",
    "fields": {},
    "confidence": 95.5,
    "pages_count": 1
  },
  "face_validation": null,
  "analysis": {
    "summary": "Resumo do contrato...",
    "risk_level": "low",
    "recommendations": ["..."],
    "is_valid_contract": true,
    "confidence": 89.2
  },
  "processed_at": "2024-01-15T10:30:00",
  "message": "Contract analysis completed successfully"
}
```

## Formatos Suportados

**Documentos:**
- PNG
- JPEG
- PDF (1 página)

**Imagem facial (opcional):**
- PNG
- JPEG

## Docker

```bash
docker-compose up --build
```

## Configuração AWS

### Permissões necessárias

O usuário IAM precisa das seguintes políticas:
- `AmazonTextractFullAccess`
- `AmazonRekognitionFullAccess`
- `AmazonBedrockFullAccess`

### Região

O projeto está configurado para `us-east-1`. Para alterar, modifique a variável `AWS_REGION`.

## Arquitetura

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Presentation  │────▶│   Application   │────▶│     Domain      │
│    (Routes)     │     │   (Use Cases)   │     │  (Interfaces)   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │ Infrastructure  │
                                               │  (AWS Services) │
                                               └─────────────────┘
```

## Princípios

- **SRP:** Cada classe tem uma única responsabilidade
- **DIP:** Use cases dependem de interfaces, não de implementações
- **OCP:** Fácil trocar implementações (mock ↔ AWS)
