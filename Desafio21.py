# Faça um programa que abra e
# reproduza o audio de um arquivo em MP3

import pygame
pygame.init()
pygame.mixer.music.load("nome.mp3")
pygame.mixer.music.play()
pygame.event.wait()
