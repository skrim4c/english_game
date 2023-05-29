from moviepy.editor import VideoFileClip
import os

class LoadsResources:
    def init(pygame):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

        width, height = 400, 600
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("My english game -skrim4c-")
        icon = pygame.image.load("./src/img/icon.ico")  
        pygame.display.set_icon(icon)
        screen = pygame.display.set_mode((width, height), pygame.NOFRAME)

        # Calcular la posición para centrar la ventana
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Centrar la ventana en la pantalla
        os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'

        pygame.mixer.init()
        pygame.mixer.music.load("./src/snd/menu.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)
        end_event = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(end_event)
        pygame.mixer.music.play(loops=-1)

        video = VideoFileClip("./src/vid/bg.mp4")
        frames = []
        for frame in video.iter_frames():
            frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
            frame = pygame.transform.scale(frame, (width, height))
            frames.append(frame)        
                
        return screen, frames
    
    def DrawButtons(pygame,arr_data,screen):
        font = pygame.font.Font(None, 50)
        font2 = pygame.font.Font(None, 30)

        if arr_data['button_close_clicked']:
            screen.blit(arr_data['button_close_image_click'], (arr_data['button_close_x'], arr_data['button_close_y']))
            arr_data['running'] = False
        else:
            screen.blit(arr_data['button_close_image'], (arr_data['button_close_x'], arr_data['button_close_y']))
        
        if not arr_data['button_snd_mute']:
            screen.blit(arr_data['button_snd_image'], (arr_data['button_snd_x'], arr_data['button_snd_y']))
            pygame.mixer.music.set_volume(0.5)
        else:
            screen.blit(arr_data['button_snd_image_mute'], (arr_data['button_snd_x'], arr_data['button_snd_y']))
            pygame.mixer.music.set_volume(0.0)
        
        text_surface = font.render("English game", True, arr_data['color_white'])
        screen.blit(text_surface, (arr_data['draw_tittle_x'], arr_data['draw_tittle_y']))

        if not arr_data['game_irregular_vetbs']:
            pygame.draw.rect(screen, arr_data['color_red'], (arr_data['draw_button_x'], arr_data['draw_button_y'], arr_data['draw_button_width'] , arr_data['draw_button_height'] ))
            text_surface2 = font2.render("Verbos irregulares", True, arr_data['color_white'])
            screen.blit(text_surface2, (arr_data['draw_button_text_x'], arr_data['draw_button_text_y']))
        else:
            pygame.draw.rect(screen, arr_data['color_red'], (arr_data['draw_input_x'], arr_data['draw_input_y'], arr_data['draw_input_width'] , arr_data['draw_input_height']),arr_data['draw_input_text_line'])
        return arr_data,screen


    def load(pygame):
        arr_data = {}
        ##
        ##Tittle
        arr_data['draw_tittle_x'] = 15
        arr_data['draw_tittle_y'] = 15
        ###
        arr_data['color_white'] =   (255, 255, 255)
        arr_data['color_black'] =   (0, 0, 0)
        arr_data['color_red'] =     (255, 0, 0)
        ## Botton irregulars verbs
        arr_data['draw_button_width'] =     200
        arr_data['draw_button_height'] =    50
        arr_data['draw_button_x'] = 100
        arr_data['draw_button_y'] = 150
        arr_data['draw_button_text_x'] = 110
        arr_data['draw_button_text_y'] = 165

        ## Botton irregulars verbs
        arr_data['draw_input_width'] =     200
        arr_data['draw_input_height'] =    50
        arr_data['draw_input_x'] = 100
        arr_data['draw_input_y'] = 250
        arr_data['draw_input_text_x'] = 110
        arr_data['draw_input_text_y'] = 165
        arr_data['draw_input_text_line'] = 2


        #GAME STATE 1
        arr_data['texto_input'] = ""
        arr_data['game_irregular_vetbs'] = False

        ##BUTTON CLOSE
        arr_data['button_close_width'] = 50;arr_data['button_close_height'] = 50
        arr_data['button_close_image'] = pygame.image.load("./src/img/close.png")
        arr_data['button_close_image'] = pygame.transform.scale(arr_data['button_close_image'], (arr_data['button_close_width'], arr_data['button_close_height']))
        arr_data['button_close_x'] = 340
        arr_data['button_close_y'] = 10
        arr_data['button_close_image_click'] = pygame.transform.scale(arr_data['button_close_image'], (arr_data['button_close_width']+1, arr_data['button_close_height']+1))
        arr_data['button_close_clicked'] = False
        ##BUTTON SONIDO
        arr_data['button_snd_width'] = 50;arr_data['button_snd_height'] = 50
        arr_data['button_snd_image'] = pygame.image.load("./src/img/sound.png")
        arr_data['button_snd_image'] = pygame.transform.scale(arr_data['button_snd_image'], (arr_data['button_snd_width'], arr_data['button_snd_height']))
        arr_data['button_snd_x'] = 280
        arr_data['button_snd_y'] = 10
        arr_data['button_snd_image_mute'] = pygame.image.load("./src/img/sound_disable.png")
        arr_data['button_snd_image_mute'] = pygame.transform.scale(arr_data['button_snd_image_mute'], (arr_data['button_snd_width'], arr_data['button_snd_height']))
        arr_data['button_snd_mute'] = False
        
        return arr_data