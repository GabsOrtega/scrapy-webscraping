<h2>COMO RODAR O PROJETO?</h2>

<ol><li>Instale o ambiente virytual com pip:</li>

pip install virtualenv

<li>Crie um ambiente virtual na máquina:</li>

virtualenv venv

<li>Entre no ambiente virtual:</li>

source venv/bin/activate (Linux ou MacOS)

venv/Scripts/Activate (Windows)

<li>Instale todas as dependências da aplicação:</li>

pip install -r requirements.txt

<li>Para rodar o spider e transformar os dados em um arquivo:</li>

scrapy crawl leiloes -O NOMEARQUIVO.extensao

Ex:

scrapy crawl leiloes -O leiloes.json

scrapy crawl leiloes -O leiloes.csv
</ol>
