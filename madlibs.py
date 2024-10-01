from flet import *
import flet as ft

class InputField(TextField):
    def __init__(self,placeholder:str):
        super().__init__()
        self.label=placeholder
        self.border_radius=20
        
    

def main(page:Page):
    page.scroll=ScrollMode.AUTO
    page.horizontal_alignment='center'
    
    list_of_input=[['occupation','noun_1'],
                   ['adj_01','noun_02'],
                   ['verb_01','adj_02'],
                   ['noun_03','verb_02'],
                   ['noun_04','verb_03'],
                   ]
    col=Column(auto_scroll=ScrollMode.AUTO)
    
    for input in list_of_input:
        counter =True
        for hint in range(len(input)):
            if counter:
                col.controls.append(Row(controls=[
                            InputField(input[hint]),
                            InputField(input[hint+1]),
                              ],alignment=MainAxisAlignment.CENTER)
                            )
            counter=False
    
    
    print(col.controls)
 
    answers =Text(style=TextThemeStyle.HEADLINE_MEDIUM,color='#f2ff00')
    def generateMad(e):
        generated_text ='The diligent {occupation} meticulously scrutinized the {adj_01} {noun_02} with unwavering focus, desperately attempting to {verb_01} the {adj_02} {noun_03} before the unpredictable {noun_04} could abruptly {verb_03} and potentially {verb_02} in a manner that would undoubtedly complicate the already intricate situation, all while maintaining a professional demeanor and adhering to the strict protocols that governed their line of work.'
        for row in col.controls:
            for items in row.controls:
                print(items.label,items.value)
                generated_text=generated_text.replace(f"{{{items.label}}}",items.value)
        
        answers.value=generated_text
        answers.update()
        
        
    button = ElevatedButton('GENERATE MADLIBS',on_click=generateMad)
    title=Container(
        content=Row(controls=[Text(value='ENJOY BADLIBS')],
                    alignment=MainAxisAlignment.CENTER),
        padding=padding.only(bottom=30)
        
            )
    
    page.add(
    title,
     col,
     button,
     answers
    )
    
app(target=main)