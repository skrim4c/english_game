import pygame

##clases
import clases.LoadsResources as C
import clases.HandleEvents as HandleEvents

class app:
    # Initialize Pygame
    pygame.init()
    arr_data = {}
    screen,frames = C.LoadsResources.init(pygame)
    arr_data = C.LoadsResources.load(pygame)
    arr_data['running'] = True


    if __name__ == '__main__':
        clock = pygame.time.Clock()
        frame_index = 0
        while arr_data['running']:

            frame = frames[frame_index]
            frame_index += 1
            if frame_index >= len(frames):
                frame_index = 0
            screen.blit(frame, (0, 0))

            arr_data = HandleEvents.HandleEvents.events(pygame,arr_data)
            arr_data,screen = C.LoadsResources.DrawButtons(pygame,arr_data,screen)
            pygame.display.update()
            
            clock.tick(30)
        pygame.quit()