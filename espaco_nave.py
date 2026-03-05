import pygame
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

