
import pymysql
#new-password
conexao = pymysql.connect(db='lojaoff', user='root', passwd='')

cursor = conexao.cursor()

'''cursor.executeCREATE TABLE `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) NOT NULL,
  `senha` varchar(50) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome` (`nome`),
  UNIQUE KEY `email` (`email`)
)'''
'''CREATE TABLE `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) NOT NULL,
   `cpf` varchar(14) DEFAULT NULL,
   `endereco` varchar(50) NOT NULL,
   `cidade` varchar(100) NOT NULL,
   `estado` varchar(2) NOT NULL,
 `numero` int(20) NOT NULL,
 `obs_cliente` varchar(5000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome` (`nome`),
  UNIQUE KEY `email` (`cpf`)
)'''
#cursor.execute("INSERT INTO usuario (nome, senha, email) VALUES ('willow','2020','willow@gmail.com' )")
cursor.execute("INSERT INTO clientes (nome, cpf,endereco, cidade, estado,  numero, obs_cliente) VALUES ('will3331','3330','rua urpa','ururpa','RO','4548','OK VAMO LA' )")
#cursor.execute(f"DELETE FROM clientes WHERE id = '1'")
conexao.commit()
#cursor.execute("UPDATE tb_cidades SET cidade =LOWER (cidade)")
cursor.execute("SELECT *from usuario")
resultado = cursor.fetchall()


for linha in resultado :
    print(linha)

conexao.close()