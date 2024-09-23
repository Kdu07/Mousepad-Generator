class Menu():
    def __init__(self, choices, table=None,exit=True,exitStr="Exit"):
        self.choice_strings = choices
        self.exit = exit
        self.table = table
        self.exitStr = exitStr

    def selection(self):
        print(self.table)
        
        sel = -1

        for i, choice in enumerate(self.choice_strings):
            print(f"[{i+1}]", choice)
        if self.exit:
            print(f"[0] {self.exitStr}")

        while sel not in self.choiceMax:
            sel = int(input(">>> "))

        return sel
    
    @property
    def choiceMax(self):
        self._choiceMax = [i+1 for i, c in enumerate(self.choice_strings)]
        if self.exit:
            self._choiceMax.append(0)
        return self._choiceMax        
    

"""
menu1_choices = ["Attack","Heal","Items"]
menu1_table = "####### TABLE #######\nSubtitle: Sentence\n\nInfo: Information\n---------------------\n"

menu1 = Menu(menu1_choices, table=menu1_table)

menu1.table()
selection = menu1.selection()
"""
