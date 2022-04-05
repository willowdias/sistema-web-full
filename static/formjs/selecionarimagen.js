function telacadastro(){
    document.getElementById('cadastro-cliente').style.display='block';
}

function fecharcadastro(){

document.getElementById('cadastro-cliente').style.display='none';
}

"launch"
function openlaunch(){
    document.getElementById('container-Lancamento').style.display='block';


}
function closelaunch(){
    document.getElementById('container-Lancamento').style.display='none';
    

}
"table clientes"
function opentableclientes(){
    document.getElementById("fundo-table").style.display="block";
}

"aba cadastro clientes"
function cadastrarcliente(){
var nome = document.getElementById("nome-cd").value;
var sobrenome = document.getElementById("sobre-nome").value;
if(nome=="" & sobrenome=="" ){
    document.getElementById("ex1").style.display="block";
    document.getElementById('nome-cd').value='';
    document.getElementById('erro').textContent='Campos  Em Branco';
    
 }
 else{
    document.getElementById("ex1").style.display="block";
    document.getElementById('erro').textContent='Cadastro Com Sucesso';
    
 }
    
}
" alerta cliente"
function closealerta(){
    document.getElementById("ex1").style.display="none"
    
}
"Cliente excluidor" 
function  excluir(){
    document.getElementById("clientexcluido").style.display="block"
    
    
}
function selecionarimagen(){
    
    let photo = document.getElementById('imgPhoto');
    let file = document.getElementById('flImage');
    
    photo.addEventListener('click', () => {
        file.click();
        
    });
    var uploadfoto = document.getElementById('flImage');
    var fotopreview = document.getElementById('imgPhoto');
    
    uploadfoto.addEventListener('change', function(e) {
        showThumbnail(this.files);
    });
    
    function showThumbnail(files) {
        if (files && files[0]) {
        var reader = new FileReader();
    
        reader.onload = function (e) {
           fotopreview.src = e.target.result;
        }
    
            reader.readAsDataURL(files[0]);
        }
    }
}
