CREATE DATABASE pfa;

use pfa;

CREATE TABLE modulos (
    id int PRIMARY KEY AUTO_INCREMENT,
    nome varchar(255)
);

INSERT INTO modulos (nome)
VALUES 
    ('Docker'),
    ('Git e GitHub'),
    ('Kubernetes'),
    ('Terraform'),
    ('Apache Kafka'),
    ('RabbitMQ');
