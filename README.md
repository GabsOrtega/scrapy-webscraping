#COMO RODAR O PROJETO?

1 - Instale o ambiente virytual com pip:

pip install virtualenv

2 - Crie um ambiente virtual na máquina:

virtualenv venv

3 - Entre no ambiente virtual:

source venv/bin/activate (Linux ou MacOS)

venv/Scripts/Activate (Windows)

4 - Instale todas as dependências da aplicação:

pip install -r requirements.txt

5 - Para rodar o spider e transformar os dados em um arquivo:

scrapy crawl leiloes -O NOMEARQUIVO.extensao

Ex:

scrapy crawl leiloes -O leiloes.json

scrapy crawl leiloes -O leiloes.csv
