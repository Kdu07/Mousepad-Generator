from PIL import Image, ImageDraw as D, ImageOps
import numpy as np

def main():
    # Split extension (.jpg | .png)
    # Add category (-website | -product)
    # Add extension again  
    
    img_filename = 'porsche.jpg'
    logo_filename = 'logo_white.png'

    img_source = Image.open(img_filename)
    logo_source = Image.open(logo_filename)
    
    img_product = add_logo(img_source, logo_source)
    img_product.show()

    img_website = add_rounded_border(img_product)
    img_website.show()

    img_website.save("website/img_website.png")
    img_product.save("product/img_product.png")


def add_logo(img, logo):
    # Logo to image ratio
    ratio = 0.25

    # Logo width position factor
    pos_w = .98

    # Logo height position factor
    pos_h = .95

    # CODE
    factor = ratio/ (logo.width/img.width)
    logo = ImageOps.scale(image=logo, factor=factor)
    offset = (int((img.width - logo.width) / pos_w), int((img.height - logo.height) / pos_h))
    
    img.paste(logo, offset, logo)
    
    return img


def add_rounded_border(img):
    # Border radio
    rad = 100

    # Border width
    border_w = 35
    
    # CODE
    # Add rounded border
    img = img.convert("RGBA")

    new = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = D.Draw(new)

    draw.rounded_rectangle([(0, 0), (img.width, img.height)], fill=(255, 0, 0, 0), outline="black",
                        width=border_w, radius=rad)
    
    img = Image.alpha_composite(img, new)

    # Cut final image
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = D.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', img.size, 255)
    w, h = img.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    img.putalpha(alpha)

    out = img
    return out


if __name__ == "__main__":
    main()
