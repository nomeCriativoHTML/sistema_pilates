const forms = document.querySelectorAll('.formulario'); // pega todos os formulários
const tabs = document.querySelectorAll('.tab');


forms.forEach(form => {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    alert("Cadastro salvo com sucesso!");
  });
});


document.querySelectorAll('.btn.cancelar').forEach(btn => {
  btn.addEventListener('click', () => {
    window.location.href = "admin.html"; 
  });
});

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
   
    tabs.forEach(t => t.classList.remove('ativo'));
    forms.forEach(f => f.classList.remove('ativo'));

    
    tab.classList.add('ativo');

   
    const formId = `form-${tab.dataset.tab}`;
    document.getElementById(formId).classList.add('ativo');
  });
});
