btnBusca=document.getElementById('busca')

function buscaTexto(){
console.log(btnBusca.value)
}

btnBusca.addEventListener('keyup',buscaTexto)