import random,time,sys
from 变量 import*
while True: 	
    for user_input in pygame.event.get():	
        key = pygame.key.get_pressed()
        #退出
        if user_input.type == pygame.QUIT:	
            pygame.quit()
            sys.exit()
        #检测"a"是否被持续按下
        if key[pygame.K_a]:
            background_move_right = True
        else:
            background_move_right = False   
        #检测"d"是否被持续按下
        if key[pygame.K_d]:
            background_move_left = True
        else:
            background_move_left = False  
        #检测"空格"是否被按下
        if key[pygame.K_SPACE] and on_ground == True:
            background_move_down = True
        #检测"s"是否被按下
        if key[pygame.K_s]:
            #技能冷却
            time.sleep(0.01)
            #魔王在勇者左边+空气墙
            if enemy_x <= 475 and enemy_x >= 175 and enemy_move_x >= -2120:
                attack += 1
                enemy_move_x -= 1
            #魔王在勇者右边+空气墙
            if enemy_x >= 475 and enemy_x <= 775 and enemy_move_x <= 1200:
                attack += 1
                enemy_move_x += 1
    #魔王位置
    enemy_x = background_x + enemy_move_x + 1000
    enemy_y = background_y - 60
    #勇者与魔王接触时受伤
    if enemy_x >= 475 and enemy_x <= 525 and enemy_y >= 145 and enemy_y <= 245:
        hurt += 1
    #游戏整体速度
    stop = random.randint(1, int(1/0.5))    
    if stop == 1:    
        time.sleep(0.001)
    #背景向左方移动+空气墙
    if background_move_left == True and background_x + 2266 != 525:
        background_x -= 1
    #背景向右方移动+空气墙
    if background_move_right == True and background_x - 1133 != 475:
        background_x += 1
    #勇者是否在地面上
    if background_y != 205:
        on_ground = False
    else:
        on_ground = True
    #勇者上升
    if background_move_down == True and background_y < 400:
        background_y +=1
    #勇者上升到极限
    if background_y == 400:   
        background_move_down = False
    #勇者落地
    if background_move_down == False and background_y > 205:
        background_y -= 1
    #魔王移动速度
    enemy_move = random.randint(1, int(1/0.2))
    if enemy_move == 1:    
        if enemy_x <= 475:
            enemy_move_x += 1
        else:
            enemy_move_x -= 1
    #蓝色天空
    screen.fill((50,150,255))
    #当前魔王血量
    text_enemy_hp = font.render(("魔王的血量还有" + str(2500 - attack)),True,(0,0,0))
    screen.blit(text_enemy_hp,(0,5))
    #当前勇者血量
    text_soldier_hp = font.render(("你的血量还有" + str(250 - hurt)),True,(0,0,0))
    screen.blit(text_soldier_hp,(0,45))
    #3块地图
    screen.blit(background,(background_x,background_y))
    screen.blit(background,(background_x - 1133,background_y))
    screen.blit(background,(background_x + 1133,background_y))
    #勇者
    pygame.draw.rect(screen,(0,0,0),(475,145,50,100),0)
    #魔王
    pygame.draw.rect(screen,(255,0,0),(enemy_x,enemy_y,50,100),0)
    #结局
    if attack >= 2500 and hurt >= 250:
        text_none_winner = font.render(("你与魔王同归于尽了"),True,(0,0,0))
        screen.blit(text_none_winner,(0,85))
        #更新屏幕
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        sys.exit()
    else:    
        if attack >= 2500:
            text_win = font.render(("你赢了"),True,(255,255,0))
            screen.blit(text_win,(0,85))
            #更新屏幕
            pygame.display.update()
            time.sleep(5)
            pygame.quit()
            sys.exit()
        if hurt >= 250:
            text_die = font.render(("你死了"),True,(255,0,0))
            screen.blit(text_die,(0,85))
            #更新屏幕
            pygame.display.update()
            time.sleep(5)
            pygame.quit()
            sys.exit()
    #更新屏幕
    pygame.display.update()