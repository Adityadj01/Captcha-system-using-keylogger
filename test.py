from PIL import Image, ImageDraw, ImageFont
import random
import string

def generate_random_chars(num_chars):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(num_chars))

def create_captcha_image(chars, img_width, img_height):
    font = ImageFont.truetype('arial.ttf', 30)
    image = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(image)

    # Start drawing text
    char_width = 0
    for char in chars:
        # Use getmask instead of getsize
        mask = font.getmask(char)
        # Calculate the size of the mask
        char_width += mask.size[0]

    # The starting position of the text depends on the calculated width
    start_pos = (img_width - char_width) // 2

    for char in chars:
        draw.text((start_pos, 5), char, font=font, fill='black')
        # Update the starting position
        start_pos += font.getmask(char).size[0]

    return image
def main():
    num_chars = 5
    img_width = 150
    img_height = 50

    chars = generate_random_chars(num_chars)
    image = create_captcha_image(chars, img_width, img_height)

    image.save('captcha.png')
    print(f'Generated CAPTCHA: {chars}')

if __name__ == '__main__':
    main()
    