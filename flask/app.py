from typing import List, Dict
from flask import Flask
import mysql.connector
import json


app = Flask(__name__)

def modulos() -> str:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'pfa'
    }
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # mycursor.execute("CREATE TABLE IF NOT EXISTS modulos (id int PRIMARY KEY AUTO_INCREMENT, nome varchar(255));")

    # mycursor.execute("INSERT INTO cursos (nome) VALUES ('Docker'), ('Git e GitHub'), ('Kubernetes'), ('Terraform'), ('Apache Kafka'), ('RabbitMQ');")

    select_query = "SELECT nome FROM modulos"
    cursor.execute(select_query)
    # modulos = cursor.fetchall()
    modulos = [nome for nome in cursor]
    print (modulos)
    linhas = ['<tr><td>' + ''.join(modulo) + '</td></tr>' for modulo in modulos]

    pagina = '<style> \
                    table, th, td {border: 1px solid black;} \
                </style> \
                <h1>Nome dos módulos do curso FullCycle</h1> \
                <table> \
                    <tr> \
                        <th> Nome do módulo </th> \
                    </tr>' \
                        + ''.join(linhas) + \
                '</table>'
    
    cursor.close()
    conn.close()
    
    return pagina
    


# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/pfa'

# db = SQLAlchemy(app)

# class Modulo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(255))

#     def to_json(self):
#         return {"id": self.id, "nome": self.nome}

@app.route('/', methods=['GET'])
def full_cycle_rocks() -> str:
    # modulos = Modulo.query.all()
    # modulos_json = [modulos.to_json() for modulo in modulos]
    
    # return Response(modulos_json)
    return modulos()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)