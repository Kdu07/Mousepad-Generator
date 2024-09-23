# Use pillow to cut logo to the right size

from PIL import Image, ImageDraw as D, ImageOps

def main():
    source_path = r'C:\Users\cadus\ARQUIVOS CADU\Codes\Python\Projetos\Mousepad Generator\source\logos_source'
    file = "logo_" + input("Filename: ") + ".png"
    filename = source_path + '\\' + file

    dest_path = r'C:\Users\cadus\ARQUIVOS CADU\Codes\Python\Projetos\Mousepad Generator\source\logos_source copy'
    dest_filename = dest_path + '\\' + file


    logo = Image.open(filename)
    #logo.show()

    cuttedLogo = cut_logo(logo)
    #cuttedLogo.show()
    cuttedLogo.save(dest_filename)
    


def cut_logo(logo):
    w, h = logo.size
    logo = logo.crop((0, 30, w, h-2315))

    return logo


if __name__ == "__main__":
    main()