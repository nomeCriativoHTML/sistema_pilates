// Navegação entre abas
document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => {
        // Remove classe ativa de todas as abas
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('ativo'));
        // Remove classe ativa de todos os formulários
        document.querySelectorAll('.formulario').forEach(f => f.classList.remove('ativo'));
        
        // Adiciona classe ativa na aba clicada
        tab.classList.add('ativo');
        
        // Mostra o formulário correspondente
        const formId = `form-${tab.dataset.tab}`;
        document.getElementById(formId).classList.add('ativo');
    });
});

// Botão voltar
document.querySelector('.btn-voltar').addEventListener('click', () => {
    window.history.back();
});

// Botão cancelar
document.querySelectorAll('.cancelar').forEach(btn => {
    btn.addEventListener('click', () => {
        if (confirm('Deseja cancelar o cadastro? Os dados não salvos serão perdidos.')) {
            window.location.href = '/home';
        }
    });
});

// Formulário Aluno
document.getElementById('form-aluno').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    
    try {
        const response = await fetch('/alunos/cadastro/aluno', {
            method: 'POST',
            body: formData
        });
        
        if (response.ok) {
            alert('Aluno cadastrado com sucesso!');
            this.reset(); // Limpa o formulário
        } else {
            alert('Erro ao cadastrar aluno. Tente novamente.');
        }
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao cadastrar aluno. Verifique sua conexão.');
    }
});

// Máscara de telefone
function mascaraTelefone(telefone) {
    const texto = telefone.value.replace(/\D/g, '');
    const regex = /^(\d{2})(\d{5})(\d{4})$/;
    
    if (regex.test(texto)) {
        telefone.value = texto.replace(regex, '($1) $2-$3');
    }
}

document.querySelectorAll('input[type="tel"]').forEach(input => {
    input.addEventListener('input', (e) => mascaraTelefone(e.target));
});

// Verificar parâmetros da URL para mensagens
document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    
    if (urlParams.has('success')) {
        alert('Aluno cadastrado com sucesso!');
        // Limpa a URL
        window.history.replaceState({}, document.title, window.location.pathname);
    }
    
    if (urlParams.has('error')) {
        const error = urlParams.get('error');
        alert(`Erro: ${error}`);
        // Limpa a URL
        window.history.replaceState({}, document.title, window.location.pathname);
    }
});