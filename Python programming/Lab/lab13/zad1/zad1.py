import os, sys, pygame
"""
przyklad pokazuje funkcjonalnosc biblioteki pygame na prostej grze gdzie postać musi dojsc do mety a w tym
przeszkadzaja mu przeciwnicy 
"""
pygame.init()

width, height = 1280, 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Przyklad wykorzystania pygame Mateusz")
white = (255, 255, 255)
FPS = 60
box = pygame.Rect(10,20,20,20)
box2 = pygame.Rect(1220,660,10,10)     
box3 = pygame.Rect(100,100,30,20)
box4 = pygame.Rect(100,100,30,20)

def win_game():
    if box.x >= box2.x and box.y >= box2.y:
        print("wygranko")
        sys.exit(0)

def drawn_element():
    def draw_character():
      character = pygame.transform.scale(pygame.image.load('postac.jpg') , (60, 60))
      win.blit(character,box)
      pygame.display.flip()

    def draw_background():
      background = pygame.transform.scale(pygame.image.load('tlo.jpg'), (width, height))
      win.blit(background,(0, 0 ))

    def draw_meta():
     item = pygame.image.load('meta.jpg').convert_alpha()
     item = pygame.transform.scale(item, (40, 50)) 
     win.blit(item,box2)

    def draw_enemy_poz():
     enemy = pygame.image.load('enemy.jpeg').convert_alpha()
     enemy = pygame.transform.scale(enemy, (50, 50)) 
     win.blit(enemy, box3)
     if box3.x < 1280: 
       box3.x += 5
    if box3.x == box.x and box3.y == box.y:
        print("przegranko")
        sys.exit(0)

    def draw_enemy_hor():
     enemy = pygame.image.load('enemy.jpeg').convert_alpha()
     enemy = pygame.transform.scale(enemy, (50, 50)) 
     win.blit(enemy, box4)
     if box4.y < 720: 
       box4.y += 5
    if box4.y == box.y and box4.x == box.x:
        print("przegranko")
        sys.exit(0)
    
    draw_character()
    draw_background()
    draw_meta()
    draw_enemy_poz()
    draw_enemy_hor()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            box.x += 10
        if keys[pygame.K_LEFT]:
            box.x -= 10
        if keys[pygame.K_UP]:
            box.y -= 10
        if keys[pygame.K_DOWN]:
            box.y += 10
        drawn_element()
        win_game()
    pygame.quit()

if __name__ == "__main__":
    main()

