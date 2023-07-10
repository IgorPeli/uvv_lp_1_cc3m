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

## Executando os Testes

Para executar os testes automatizados, execute o arquivo pset1_tests.py presente neste diretório. Certifique-se de que o pacote unittest esteja instalado no ambiente Python. Os testes irão verificar a corretude das implementações e exibir os resultados no console.  

Caso queira executar individualmente cada grupo de testes, você pode descomentar a seção correspondente ao grupo de testes desejado no final do arquivo pset1.py e executá-lo separadamente. 

## Diretório de Testes

Os testes utilizam imagens localizadas no diretório test_images para verificar os resultados das operações. Os resultados esperados são armazenados no diretório test_results. Certifique-se de que os arquivos de imagem estejam presentes nesses diretórios antes de executar os testes.  

## Diretório de Imagens de Entrada

As imagens de entrada utilizadas nos testes estão localizadas no diretório test_images. Para utilizar suas próprias imagens de entrada, coloque-as neste diretório e faça as modificações necessárias nos testes.  

## Diretório de Resultados Esperados

Os resultados esperados das operações são armazenados no diretório test_results. Para adicionar novos casos de teste, adicione as imagens de resultado esperado neste diretório e atualize os testes correspondentes para comparar com os resultados obtidos.  

## Requisitos

    Python 3.5 ou superior
    Bibliotecas: os, pset1, unittest
