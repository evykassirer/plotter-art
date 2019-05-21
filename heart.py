import pygame

pygame.init()

WIDTH = 900
HEIGHT = WIDTH
screen = pygame.display.set_mode((WIDTH+1, HEIGHT+1))

LEFT = 0
TOP = 0

HALF_BUMP_WIDTH = int(WIDTH*0.25)
MID_LEFT = HALF_BUMP_WIDTH
MID = HALF_BUMP_WIDTH*2
MID_RIGHT = HALF_BUMP_WIDTH*3

BUMP_SIDE_Y = HEIGHT/3
BUMP_MID_Y = HEIGHT/5


blue = 0, 0, 255
TICKS_PER_ALL = 40
TICKS_PER_HALF_BUMP = int(TICKS_PER_ALL/4)

# ----- top curves -----

for i in range(0, TICKS_PER_HALF_BUMP + 1):
  percent_through = i/TICKS_PER_HALF_BUMP
  # left bump, left side
  pygame.draw.line(screen, blue,
      (LEFT, percent_through*BUMP_SIDE_Y),
      (MID_LEFT - percent_through*HALF_BUMP_WIDTH, TOP)
    )
  # left bump, right side
  pygame.draw.line(screen, blue,
    (MID, percent_through*BUMP_MID_Y),
    (MID_LEFT + percent_through*HALF_BUMP_WIDTH, TOP)
  )
  # right bump, left side
  pygame.draw.line(screen, blue,
      (MID, percent_through*BUMP_MID_Y),
      (MID_RIGHT - percent_through*HALF_BUMP_WIDTH, TOP)
    )
  # right bump, right side
  pygame.draw.line(screen, blue,
      (WIDTH, percent_through*BUMP_SIDE_Y),
      (MID_RIGHT + percent_through*HALF_BUMP_WIDTH, TOP)
    )

# ----- bottom pointy thing -----

LOWEST_RIGHT_TICK = BUMP_SIDE_Y + 0.6*(HEIGHT - BUMP_SIDE_Y) - 200
# 200 is a magic number oh well TODO make it less magic?

for i in range(0, TICKS_PER_HALF_BUMP + 1):
  percent_through = i/TICKS_PER_HALF_BUMP
  pygame.draw.line(screen, blue,
    (MID + percent_through*2*HALF_BUMP_WIDTH, HEIGHT),
    (WIDTH, LOWEST_RIGHT_TICK-percent_through*(LOWEST_RIGHT_TICK - BUMP_SIDE_Y))
  )

  pygame.draw.line(screen, blue,
    (MID - percent_through*2*HALF_BUMP_WIDTH, HEIGHT),
    (0, LOWEST_RIGHT_TICK-percent_through*(LOWEST_RIGHT_TICK - BUMP_SIDE_Y))
  )


pygame.display.flip()

done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
