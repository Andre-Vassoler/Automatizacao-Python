## 📌 Automação com Python

Projeto de automação desenvolvido em Python para realizar cadastros automáticos de produtos em um sistema web, utilizando leitura de dados de uma planilha CSV e automação de cliques e preenchimentos na tela.

## 📁 Estrutura do Projeto
- automacao.py – código principal com os comandos de automação (cliques, digitação e cadastro dos produtos).

- auxiliar.py – script utilizado para capturar a posição do mouse na tela, auxiliando na definição dos pontos de clique da automação.

- produtos.csv – arquivo CSV contendo a lista de produtos que serão cadastrados automaticamente no sistema.

## ⚙️ Requisitos (Recomendado)

- Antes de executar o projeto, instale:

- Python 3.10 ou superior

- Extensão do Python (VS Code)

- Extensão para visualização/manipulação de arquivos CSV

- Bibliotecas necessárias:

    pip install pyautogui pandas

## 📝 Descrição

Este projeto realiza uma automação utilizando Python para:

- Abrir o navegador automaticamente

- Acessar um site de testes

- Realizar login automático

- Ler uma tabela de produtos (produtos.csv)

- Cadastrar automaticamente cada produto no sistema

O script principal usa a biblioteca pyautogui para controlar o mouse e teclado, e pandas para leitura da planilha CSV.

## ⚠️ Avisos Importantes

- O site utilizado é apenas para testes e pode não estar mais disponível.

- O projeto foi desenvolvido e testado no Windows. Em Linux ou MacOS podem ocorrer erros.

- A automação depende da posição dos elementos na tela. Caso a resolução do seu monitor seja diferente, os cliques podem ocorrer em locais incorretos.

- Utilize o arquivo auxiliar.py para descobrir as posições corretas do mouse antes de rodar a automação.

O MEU COMPUTADOR É UM POUCO LENTO E TRAVA, ENTÃO, SE QUISER, PODE DIMINUIR O TEMPO ENTRE AS AÇÕES

pyautogui.PAUSE = 2 (2 segundos, pode diminuir)
