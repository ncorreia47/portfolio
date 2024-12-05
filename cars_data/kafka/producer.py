# from kafka import KafkaProducer
from faker import Faker
from faker_education import SchoolProvider
from faker_vehicle import VehicleProvider
from faker_music import MusicProvider
import json
import time

# Configuração do Faker
fake = Faker()
fake.add_provider(MusicProvider)
fake.add_provider(VehicleProvider)
fake.add_provider(SchoolProvider)

# Função para gerar dados fictícios
def generate_fake_data():
    return {
        "nome": fake.name(),
        "endereco": fake.address(),
        "email": fake.email(),
        "telefone": fake.phone_number(),
        "cpf": fake.ssn(),
        "data_nascimento": fake.date_of_birth(),
        "genero": fake.random_element(["Masculino", "Feminino", "Outro"]),
        "profissao": fake.job(),
        "empresa": fake.company(),
        "cargo": fake.job(),
        "cidade": fake.city(),
        "estado": fake.state(),
        "pais": fake.country(),
        "cep": fake.zipcode(),
        "genero_musica": fake.music_genre(),
        "escolaridade": fake.school_level(),
        "classificacao_escola": fake.school_type(),
        "marca": fake.vehicle_make(),
        "modelo": fake.vehicle_model(),
        "ano": fake.vehicle_year(),
        "placa": fake.license_plate(),
        "vin": fake.vin(),
        "categoria": fake.vehicle_category()
    }
"""
# Configuração do Kafka
producer = KafkaProducer(
    bootstrap_servers='kafka:9093',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Nome do tópico no Kafka
topic = 'test_topic'

# Enviando dados fictícios para o Kafka
while True:
    fake_data = generate_fake_data()
    print(f"Sending data: {fake_data}")
    producer.send(topic, fake_data)
    time.sleep(2)  # Envia uma nova mensagem a cada 2 segundos """
