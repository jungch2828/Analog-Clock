import sys, pygame
import math
import time

pygame.init()

scr_size = scr_w, scr_h = 500, 500
clock_r = 200

screen = pygame.display.set_mode(scr_size)
width = 1

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

clock = pygame.time.Clock()
tick = 60

def draw_clock():
    pygame.draw.circle(screen, white, (scr_w/2, scr_h/2), clock_r, width)
    rad = 2*math.pi/60

    for i in range(60):
        inner_r = 0.9*clock_r if(i % 5 == 0) else 0.95*clock_r
        color = blue if(i % 5 == 0) else green
        start_pos = scr_w/2 + inner_r*math.cos(i*rad), scr_h/2 + inner_r*math.sin(i*rad)
        end_pos = scr_w/2 + clock_r*math.cos(i*rad), scr_h/2 + clock_r*math.sin(i*rad)
        pygame.draw.line(screen, color, start_pos, end_pos, width)

def draw_sec(sec):
    needle_r = 0.9*clock_r
    rad_sec = sec*(2*math.pi/60)
    start_pos = scr_w/2, scr_h/2
    end_pos = scr_w/2 + needle_r*math.cos(rad_sec-math.pi/2), scr_h/2 + needle_r*math.sin(rad_sec-math.pi/2)
    pygame.draw.line(screen, red, start_pos, end_pos, width)

def draw_min(min, sec):
    needle_r = 0.8*clock_r
    rad_sec = sec*(2*math.pi/60/60)
    rad_min = min*(2*math.pi/60)
    start_pos = scr_w/2, scr_h/2
    end_pos = scr_w/2 + needle_r*math.cos(rad_min+rad_sec-math.pi/2), scr_h/2 + needle_r*math.sin(rad_min+rad_sec-math.pi/2)
    pygame.draw.line(screen, green, start_pos, end_pos, width)

def draw_hr(hr, min, sec):
    needle_r = 0.6*clock_r
    rad_sec = sec*(2*math.pi/12/60/60)
    rad_min = min*(2*math.pi/12/60)
    rad_hr = hr*(2*math.pi/12)
    start_pos = scr_w/2, scr_h/2
    end_pos = scr_w/2 + needle_r*math.cos(rad_hr+rad_min+rad_sec-math.pi/2), scr_h/2 + needle_r*math.sin(rad_hr+rad_min+rad_sec-math.pi/2)
    pygame.draw.line(screen, blue, start_pos, end_pos, width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)

    hr = time.localtime(time.time()).tm_hour
    min = time.localtime(time.time()).tm_min
    sec = time.localtime(time.time()).tm_sec

    draw_sec(sec)
    draw_min(min, sec)
    draw_hr(hr, min, sec)
    draw_clock()

    clock.tick(tick)
    pygame.display.flip()