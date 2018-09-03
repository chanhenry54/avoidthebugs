import pygame,sys,os
# https://www.pygame.org/docs/tut/PygameIntro.html

pygame.init() # initialize the display window
pygame.mixer.init() # initialize the module that plays sounds

size = (width, height) = (800, 450)
scrn = pygame.display.set_mode(size)

base_y = height-100

def get_files(dir):
    files = []

    for (dirpath, dirname, filenames) in os.walk(dir):
        files = filenames
        break
    
    return files

images = {}
for file in get_files('assets/images/'):
    images[os.path.splitext(file)[0]] = pygame.image.load('assets/images/' + file)

sfx = {}
for file in get_files('assets/sfx/'):
    sfx[os.path.splitext(file)[0]] = pygame.mixer.Sound('assets/sfx/' + file)

pygame.display.set_caption('Avoid the Bugs')
pygame.display.set_icon(images['appicon'])

mcFont = pygame.font.Font('assets/fonts/Minecraft.ttf', 24) # load in the custom font.

images['gary'] = pygame.transform.scale(images['gary'], (64, 64))
images['platform'] = ground = pygame.transform.scale(images['platform'], (width, images['platform'].get_size()[1]))

playRect = pygame.Rect((width-300)//2,(height+70)//2,300,120)
images['playbtn'] = pygame.transform.scale(images['playbtn'], playRect.size)
images['titleimg'] = pygame.transform.scale(images['titleimg'], (798, 242))

images['sky'] = pygame.transform.scale(images['sky'], size)

state = 0 # 0: MENU, 1: PLAY, 2: RESULTS
score = 0

jump = {
    'isJumping': False,
    'falling': False,
    'height': 0
}

started = False # Will turn True once the player hits space as an indicator to go.
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit() # make sure pygame clears everything out smoothly
        elif ev.type == pygame.MOUSEBUTTONUP:
            pos = ev.pos

            if playRect.collidepoint(pos) and state == 0:
                state = 1
                score = 0
    
    scrn.blit(images['sky'], (0, 0))

    if (state == 0):
        scrn.blit(images['titleimg'], (playRect.x - 250, playRect.y - 250))
        scrn.blit(images['playbtn'], (playRect.x, playRect.y))
    elif (state == 1):
        # Draw the sprites onto the screen through blit.

        scoreS = mcFont.render('SCORE: ' + str(score), False, (0, 0, 0))
        scrn.blit(scoreS, (5, 5))

        groundY = base_y - ground.get_size()[1]
        scrn.blit(images['gary'], (25, groundY+jump['height']))
        if jump['isJumping']:
            if jump['height'] <= -150 or jump['falling']:
                jump['falling'] = True

                if jump['height'] >= 0:
                    jump['isJumping'] = False
                    jump['falling'] = False
                    jump['height'] = 0
                else:
                    jump['height'] += 1.5
            else:
                jump['height'] -= 1.5

        if pygame.key.get_pressed()[pygame.K_SPACE] and not jump['isJumping']:
            jump['isJumping'] = True
            sfx['jump'].play()
            if not started: started = True
        
        if started:
            pass

        scrn.blit(ground, (0, base_y + ground.get_size()[1]))
    
    # update graphics
    pygame.display.flip()