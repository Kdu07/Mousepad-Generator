from PIL import Image, ImageDraw as D, ImageOps
import numpy as np
import menu as me
import json
import os


class Generator():
    def __init__(self):
        pass
    
    def add_logo(self):
        '''
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
    
        return self.img
        '''
        pass

    def add_border(self):
        '''
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
        '''
        pass

    def save_product():
        #add_logo()
        pass

    
    def save_display():
        #add_logo()
        #add_border()
        pass

    def table_main():
        pass

    def table_config():
        pass

    
    @property
    def data(self):       
        with open(r"data.json", "r") as file:
            self._data = json.load(file)
        return self._data

    @data.setter
    def data(self, value):       
        self._data = value 
        with open(r"data.json", "w") as file:
            json.dump(self._data, file)


# Class Generator
    # Vars
        # dir paths dictionary {"source": <path>, ...}
        # source_img
        # source_logo
        # extension


def main():
    gen = Generator()
    
    """
    data = gen.data
    data['config']['border_radius'] = 10
    gen.data = data
    """

    menu_main = me.Menu(["GERAR IMAGENS", "ALTERAR imagem ({<filename>})", "ALTERAR cor da logo (<filename>)", "CONFIGURAÇÕES"], 
                        "Mousepad Generator\n\n", exitStr="SAIR")   
    
    selection_main = 1

    while selection_main != 0:
        clear()
        selection_main = menu_main.selection()

        match selection_main:
            case 1:
                # Gerar imagens
                pass
            
            case 2:
                # Alterar imagem fonte
                img_source_new = input("Nova imagem: ")
                data = gen.data
                data["paths"]["img_source_filename"] = img_source_new              
                gen.data = data

            case 3:
                # Alterar cor da logo
                data = gen.data
                logo_list = [key for key in data["logo"]]
                menu_logo = me.Menu([i.title() for i in logo_list], "LOGO - OPÇÕES DE CORES", exitStr="VOLTAR")

                clear()
                selection_logo = menu_logo.selection()
                if selection_logo != 0:
                    logo_source = data["logo"][logo_list[selection_logo - 1]]
                    data["paths"]["logo_source_filename"] = logo_source
                    gen.data = data
            
            case 4:
                data = gen.data
                
                config_list = [key for key in data["config"]]

                
                menu_config = me.Menu([" "], "Configurações\n\n", exitStr="VOLTAR")
                selection_config = 1
                
                while selection_config != 0:
                    menu_config.choice_strings = [f"LOGO - Proporção ({data["config"]["logo_proportion"]})", 
                                      f"LOGO - Posição vertical na estampa ({data["config"]["logo_vertical"]})", 
                                      f"LOGO - Posição horizontal na estampa ({data["config"]["logo_horizontal"]})", 
                                      f"BORDA - Grossura ({data["config"]["border_width"]})", 
                                      f"BORDA - Raio de curva ({data["config"]["border_radius"]})"]

                    clear()
                    selection_config = menu_config.selection()

                    if selection_config != 0:
                        config_key = config_list[selection_config - 1]
                        data["config"][config_key] = int(input(f"Atual: {data["config"][config_key]} | Novo: "))
                        gen.data = data


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_table():
    pass


if __name__ == "__main__":
    main()