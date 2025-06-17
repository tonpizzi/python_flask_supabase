# Python Flask Supabase

Uma aplicação web simples utilizando o framework Flask para demonstrar a integração com o [Supabase](https://supabase.com/).  
Esta aplicação busca dados de uma tabela do Supabase (por exemplo, `stock_current`) e os exibe em formato de tabela em uma página web.

## Visão Geral

O projeto foi criado para exemplificar como desenvolver APIs e aplicações web com Flask e consumir dados de um banco de dados via Supabase.  
É uma ótima base para quem deseja desenvolver projetos em Flask que necessitam de um backend escalável e com autenticação, armazenamento e outras funcionalidades prontas.

## Funcionalidades

- Integração com o Supabase para consulta de dados.
- Exibição dos dados em uma tabela HTML utilizando template Jinja2.
- Demonstração de boas práticas na estruturação de uma aplicação Flask simples.

## Requisitos

- Python 3.7 ou superior
- [Pipenv](https://pipenv.pypa.io/) ou [virtualenv](https://virtualenv.pypa.io/) (opcional, mas recomendado)
- Conta no [Supabase](https://supabase.com/) com uma instância configurada e uma tabela (`stock_current` ou outra de sua preferência)

## Instalação

1. **Clone o repositório**

   ```bash
   git clone https://github.com/tonpizzi/python_flask_supabase.git
   cd python_flask_supabase
