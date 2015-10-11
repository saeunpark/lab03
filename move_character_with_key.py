from pico2d import *

def handle_events():
    global running
    global x, y

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                keys[0] = True
            elif event.key == SDLK_LEFT:
                keys[1] = True
            elif event.key == SDLK_UP:
                keys[2] = True
            elif event.key == SDLK_DOWN:
                keys[3] = True
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                keys[0] = False
            elif event.key == SDLK_LEFT:
                keys[1] = False
            elif event.key == SDLK_UP:
                keys[2] = False
            elif event.key == SDLK_DOWN:
                keys[3] = False

# http://www.gimo.co.kr/index.php?mid=game_dev&listStyle=webzine&document_srl=433

    if keys[0]:
       x+=5
    elif keys[1]:
        x-=5
    if keys[2]:
       y+=5
    elif keys[3]:
        y-=5


open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
x = 0
y = 0
frame = 0
keys = [False, False, False, False]
#playerpos = [100,100]
while (running):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)
    handle_events()

close_canvas()
