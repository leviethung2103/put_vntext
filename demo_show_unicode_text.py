from PIL import ImageFont, ImageDraw, Image

def put_VietnameseText(img_path, vn_text, font_name="times.ttf"):
    # Read a PIL Image
    pil_im = Image.open(img_path).convert("RGBA")
    width, height = pil_im.size
    
    rect_height = 200
    x_rect = 0
    y_rect = height - rect_height
    
    # Create an object to draw 2D graphics
    draw = ImageDraw.Draw(pil_im)
    draw.rectangle(((x_rect, y_rect), (width, height)), fill="black")

    # Choose a font
    font_size = 30
    font = ImageFont.truetype(font_name, font_size, encoding='unic')

    # Draw the text
    text_size = draw.textsize(vn_text, font)
    text_w = text_size[0]
    text_h = text_size[1]
    print('Width, Height of the text: ', text_w, text_h)
    text_pos = ((width-text_w)/2, height-(rect_height-text_h)/2)    
    draw.text(text_pos, vn_text, font=font, fill=(255,255,255,255))

    # Save the image
    pil_im.save('output_test.png')


if __name__=='__main__':
    img_path = './BTV_TranHang.png'
    vn_text = 'BTV Trần Hằng'
    font_name = './timesbi.ttf'
    put_VietnameseText(img_path, vn_text, font_name)
