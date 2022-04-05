
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


function cadastrocliente(){
    document.getElementById('cadastro-cliente').style.display='block';
    document.getElementById('Lancamento').style.display='none';
}
function fechas(){
    document.getElementById('cadastro-cliente').style.display='none';
    alert("Fechado" );
}

function lancamento(){
    document.getElementById('Lancamento').style.display='block';
    document.getElementById('cadastro-cliente').style.display='none';
}


function tablecliente(){
    alert("willow")
   cadastrocliente()

}

function connect()
{
    
        alert("Login    " +login);
        

 }
 function cadastrodirect(){
        document.getElementById('id02').style.display='block';
        document.getElementById('login').style.display='none';
    }
function closelp(){ 
        document.getElementById('id02').style.display='none';
        document.getElementById('login').style.display='block';
 }