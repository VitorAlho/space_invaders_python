class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena"""
    
    def __init__(self):
        """Inicializa as configurações estáticas do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        # Configurações da espaçonave
        self.ship_limit = 3
        
        # A taxa com que os pontos para cada alien aumentam
        self.score_scale = 1.5
        
        # Configurações dos projéteis        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
        
        # Configurações para aliens
        self.fleet_drop_speed = 10

        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1
        
    def initialize_dynamic_settings(self):
        """Inicializa as configurações dinâmicas do jogo"""
        # Configurações da espaçonave
        self.ship_speed_factor = 1.5
        
        # Pontuação
        self.alien_points = 50
        
        # Configurações dos projéteis
        self.bullet_speed_factor = 3
        
        # Configurações para aliens
        self.alien_speed_factor = 1
        
        # fleet_direction igual a 1 representa a direita;
        # -1 representa a esquerda
        self.fleet_direction = 1

    def increase_speed(self):
        """Aumenta as configurações de velocidade"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
