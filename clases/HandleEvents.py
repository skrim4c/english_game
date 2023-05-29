class HandleEvents:
    def events(pygame,arr_data):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botón izquierdo del ratón
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if arr_data['button_close_x'] <= mouse_x <= arr_data['button_close_x'] + arr_data['button_close_width'] and arr_data['button_close_y'] <= mouse_y <= arr_data['button_close_y'] + arr_data['button_close_height']:
                        arr_data['button_close_clicked'] = True
                    if arr_data['button_snd_x'] <= mouse_x <= arr_data['button_snd_x'] + arr_data['button_snd_width'] and arr_data['button_snd_y'] <= mouse_y <= arr_data['button_snd_y'] + arr_data['button_close_height']:
                        if arr_data['button_snd_mute']:
                            arr_data['button_snd_mute'] = False
                        else:
                            arr_data['button_snd_mute'] = True
                    if arr_data['draw_button_x'] <= mouse_x <= arr_data['draw_button_x'] + arr_data['draw_button_width'] and arr_data['draw_button_y'] <= mouse_y <= arr_data['draw_button_y'] + arr_data['draw_button_height']:
                        arr_data['game_irregular_vetbs'] = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Botón izquierdo del ratón
                    if arr_data['button_close_clicked']:
                        arr_data['button_close_clicked'] = False
        return arr_data