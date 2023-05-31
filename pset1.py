# IDENTIFICAÇÃO DO ESTUDANTE:
# Preencha seus dados e leia a declaração de honestidade abaixo. NÃO APAGUE
# nenhuma linha deste comentário de seu código!
#
#    Nome completo: Igor Peli Resende   
#    Matrícula: 202202232   
#    Turma: CC3M
#    Email: igor.peli.resende@gmail.com
#
# DECLARAÇÃO DE HONESTIDADE ACADÊMICA:
# Eu afirmo que o código abaixo foi de minha autoria. Também afirmo que não
# pratiquei nenhuma forma de "cola" ou "plágio" na elaboração do programa,
# e que não violei nenhuma das normas de integridade acadêmica da disciplina.
# Estou ciente de que todo código enviado será verificado automaticamente
# contra plágio e que caso eu tenha praticado qualquer atividade proibida
# conforme as normas da disciplina, estou sujeito à penalidades conforme
# definidas pelo professor da disciplina e/ou instituição.
#


# Imports permitidos (não utilize nenhum outro import!):
import sys
import math
import base64
import tkinter
from io import BytesIO
from PIL import Image as PILImage


#Definindo a matématica de Kernel.
def FuncKernel(n):
    kernel = [[1/n**2 for index in range(n)]for index in range(n)]
    return kernel

