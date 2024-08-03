import pygame
pygame.init()

#创建一个屏幕并设置屏幕大小
screen = pygame.display.set_mode((1000,500))

#设置屏幕标题
pygame.display.set_caption("bcylcygame")

#加载背景
background = pygame.image.load("图片/bcylcygame-ground.png").convert()

#字体
font = pygame.font.Font("字体/HarmonyOS_Sans_SC_Light.ttf",30)

#不允许背景向右方移动
background_move_right = False

#不允许背景向左方移动
background_move_left = False

#不允许背景向下方移动
background_move_down = False

#背景初始位置
background_x = 0

background_y = 205

#勇者是否在地面
on_ground = True

#魔王移动的距离
enemy_move_x = 0

#攻击造成的伤害
attack = 0

#受伤受到的伤害
hurt = 0