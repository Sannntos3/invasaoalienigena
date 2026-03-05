import pygame
import sys
import configuracoes_da_tela as cf

class EspacoNave:
    def __init__(self, tela_jogo_ia):
        self.tela_jogo_ia = tela_jogo_ia

        # Carrega a espaço-nave e obtém o retângulo dela.
        self.imagem = pygame.image.load("imagem_espaco_nave/espaconave.bmp")
        self.retangulo_da_espaco_nave = self.imagem.get_rect()
        self.retangulo_da_tela = tela_jogo_ia.get_rect()

        # Iniciar a espaço nave no ponto inferior da tela.
        self.retangulo_da_espaco_nave.centerx = self.retangulo_da_tela.centerx
        self.retangulo_da_espaco_nave.bottom = self.retangulo_da_tela.bottom

    def desenhar_imagem(self):
        # Desenha a espaço-nave na parte inferior da tela.
        self.tela_jogo_ia.blit(self.imagem, self.retangulo_da_espaco_nave)


def run_game():
    pygame.init() # Inicializa os modúlos de pygame.
    configuracoes_da_tela = cf.ConfiguracoesDaTela()
    tela_jogo_ia = pygame.display.set_mode((configuracoes_da_tela.base, configuracoes_da_tela.altura)) # Cria um surface
    # para poder gerar um superfície que vai comportar elementos gráficos.
    pygame.display.set_caption("Invasão alienígena") # Delimitação do nome da janela.

    espaco_nave = EspacoNave(tela_jogo_ia)

    cor_de_fundo = (configuracoes_da_tela.cor_de_fundo) # Cor de fundo da tela de jogo

    while True:
        for evento in pygame.event.get(): # Coleta os eventos e específica um para fechar a janela.
            if evento.type == pygame.QUIT:
                sys.exit()

        tela_jogo_ia.fill(cor_de_fundo)
        espaco_nave.desenhar_imagem()

        pygame.display.flip() # Atualiza os frames em tela | Deixa a tela mais recente visivel.

run_game()

