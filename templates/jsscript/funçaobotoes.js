const {Client} = require('pg')

const cliente = new Client(
    {
       host:"localhost",
       user:"postgres",
       port:5432,
       password:"123456",
       database:"db_sistema"
    }
)

cliente.connect();
cliente.query('SELECT * FROM usuario', (err,res)=>{
    if(!err){
        console.log(res.rows);
    }else{
        console.log(err.message);
    }
    cliente.end;
})
function connect()
{
    var login = document.getElementById("login").value;
    var senha = document.getElementById("senha").value;
    if(login=="admin" && senha=="admin"){
        alert("Login    " +login);
        document.getElementById('login').value='';
        window.location="index.html"; done=1;

    }
        
        
    else{
        document.getElementById('erro=login').innerHTML = "Login Incorreto";
        document.getElementById('login').value='';
        document.getElementById('senha').value='';
        alert("Erro login ",{
            label:"OK",
            success:function () {
                  console.log("User clicked YES");
                
                }
                   
        }
        );
        
        
        

    }
}        

function logindirect(){
    document.getElementById('id01').style.display='block';
    document.getElementById('id02').style.display='none';
}
function cadastrodirect(){
    document.getElementById('id02').style.display='block';
    document.getElementById('id01').style.display='none';
}

// Change the type of input to password or text
function Toggle() {
    var ver = document.getElementById("senha");
    if (ver.type === "password") {
        ver.type = "text";
    }
    else {
        ver.type = "password";
    }
}
function visualizarsenha() {
    var ver = document.getElementById("senhacadastro");
    if (ver.type === "password") {
        ver.type = "text";
    }
    else {
        ver.type = "password";
    }
}