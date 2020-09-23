import pygame 
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game(): 
	# Inicializa o jogo e cria um objeto para a tela    
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Cria o botão de play
	play_button = Button(ai_settings,screen,"Play")
	
	# Cria uma instância para armazenas dados estatísticos do jogo
	# e cria painel de pontuação
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	
	# Cria uma espaçonave
	ship = Ship(ai_settings,screen)
	
	# Cria um alienígena
	alien = Alien(ai_settings,screen)
	
	# Cria um grupo no qual serão armazenados os projéteis
	bullets = Group()
	
	# Cria um grupo no qual serão armazenados os alienígenas
	aliens = Group()
	
	# Cria a frota de alienígenas
	gf.create_fleet(ai_settings,screen,ship,aliens)	
	
	# Inicia o laço principal do jogo
	while True: 
		
		# Observa eventos de teclado e de mouse 
		gf.check_events(ai_settings,stats,sb,play_button,screen,ship,aliens,bullets)
		
		if stats.game_active == True:
			# Atualiza a posição da espaçonave a cada passagem do laço
			ship.update()
			
			# Atualiza a posição dos projéteis a cada passagem do laço
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			
			# Atualiza a posição dos aliens a cada passagem do laço
			gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
		
		# Redesenha a tela a cada passagem do laço
		gf.update_screen(ai_settings, stats, screen, sb, ship, aliens, bullets, play_button)

run_game()
