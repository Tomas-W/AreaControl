import pygame


all_sprites = pygame.sprite.Group()
# Characters
player_sprite = pygame.sprite.GroupSingle()
enemy_sprites = pygame.sprite.Group()
# Projectiles
all_projectile_sprites = pygame.sprite.Group()
player_projectile_sprites = pygame.sprite.Group()
enemy_projectile_sprites = pygame.sprite.Group()
bomb_sprites = pygame.sprite.Group()
# Creepers
all_creeper_sprites = pygame.sprite.Group()
bat_sprites = pygame.sprite.Group()
fish_sprites = pygame.sprite.Group()
# Pickups
all_pickup_sprites = pygame.sprite.Group()
skull_sprites = pygame.sprite.Group()
energy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()
health_potion_sprites = pygame.sprite.Group()
# Interactives
all_interactives_sprites = pygame.sprite.Group()
portal_sprites = pygame.sprite.Group()