# Classe Imagem:
class Imagem:
    def __init__(self, largura, altura, pixels):
        self.largura = largura
        self.altura = altura
        self.pixels = pixels

    def get_pixel(self, x, y):
        if x < 0:     
            # O é o tamanho mínimo da imagem.
            x = 0
            # Então caso ele for menor que 0, ele vai ser ajustado para 0.
        elif x >= self.largura:
        # Se a quantidade de X(vertical) for maior que o tamanho da imagem, vai ser self.largura -1    
            x = self.largura - 1
            # -1 porque as colunas são enumeradas a patir do 0, ou seja, se tem tamanho de 10 pixels, vai ate 9, então por isso tem que ser 10-1.
            # Assim acessando o ultimo indice corretamente.

            # A mesma coisa de cima vale pro Y(horizontal).
        if y<0:
            y = 0
        elif y >= self.altura:
            y = self.altura - 1
        return self.pixels[(x+y*self.largura)]
        # Os pixels vão serão guardados em uma forma unidimensional, com essa matemática, eles serão guardados na ordem certa.
        # Exemplo: Imagem[2,2][10, 20, 30, 40]
        # posição do primeiro pixel(0,0): 0 + (0 * 2) = 0
        # posição do segundo  pixel(1,0): 1 + (0 * 2) = 1
        # posição do terceiro pixel(0,1): 0 + (1 * 2) = 2
        # posição do quarto pixel(1,1): 1 + (1 * 2) = 3
        
    def intpixel(self):
        for x in range(self.largura):
            for y in range(self.altura):
                inteiro = self.get_pixel(x, y)
                if inteiro < 0:
                    inteiro = 0
                elif inteiro > 255:
                    inteiro = 255
                inteiro = round(inteiro)
                # Round 
                self.set_pixel(x,y, inteiro)
    # Pixeis precisam ser inteiros, por isso essa funçãou com o Round.            

            
    def set_pixel(self, x, y, c):
        self.pixels[(x+y*self.largura)] = c
        # Mesma coisa do que no de cima.
        # A atribuição = c é usada para indicar que queremos atualizar o valor do pixel na posição (x, y) com o valor c fornecido.
        
    def aplicar_por_pixel(self, func):
        resultado = Imagem.nova(self.largura, self.altura)
        for x in range(resultado.largura):
            for y in range(resultado.altura):
                cor = self.get_pixel(x, y)
                nova_cor = func(cor)
                resultado.set_pixel(x, y, nova_cor)
                # é X, Y não Y, X
        return resultado
    
    def invertida(self):
        return self.aplicar_por_pixel(lambda c: 255 - c)
        # Não é 256, porque so vai até 255. Branco é 255. Cada pixel terá seu valor subtraido por 255, invertendo a cor.

    def relacao(self, n):
        kernel_tamanho = len(n)
        # Calcula o tamanho do kernel
        img = Imagem.nova(self.largura, self.altura)
        # Cria uma nova imagem vazia com a mesma largura e altura da imagem atual.
        for x in range(self.largura):
            for y in range(self.altura):
                # O método itera pelos pixels da imagem atual usando dois loops for aninhados: um loop para as coordenadas x e outro para as coordenadas y.
                relacaoSoma = 0
                # Inicializa uma variável relacaoSoma como zero. Essa variável será usada para armazenar a soma da multiplicação dos elementos do kernel com os valores dos pixels.
                for z in range(kernel_tamanho):
                    for w in range(kernel_tamanho):
                        # Outro conjunto de loops for aninhados é utilizado para percorrer os elementos do kernel. Os loops for têm a variável z para as linhas e a variável w para as colunas.
                        relacaoSoma += self.get_pixel((x-(kernel_tamanho//2)+z), (y-(kernel_tamanho//2))+w)*n[z][w]
                        # Dentro dos loops do kernel, o método realiza a multiplicação entre o valor do pixel na posição deslocada (x-(kernel_tamanho//2)+z, y-(kernel_tamanho//2)+w) 
                        # da imagem atual e o valor correspondente no kernel n[z][w]. Esses produtos são somados à variável relacaoSoma.
                        # TIVE QUE PESQUISAR BASTANTE.
                img.set_pixel(x, y, relacaoSoma)
                # Após a iteração completa do kernel, o valor de relacaoSoma é atribuído ao pixel correspondente (x, y) na nova imagem img.
        return img
        
    def borrada(self, n):
        kernel = self.relacao(FuncKernel(n))
        kernel.intpixel()
        return kernel

    def focada(self, n):
        borrado = self.borrada(n)
        img = Imagem.nova(self.largura, self.altura)
        for x in range(self.largura):
            for y in range (self.altura):
                # Subtração da foto normal(2) com uma foto borrada
                equacaoNitida = round(2*self.get_pixel(x,y)-(borrado.get_pixel(x,y)))
                img.set_pixel(x,y, equacaoNitida)
        img.intpixel()
        return img
        
    def bordas(self):
        img = Imagem.nova(self.largura, self.altura)
        operadorSobelX = [[1, 0, -1],
                         [2, 0, -2],
                         [1, 0, -1]]
        
        operadorSobelY = [[1, 2, 1],
                         [0, 0, 0],
                         [-1, -2, -1]]
        # De acordo com o Wikipedia que você passou, você colocou errado os operadores.
        SobelAplicadoX = self.relacao(operadorSobelX)
        SobelAplicadoY = self.relacao(operadorSobelY)
        for x in range(self.largura):
            for y in range(self.altura):
                sobelOperacao = round(math.sqrt(SobelAplicadoX.get_pixel(x,y)**2 + SobelAplicadoY.get_pixel(x,y)**2))
                # Matématica passada no pset, onde tira a Raiz da soma dos quadrados dos pixeis X e Y.
                img.set_pixel(x,y, sobelOperacao)
        img.intpixel()
        return img

    # Abaixo deste ponto estão utilitários para carregar, salvar e mostrar
    # as imagens, bem como para a realização de testes.

    def __eq__(self, other):
        return all(getattr(self, i) == getattr(other, i)
                   for i in ('altura', 'largura', 'pixels'))

    def __repr__(self):
        return "Imagem(%s, %s, %s)" % (self.largura, self.altura, self.pixels)

    @classmethod
    def carregar(cls, nome_arquivo):
        """
        Carrega uma imagem do arquivo fornecido e retorna uma instância dessa
        classe representando essa imagem. Também realiza a conversão para tons
        de cinza.

        Invocado como, por exemplo:
           i = Imagem.carregar('test_images/cat.png')
        """
        with open(nome_arquivo, 'rb') as guia_para_imagem:
            img = PILImage.open(guia_para_imagem)
            img_data = img.getdata()
            if img.mode.startswith('RGB'):
                pixels = [round(.299 * p[0] + .587 * p[1] + .114 * p[2]) for p in img_data]
            elif img.mode == 'LA':
                pixels = [p[0] for p in img_data]
            elif img.mode == 'L':
                pixels = list(img_data)
            else:
                raise ValueError('Modo de imagem não suportado: %r' % img.mode)
            l, a = img.size
            return cls(l, a, pixels)

    @classmethod
    def nova(cls, largura, altura):
        """
        Cria imagens em branco (tudo 0) com a altura e largura fornecidas.

        Invocado como, por exemplo:
            i = Imagem.nova(640, 480)
        """
        return cls(largura, altura, [0 for i in range(largura * altura)])

    def salvar(self, nome_arquivo, modo='PNG'):
        """
        Salva a imagem fornecida no disco ou em um objeto semelhante a um arquivo.
        Se o nome_arquivo for fornecido como uma string, o tipo de arquivo será
        inferido a partir do nome fornecido. Se nome_arquivo for fornecido como
        um objeto semelhante a um arquivo, o tipo de arquivo será determinado
        pelo parâmetro 'modo'.
        """
        saida = PILImage.new(mode='L', size=(self.largura, self.altura))
        saida.putdata(self.pixels)
        if isinstance(nome_arquivo, str):
            saida.save(nome_arquivo)
        else:
            saida.save(nome_arquivo, modo)
        saida.close()

    def gif_data(self):
        """
        Retorna uma string codificada em base 64, contendo a imagem
        fornecida, como uma imagem GIF.

        Função utilitária para tornar show_image um pouco mais limpo.
        """
        buffer = BytesIO()
        self.salvar(buffer, modo='GIF')
        return base64.b64encode(buffer.getvalue())

    def mostrar(self):
        """
        Mostra uma imagem em uma nova janela Tk.
        """
        global WINDOWS_OPENED
        if tk_root is None:
            # Se Tk não foi inicializado corretamente, não faz mais nada.
            return
        WINDOWS_OPENED = True
        toplevel = tkinter.Toplevel()
        # O highlightthickness=0 é um hack para evitar que o redimensionamento da janela
        # dispare outro evento de redimensionamento (causando um loop infinito de
        # redimensionamento). Para maiores informações, ver:
        # https://stackoverflow.com/questions/22838255/tkinter-canvas-resizing-automatically
        tela = tkinter.Canvas(toplevel, height=self.altura,
                              width=self.largura, highlightthickness=0)
        tela.pack()
        tela.img = tkinter.PhotoImage(data=self.gif_data())
        tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        def ao_redimensionar(event):
            # Lida com o redimensionamento da imagem quando a tela é redimensionada.
            # O procedimento é:
            #  * converter para uma imagem PIL
            #  * redimensionar aquela imagem
            #  * obter os dados GIF codificados em base 64 (base64-encoded GIF data)
            #    a partir da imagem redimensionada
            #  * colocar isso em um label tkinter
            #  * mostrar a imagem na tela
            nova_imagem = PILImage.new(mode='L', size=(self.largura, self.altura))
            nova_imagem.putdata(self.pixels)
            nova_imagem = nova_imagem.resize((event.largura, event.altura), PILImage.NEAREST)
            buffer = BytesIO()
            nova_imagem.save(buffer, 'GIF')
            tela.img = tkinter.PhotoImage(data=base64.b64encode(buffer.getvalue()))
            tela.configure(height=event.altura, width=event.largura)
            tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        # Por fim, faz o bind da função para que ela seja chamada quando a tela
        # for redimensionada:
        tela.bind('<Configure>', ao_redimensionar)
        toplevel.bind('<Configure>', lambda e: tela.configure(height=e.altura, width=e.largura))

        # Quando a tela é fechada, o programa deve parar
        toplevel.protocol('WM_DELETE_WINDOW', tk_root.destroy)


# Não altere o comentário abaixo:
# noinspection PyBroadException
try:
    tk_root = tkinter.Tk()
    tk_root.withdraw()
    tcl = tkinter.Tcl()


    def refaz_apos():
        tcl.after(500, refaz_apos)


    tcl.after(500, refaz_apos)
except:
    tk_root = None

WINDOWS_OPENED = False

if __name__ == '__main__':
    
    # O código neste bloco só será executado quando você executar
    # explicitamente seu script e não quando os testes estiverem
    # sendo executados. Este é um bom lugar para gerar imagens, etc.

     Questão 01: Está no TestInvertida.test_invertida_2
    
     Questão 02:
     peixe = Imagem.carregar(r'C:\Users\Pichau\Desktop\pset1\test_images\bluegill.png')
     peixe = peixe.invertida()
     Imagem.salvar(peixe,'pset1/resposta/peixe.png')

     Questão 03:
     80x0   +   (-0,07x53)   +   99x0 +
    (-0,45x129) + 127x1,20 + (-0,25x148) + 175x0 + (-0,12x174) + 193x0 +0 -3,71 +0 - 58,05 + 152,4 -37 +0 -20,88 +0 = 32,76
    
     Questão 04:
     kernel = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [1, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

     porco = Imagem.carregar(r'C:\Users\Pichau\Desktop\pset1\test_images\pigbird.png')
     relacaoPorco = porco.relacao(kernel)
     Imagem.salvar(relacaoPorco, 'pset1/resposta/porco_passaro.png')

    
     Questão 5.1:
    
    gato = Imagem.carregar(r'C:\Users\Pichau\Desktop\pset1\test_images\cat.png')
    gatoBorrado = gato.borrada(5)
    Imagem.salvar(gatoBorrado,'pset1/resposta/gato.png')
 
    python = Imagem.carregar(r'C:\Users\Pichau\Desktop\pset1\test_images\python.png')
    pythonFocada = python.focada(11)
    Imagem.salvar(pythonFocada,'pset1/resposta/python.png')

     Questão 6:
     operadorSobelX = [[1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]]

     operadorSobelY = [[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]]
    

     construcao = Imagem.carregar(r'C:\Users\Pichau\Desktop\pset1\test_images\construct.png')
     construcaoSobelX = construcao.relacao(operadorSobelX)
     Imagem.salvar(construcaoSobelX, 'pset1/resposta/construcao_sobel_X.png')

     construcaoSobelY = construcao.relacao(operadorSobelY)
     Imagem.salvar(construcaoSobelY, 'pset1/resposta/construcao_sobel_Y.png')
 
     construct = construcao.bordas()
     Imagem.salvar(construct,'pset1/resposta/construcao.png')

    pass
    # O código a seguir fará com que as janelas de Imagem.mostrar
    # sejam exibidas corretamente, quer estejamos executando
    # interativamente ou não:
    if WINDOWS_OPENED and not sys.flags.interactive:
        tk_root.mainloop()
