import pygame
import sys
import configuracoes_da_tela as cf
import espaco_nave as en

def run_game():
    pygame.init() # Inicializa os modúlos de pygame.
    configuracoes_da_tela = cf.ConfiguracoesDaTela()
    tela_jogo_ia = pygame.display.set_mode((configuracoes_da_tela.base, configuracoes_da_tela.altura)) # Cria um surface
    # para poder gerar um superfície que vai comportar elementos gráficos.
    pygame.display.set_caption("Invasão alienígena") # Delimitação do nome da janela.

    espaco_nave = en.EspacoNave(tela_jogo_ia)

    cor_de_fundo = (configuracoes_da_tela.cor_de_fundo) # Cor de fundo da tela de jogo

    while True:
        for evento in pygame.event.get(): # Coleta os eventos e específica um para fechar a janela.
            if evento.type == pygame.QUIT:
                sys.exit()

        tela_jogo_ia.fill(cor_de_fundo)
        espaco_nave.desenhar_imagem()

        pygame.display.flip() # Atualiza os frames em tela | Deixa a tela mais recente visivel.

run_game()

