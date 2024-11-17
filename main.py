import sys, pygame
import math
import time

pygame.init()

scr_size = scr_w, scr_h = 500, 500
clock_r = 200

screen = pygame.display.set_mode(scr_size)
width = 1

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

clock = pygame.time.Clock()
tick = 60

def draw_clock():
    pygame.draw.circle(screen, WHITE, (scr_w/2, scr_h/2), clock_r, width)
    rad = 2*math.pi/60

    for i in range(60):
        inner_r = 0.9*clock_r if(i % 5 == 0) else 0.95*clock_r
        color = BLUE if(i % 5 == 0) else GREEN
        start_pos = scr_w/2 + inner_r*math.cos(i*rad), scr_h/2 + inner_r*math.sin(i*rad)
        end_pos = scr_w/2 + clock_r*math.cos(i*rad), scr_h/2 + clock_r*math.sin(i*rad)
        pygame.draw.line(screen, color, start_pos, end_pos, width)

def draw_sec(sec):
    needle_r = 0.9*clock_r
    sec_rad = sec*(2*math.pi/60)
    start_pos = scr_w/2, scr_h/2
    end_pos = scr_w/2 + needle_r*math.cos(sec_rad-math.pi/2), scr_h/2 + needle_r*math.sin(sec_rad-math.pi/2)
    pygame.draw.line(screen, RED, start_pos, end_pos, width)

def draw_min(min, sec):
    needle_r = 0.8*clock_r
    sec_rad = sec*(2*math.pi/60/60)
    min_rad = min*(2*math.pi/60)
    start_pos = scr_w/2, scr_h/2
    end_pos = scr_w/2 + needle_r*math.cos(min_rad+sec_rad-math.pi/2), scr_h/2 + needle_r*math.sin(min_rad+sec_rad-math.pi/2)
    pygame.draw.line(screen, GREEN, start_pos, end_pos, width)

def draw_hr(hr, min, sec):
    needle_r = 0.6*clock_r
    sec_rad = sec*(2*math.pi/12/60/60)
    min_rad = min*(2*math.pi/12/60)
    hr_rad = hr*(2*math.pi/12)
    start_pos = scr_w/2, scr_h/2
    end_pos = scr_w/2 + needle_r*math.cos(hr_rad+min_rad+sec_rad-math.pi/2), scr_h/2 + needle_r*math.sin(hr_rad+min_rad+sec_rad-math.pi/2)
    pygame.draw.line(screen, BLUE, start_pos, end_pos, width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    hr = time.localtime(time.time()).tm_hour
    min = time.localtime(time.time()).tm_min
    sec = time.localtime(time.time()).tm_sec

    draw_sec(sec)
    draw_min(min, sec)
    draw_hr(hr, min, sec)
    draw_clock()

    clock.tick(tick)
    pygame.display.flip()
