# Calculadora com interface em phyton

Este é um programa de calculadora desenvolvido em Python, utilizando a biblioteca Tkinter para criar a interface gráfica. A calculadora permite realizar operações básicas como adição, subtração, multiplicação e divisão, além de operações como mudança de sinal e porcentagem.

## Como executar o programa

1. Certifique-se de ter o Python instalado em seu vscode.
2. Para executar o programa, siga os seguintes passos:
   
   1. Baixe o arquivo contendo o código fornecido (por exemplo, `calculadora.py`).
   
   2. No terminal ou prompt de comando, navegue até o diretório onde o arquivo está localizado.
   
   3. Execute o seguinte comando:
      ```bash
      python calculadora.py
      ```

3. A calculadora será aberta em uma janela gráfica.

## Principais funcionalidades

- **Teclas numéricas (0-9):** permitem inserir os números para realizar operações.
- **Operadores (+, -, *, /):** permitem realizar as operações aritméticas básicas.
- **Botão de limpar (C):** limpa todas as expressões da calculadora.
- **Botão de porcentagem (%):** calcula a porcentagem do valor atual.
- **Botão de mudar sinal (+/-):** inverte o sinal do número atual.
- **Botão de igual (=):** realiza o cálculo da expressão atual.

## Principais decisões de design

1. **Organização da interface:**
   - A calculadora é composta por dois frames principais: um para exibir os números e outro para os botões.
   - O display da calculadora possui dois labels: uma para exibir a expressão total e outra para mostrar o número atual.

2. **Estilização parecida com a calculadora do iphone:**
   - Foi utilizado um esquema de cores que lembra calculadoras dos dispositivos iphone. Botões numéricos e de operações especiais têm cores diferenciadas para melhor usabilidade.
   - Cores escuras para o fundo (`#000000`) com texto claro (`#FFFFFF`) foram usadas para criar um contraste que facilita a leitura dos valores no display.

3. **Funções de operações especiais:**
   - Implementação de funcionalidades como `mudar_sinal`, que inverte o valor do número atual, e `porcentagem`, que transforma o número atual em uma porcentagem, para oferecer mais funcionalidades além das operações básicas.

4. **Tratamento de erros:**
   - A função `calcular` utiliza a função `eval` para avaliar a expressão matemática, com um bloco `try-except` para capturar possíveis erros e exibir "Erro" no display em caso de entrada inválida.

## Possíveis melhorias

- Adicionar suporte para teclas do teclado para permitir a interação sem o mouse.
- Melhorar a validação das expressões para prevenir erros de entrada antes da avaliação.
- Implementar mais operações, como raízes quadradas ou expoentes.

## Dependências

- **Tkinter**: biblioteca padrão do Python para criação de interfaces gráficas.
