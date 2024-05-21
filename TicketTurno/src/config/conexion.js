const mysql = require('mysql');

// Configura las credenciales
const connection = mysql.createConnection({
  host: 'hostname',
  user: 'root',
  password: '1234',
  database: 'ticket',
  port: 3306
});

// Conectar a la base de datos
connection.connect((err) => {
  if (err) {
    console.error('Error en la conexión:', err.stack);
    return;
  }

  console.log('Conexión exitosa');
  
  // Puedes ejecutar consultas aquí
  connection.query('SELECT DATABASE()', (error, results, fields) => {
    if (error) throw error;
    console.log('Conectado a la base de datos:', results[0]['DATABASE()']);
  });

  // Cerrar la conexión
  connection.end();
});