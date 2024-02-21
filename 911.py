import runpy
import sys
import pygame


def main():
    # Set up window
    pygame.init()

    size = (1280, 720)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("9/11")

    # Load the background image (ensure transparency)
    background = pygame.image.load("bumpy_sky-blue_03-512x512.png").convert_alpha()
    background = pygame.transform.scale(background, size)

    # Load the plane image
    plane = pygame.image.load("Aircraft-PNG-Photos.png")
    plane = pygame.transform.scale(plane, (120, 100))

    # Initial position for the plane (centered)

    plane_x = (size[0] - plane.get_width()) // 6
    plane_y = (size[1] - plane.get_height()) // 2

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen with the background image
        screen.blit(background, (0, 0))

        # Blit the plane image at the calculated position
        screen.blit(plane, (plane_x, plane_y))

        # Update the display
        pygame.display.flip()

        # move the plane 
        plane_x += 1
        #speed
       

if __name__ == "__main__":
    main()
