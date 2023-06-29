import scrapy


class LeiloesSpider(scrapy.Spider):
    name = "leiloes"
    start_urls = ["https://agostinholeiloes.com.br/item/1435/detalhes?page=1"]

    def parse(self, response):
        yield {
        'titulo': response.css('.px-1 h4:nth-child(2)::text').get(),
        'Valor de avaliação': response.css('.m-0:nth-child(5)::text').get(),
        'Data da Primeira Praça': response.css('.m-0:nth-child(7)::text').get(),
        'Valor da Segunda Praça': response.css('.m-0:nth-child(10)::text').get(),
        'Endereço': response.css('.mb-3.p-2.border.rounded>p::text').getall()[3],
        'Link de uma imagem': response.css('.img-cover::attr(style)').get().split()[1][5:-2],
        'Link de um documento': response.css('.btn-block.btn-outline-secondary::attr(href)').get()
        }
