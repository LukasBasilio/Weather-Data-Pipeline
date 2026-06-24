# 🌪️ Estudo Prático: Pipeline de Engenharia de Dados (Weather Data)

## 📋 Sobre o Projeto
Este repositório contém o código desenvolvido durante o meu estudo prático de Engenharia de Dados. O objetivo foi replicar um pipeline de dados funcional do zero para entender o ciclo de vida do processo de ETL, isolamento de ambientes e orquestração de tarefas.

> 🎓 **Créditos e Referência:** Este projeto foi totalmente baseado e desenvolvido acompanhando o tutorial prático do canal **VB Luíza** (Engenheira de Dados). A replicação deste código serviu como laboratório pessoal para consolidar conceitos teóricos de computação na prática.

---

## 🏗️ Arquitetura do Pipeline
O fluxo de dados segue o modelo clássico ETL (Extract, Transform, Load):
1. **Extração:** Consumo de dados climáticos em tempo real via requisição HTTP para a API do OpenWeatherMap.
2. **Transformação:** Limpeza dos dados, normalização de estruturas aninhadas (JSON) e conversão de timestamps Unix para datetime com o fuso horário correto utilizando Python e Pandas.
3. **Carga:** Armazenamento dos dados tratados em uma tabela estruturada no banco de dados PostgreSQL.
4. **Orquestração:** Todo o fluxo é automatizado por uma DAG dentro do Apache Airflow rodando em containers Docker.

---

## 🧠 Principais Aprendizados e Desafios
Desenvolver este projeto me trouxe aprendizados práticos que vão muito além da teoria da faculdade:
* **Gerenciamento de Variáveis de Ambiente:** Uso prático de arquivos `.env` para proteger chaves de API (`API Key`) e credenciais de banco de dados, evitando exposição de dados sensíveis no GitHub.
* **Manipulação de Caminhos com Pathlib:** Entendimento profundo sobre a diferença de caminhos relativos e absolutos no sistema operacional ao estruturar pastas de scripts.
* **Isolamento com Docker e Airflow:** Entendi como o Airflow funciona de forma rígida dentro de um container e como registrar manualmente o caminho das pastas (`sys.path.insert`) para que o container enxergue as funções Python locais.
* **TaskFlow API:** Uso moderno de decoradores do Airflow (`@dag` e `@task`) para definir dependências de execução de forma limpa.

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem Principal:** Python 3.12+
* **Manipulação e Análise:** Pandas, JSON e Pathlib
* **Banco de Dados:** PostgreSQL 14+
* **Orquestrador:** Apache Airflow
* **Infraestrutura:** Docker & Docker Compose
* **Gerenciador de Pacotes:** UV

---

## 📂 Estrutura do Projeto
* `src/`: Contém os scripts modulares de execução do pipeline (`extract_data.py`, `transform_data.py`, `load_data.py`).
* `dags/`: Onde fica armazenada a DAG (`weather_dag.py`) que o Airflow lê para rodar o pipeline.
* `config/`: Pasta que armazena as configurações locais e o arquivo `.env` com as credenciais.
* `notebooks/`: Arquivos Jupyter Notebook utilizados para a análise exploratória inicial do JSON da API.

---

## 🚀 Como Executar o Projeto Localmente
1. Certifique-se de ter o **Python**, o **Docker Desktop** e o **WSL2** instalados e rodando.
2. Crie uma conta gratuita no OpenWeatherMap e gere sua API Key.
3. Clone este repositório para a sua máquina.
4. Crie o arquivo `config/.env` e preencha com as suas credenciais do Postgres e a sua chave da API de clima.
5. Suba a infraestrutura do Airflow com o comando:
   ```bash
   docker compose up -d