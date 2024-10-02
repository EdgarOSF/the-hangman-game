import flet as ft


word_to_guess = 'campana'
hidden_word = ['_'] * len(word_to_guess)
max_attemps = 7
attemps_left = max_attemps

hangman_images = [
    'img_hangman/0.png',
    'img_hangman/1.png',
    'img_hangman/2.png',
    'img_hangman/3.png',
    'img_hangman/4.png',
    'img_hangman/5.png',
    'img_hangman/6.png',
    'img_hangman/7.png',
]


def disable_all_buttons(page):
    for control in page.controls[1].controls:
        control.disabled = True
    page.update()


def letter_button(page, letter, hidden_word_display, hangman_image_display, message_display):

    def ft_onclick(e):
        global attemps_left
        # Deshabilitar boton al presionar
        e.control.disabled = True
        page.update()

        

        if letter in word_to_guess:
            for idx, chr in enumerate(word_to_guess):
                if letter == chr:
                    hidden_word[idx] = letter
            
            hidden_word_display.value = ' '.join(hidden_word)
            hidden_word_display.update()
            
            if '_' not in hidden_word:
                message_display.value = f'Felicidades haz ganado! 🥳'
                message_display.update()
                disable_all_buttons(page)

        else:
            attemps_left -= 1
            hangman_image_display.src = hangman_images[max_attemps - attemps_left]
            hangman_image_display.update()
            if attemps_left == 0:
                message_display.value = f'Ya no te quedan intentos... 😢, la palabra era {word_to_guess.upper()}'
                message_display.update()
                disable_all_buttons(page)

    btn = ft.ElevatedButton(letter, on_click=ft_onclick)

    return btn


def main(page: ft.Page):
    page.title = "Hangman"
    hidden_word_display = ft.Text(' '.join(hidden_word), size=50)
    hangman_image_display = ft.Image(
        src=hangman_images[0], width=400, height=400)

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_display = ft.Text(attemps_left)
    letters_buttons = [letter_button(
        page, letter, hidden_word_display, hangman_image_display, message_display) for letter in alphabet]

    page.add(
        hidden_word_display,
        ft.Row(letters_buttons, wrap=True),
        hangman_image_display,
        message_display

    )


ft.app(main)
