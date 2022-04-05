const mysql = require('mysql')
const express = require("express");

const app= express()


const connection= mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"new-password",
    database:"lojaoff"
});
//connecta data base
connection.connect(function(erro){
    if (erro) throw erro
    else console.log("connect sistema com sucesso")
})

app.get("/",function(req,res){
    res.sendFile(__dirname +"/templades/login.html");
    
})

app.listen(4500)