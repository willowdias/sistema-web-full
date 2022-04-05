import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='', host='127.0.0.1', port=3306)

# Descomente se quiser desfazer o banco...
conn.cursor().execute("DROP DATABASE `lojaoff`;")
conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `lojaoff` ;
    USE `lojaoff`;
   CREATE TABLE `clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
   CREATE TABLE `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) NOT NULL,
  `senha` varchar(50) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome` (`nome`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO lojaoff.usuario ( nome, senha,email) VALUES (%s, %s,%s)',
      [
            ('willow', '2020',"willow18282@gmail.com")
           
      ])

cursor.execute('select * from lojaoff.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])
#tabela clientes
cursor.executemany(
      'INSERT INTO lojaoff.clientes ( nome, cpf,endereco, cidade, estado,  numero, obs_cliente) VALUES (%s,%s,%s,%s,%s,%s,%s)',
      [
            ('willow', '03566856240','rua osmar','urupa','ro','69','bem vindo brasil')
           
      ])

cursor.execute('select * from lojaoff.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])
conn.commit()
cursor.close()