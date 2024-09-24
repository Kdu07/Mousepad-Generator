from PIL import Image, ImageDraw as D, ImageOps
import numpy as np
import menu as me
import json
import os


class Generator():    
    def add_logo(self):
        # Logo to image ratio
        ratio = self.data["config"]["logo_proportion"]

        # Logo height position factor
        pos_h = self.data["config"]["logo_vertical"]

        # Logo width position factor
        pos_w = self.data["config"]["logo_horizontal"]


        # CODE
        factor = ratio/ (self.logo.width/self.img.width)
        self.logo = ImageOps.scale(image=self.logo, factor=factor)
        offset = (int((self.img.width - self.logo.width) / pos_w), int((self.img.height - self.logo.height) / pos_h))
        
        self.img.paste(self.logo, offset, self.logo)
        

    def add_border(self):
        # Border width
        border_w = int(self.data["config"]["border_width"])
        
        # Border radio
        rad = int(self.data["config"]["border_radius"])

        
        # CODE
        # Add rounded border
        self.img = self.img.convert("RGBA")

        new = Image.new('RGBA', self.img.size, (255, 255, 255, 0))
        draw = D.Draw(new)

        draw.rounded_rectangle([(0, 0), (self.img.width, self.img.height)], fill=(255, 0, 0, 0), outline="black",
                            width=border_w, radius=rad)
        
        self.img = Image.alpha_composite(self.img, new)

        # Cut final image
        circle = Image.new('L', (rad * 2, rad * 2), 0)
        draw = D.Draw(circle)
        draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
        alpha = Image.new('L', self.img.size, 255)
        w, h = self.img.size
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        self.img.putalpha(alpha)

    
    def show_images(self):
        img_name = self.data["paths"]["img_source_filename"]
        logo_name = self.data["paths"]["logo_source_filename"]

        img_id, extension = img_name.split('.')

        self.img =  Image.open(f"{self.data["paths"]["img_source_folder"] + "\\" + img_name}", "r")
        self.logo = Image.open(f"{self.data["paths"]["logo_source_folder"] + "\\" + logo_name}", "r")
        
        self.add_logo()
        self.img_product = self.img

        self.add_border()
        self.img_site = self.img

        self.save_img_site = self.data["paths"]["img_site_folder"] + "\\" + "site_" + img_id + ".png"
        self.save_img_product = self.data["paths"]["img_products_folder"] + "\\" + "produto_" + img_id + ".png"
        
        #self.img_product.show()
        self.img_site.show()


    def save_images(self):
        self.img_site.save(self.save_img_site)
        self.img_product.save(self.save_img_product)

    
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
    data = gen.data

    menu_main = me.Menu(["GERAR IMAGENS", "ALTERAR imagem ({<filename>})", "ALTERAR cor da logo (<filename>)", "CONFIGURAÇÕES"], 
                        "Mousepad Generator\n\n", exitStr="SAIR")
    
    selection_main = 1

    while selection_main != 0:
        menu_main.choice_strings = [f"GERAR IMAGENS", 
                                  f"ALTERAR imagem ({data["paths"]["img_source_filename"]})", 
                                  f"ALTERAR cor da logo ({data["paths"]["logo_source_filename"]})", 
                                  f"CONFIGURAÇÕES"]
        clear()
        selection_main = menu_main.selection()

        match selection_main:
            case 1:
                gen.show_images()

                save = '1'
                while save != 'y' and save != 'n':
                    save = input("Salvar imagens? [y/n]: ")
                
                if save == 'y':
                    gen.save_images()

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
                        data["config"][config_key] = float(input(f"Atual: {data["config"][config_key]} | Novo: "))
                        gen.data = data


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_table():
    pass


if __name__ == "__main__":
    main()