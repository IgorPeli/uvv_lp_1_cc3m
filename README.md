# Pset 1
Aluno: Igor Peli Resende  
Turma: CC3M  
Professor: Abrantes Araújo Silva Filho  

# Descrição:
Este PSET é uma tradução da primeira tarefa de programação que os alunos da
disciplina “MIT 6.009: Fundamentals of Programming” recebem logo no primeiro
dia de aula, feita para os alunos da disciplina “Linguagens de Programação” na
Universidade Vila Velha (UVV).

uncionalidades implementadas

### A classe Imagem possui os seguintes métodos:
- **get_pixel(x, y)**: retorna o valor do pixel nas coordenadas (x, y) da imagem.  
- **set_pixel(x, y, c)**: define o valor do pixel nas coordenadas (x, y) como c.  
- **aplicar_por_pixel(func)**: aplica uma função fornecida a cada pixel da imagem e retorna uma nova imagem resultante.  
- **invertida()**: retorna uma nova imagem invertendo as cores da imagem atual.  
- **relacao(n)**: aplica uma operação de convolução utilizando um kernel fornecido na imagem atual e retorna uma nova imagem resultante.  
- **borrada(n)**: retorna uma nova imagem borrada utilizando um kernel gerado a partir de uma função de kernel.  
- **focada(n)**: retorna uma nova imagem resultante da operação de nitidez aplicada à imagem atual.  
- **bordas()**: retorna uma nova imagem realçando as bordas da imagem atual utilizando o operador Sobel.  

## Utilização

Para utilizar a classe Imagem, basta criar uma instância da classe com a largura, altura e pixels da imagem desejada. Em seguida, é possível chamar os métodos disponíveis para realizar diferentes operações na imagem.  
No arquivo principal, há exemplos de utilização dos métodos da classe Imagem para executar diferentes operações em imagens de teste. Essas operações incluem inversão de cores, aplicação de convolução, desfoque, realce de nitidez e realce de bordas.

## Carregamento e salvamento de imagens

A classe Imagem também fornece métodos para carregar imagens a partir de arquivos e salvar imagens em disco. Os métodos carregar e salvar são utilizados para esse propósito. O método carregar lê uma imagem do arquivo fornecido e realiza a conversão para tons de cinza, enquanto o método salvar salva uma imagem no disco em um formato especificado.  

## Execução e testes

O código pode ser executado diretamente para realizar as operações descritas nos exemplos do arquivo principal. Para executar o código, é necessário ter uma instalação do Python 3 e as bibliotecas PIL e tkinter instaladas.  

Além disso, o repositório contém testes automatizados para verificar o correto funcionamento da classe Imagem. Os testes estão localizados em um arquivo separado e podem ser executados para verificar se as funcionalidades estão implementadas corretamente.  
