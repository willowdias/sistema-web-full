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
cliente.query('SELECT nome FROM usuario', (err,res)=>{
    if(!err){
        console.log(res.rows)
    }
    cliente.end()
})
