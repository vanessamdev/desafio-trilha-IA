const API_URL = 'http://localhost:8000/api/v1';

const form = document.getElementById('analysis-form');
const submitBtn = document.getElementById('submit-btn');
const loading = document.getElementById('loading');
const result = document.getElementById('result');
const resultContent = document.getElementById('result-content');
const error = document.getElementById('error');
const errorMessage = document.getElementById('error-message');

const documentInput = document.getElementById('document');
const faceInput = document.getElementById('face-image');
const documentInfo = document.getElementById('document-info');
const faceInfo = document.getElementById('face-info');

documentInput.addEventListener('change', () => {
    documentInfo.textContent = documentInput.files[0]?.name || 'Nenhum arquivo selecionado';
});

faceInput.addEventListener('change', () => {
    faceInfo.textContent = faceInput.files[0]?.name || 'Nenhum arquivo selecionado';
});

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const documentFile = documentInput.files[0];
    const faceFile = faceInput.files[0];
    
    if (!documentFile || !faceFile) {
        showError('Selecione ambos os arquivos');
        return;
    }
    
    const formData = new FormData();
    formData.append('document', documentFile);
    formData.append('face_image', faceFile);
    
    showLoading();
    
    try {
        const response = await fetch(`${API_URL}/analyze-contract`, {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Erro ao processar análise');
        }
        
        const data = await response.json();
        showResult(data);
    } catch (err) {
        showError(err.message);
    }
});

function showLoading() {
    submitBtn.disabled = true;
    loading.classList.remove('hidden');
    result.classList.add('hidden');
    error.classList.add('hidden');
}

function hideLoading() {
    submitBtn.disabled = false;
    loading.classList.add('hidden');
}

function showError(message) {
    hideLoading();
    error.classList.remove('hidden');
    result.classList.add('hidden');
    errorMessage.textContent = message;
}

function showResult(data) {
    hideLoading();
    result.classList.remove('hidden');
    error.classList.add('hidden');
    
    resultContent.innerHTML = `
        <div class="result-section">
            <h3>Informações Gerais</h3>
            <div class="result-item">
                <span class="result-label">ID da Requisição</span>
                <span class="result-value">${data.request_id}</span>
            </div>
            <div class="result-item">
                <span class="result-label">Status</span>
                <span class="result-value ${data.status === 'success' ? 'status-valid' : 'status-invalid'}">${data.status}</span>
            </div>
            <div class="result-item">
                <span class="result-label">Documento</span>
                <span class="result-value">${data.document_filename}</span>
            </div>
            <div class="result-item">
                <span class="result-label">Processado em</span>
                <span class="result-value">${new Date(data.processed_at).toLocaleString('pt-BR')}</span>
            </div>
        </div>
        
        ${renderDocumentData(data.document_data)}
        ${renderFaceValidation(data.face_validation)}
        ${renderAnalysis(data.analysis)}
    `;
}

function renderDocumentData(data) {
    if (!data) return '';
    
    return `
        <div class="result-section">
            <h3>Dados do Documento</h3>
            <div class="result-item">
                <span class="result-label">Confiança</span>
                <span class="result-value">${data.confidence.toFixed(1)}%</span>
            </div>
            <div class="result-item">
                <span class="result-label">Páginas</span>
                <span class="result-value">${data.pages_count}</span>
            </div>
            <div class="result-item">
                <span class="result-label">Texto Extraído</span>
                <span class="result-value">${data.raw_text.substring(0, 100)}...</span>
            </div>
        </div>
    `;
}

function renderFaceValidation(data) {
    if (!data) return '';
    
    return `
        <div class="result-section">
            <h3>Validação Facial</h3>
            <div class="result-item">
                <span class="result-label">Válido</span>
                <span class="result-value ${data.is_valid ? 'status-valid' : 'status-invalid'}">${data.is_valid ? 'Sim' : 'Não'}</span>
            </div>
            <div class="result-item">
                <span class="result-label">Confiança</span>
                <span class="result-value">${data.confidence.toFixed(1)}%</span>
            </div>
            <div class="result-item">
                <span class="result-label">Faces Detectadas</span>
                <span class="result-value">${data.faces_detected}</span>
            </div>
            <div class="result-item">
                <span class="result-label">Mensagem</span>
                <span class="result-value">${data.message}</span>
            </div>
        </div>
    `;
}

function renderAnalysis(data) {
    if (!data) return '';
    
    const riskClass = `risk-${data.risk_level}`;
    
    return `
        <div class="result-section">
            <h3>Análise</h3>
            <div class="result-item">
                <span class="result-label">Contrato Válido</span>
                <span class="result-value ${data.is_valid_contract ? 'status-valid' : 'status-invalid'}">${data.is_valid_contract ? 'Sim' : 'Não'}</span>
            </div>
            <div class="result-item">
                <span class="result-label">Nível de Risco</span>
                <span class="result-value ${riskClass}">${data.risk_level.toUpperCase()}</span>
            </div>
            <div class="result-item">
                <span class="result-label">Confiança</span>
                <span class="result-value">${data.confidence.toFixed(1)}%</span>
            </div>
            <div class="result-item">
                <span class="result-label">Resumo</span>
                <span class="result-value">${data.summary}</span>
            </div>
            <div class="result-item" style="flex-direction: column; gap: 0.5rem;">
                <span class="result-label">Recomendações</span>
                <ul class="recommendations">
                    ${data.recommendations.map(r => `<li>${r}</li>`).join('')}
                </ul>
            </div>
        </div>
    `;
}
