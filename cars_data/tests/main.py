import os
import sys

# Adiciona o diretório raiz ao sys.path para garantir que módulos sejam importados corretamente
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

# Altera o diretório de trabalho para a pasta raiz do projeto
os.chdir(project_root)

from kafka.producer import generate_fake_data as gen


print(gen())