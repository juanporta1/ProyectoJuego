import pygame

parallax_bg = pygame.image.load("assets//background//parallax-mountain-bg.png")

parallax_bg = pygame.transform.scale(parallax_bg, (parallax_bg.get_width() * 3, parallax_bg.get_height() * 5))
