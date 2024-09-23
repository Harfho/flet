import flet as ft
import random


rand = random.randint(0,100)
text_correct=ft.Text(value='PRIDICT THE CORRECT NUMBERS',size=30)
column = ft.Column(
    controls=[
        text_correct,
    ],
    alignment=ft.MainAxisAlignment.CENTER
)

class Player(ft.Column):
    global text_correct
    global column
    instance_value=[]
    def __init__(self,player):
        super().__init__()
        self.player= player
        self.text = ft.TextField(hint_text="Gues a number from (1-100)",label=player,border_radius=30,adaptive=True)
        self.alignment=ft.CrossAxisAlignment.CENTER
        self.horizontal_alignment='center'
        self.adaptive=True
        self.controls.append(
            self.text
        )
        self.controls.append(
         ft.ElevatedButton(text='Check your guess',on_click=self.guess)
        )
        Player.instance_value.append(self.text)
    
    def reset(self,e):
        global rand
        rand = random.randint(0,100)
        print('new correct',rand)
        column.controls.pop(-1)
        self.update_text('RANDOM NUMBER RESET')
        
    def guess(self,e):
        print("correct",rand)
        listofplayer=[instance.label for instance in self.instance_value if instance.value]
        for text in self.instance_value:
            if text.value:
                guess_num =text.value
                print("guess_num",guess_num)
                if int(guess_num)==rand:
                    print(text.label,'GET IT CORRECTLY')
                    if(len(column.controls)<2):
                        column.controls.append(ft.ElevatedButton(text='START AGAIN',on_click=self.reset))
                    self.update_text(f"{text.label} GET IT CORRECTLY 😍".upper())
                    break
                else:
                    pridiction=[int(instance.value) for instance in self.instance_value if instance.value]
                    closest = min(pridiction, key=lambda x: abs(x - rand))
                    index_ = pridiction.index(closest)
                    # print(f"The number closest to {rand} is {closest} in {index_}")
                    # print(f"{listofplayer[index_]}")
                    self.update_text(f"CORRECT NUMBER IS CLOSER TO {listofplayer[index_]} GUESS".upper())
    
    def update_text(self,text):
            text_correct.value=text
            text_correct.update()
            column.update()
                    
class Game(ft.Column):
    global text_correct
    global column
    def __init__(self):
        super().__init__()
        self.row = ft.Card(
            content=ft.Row(
            controls=[
                ft.Text(value='GUESS ME',font_family='SM',size=30)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
            elevation=50
        )
        # self.controls.append(ft.Container())

        self.alignment=ft.CrossAxisAlignment.CENTER
        self.horizontal_alignment='center'
        self.adaptive=True
        self.controls.append(self.row)
        for i in range(3):
            self.controls.append(Player(f'player {i}'))        
        self.controls.append(column)    
        # self.controls.append(text_correct)

def main(page:ft.Page):
    page.title = 'GAME'
    page.padding=50
    page.fonts={
        'SM':'SM.otf',
        'PTH':'PTH.ttf'
    }
    page.adaptive=True    
    text_correct.font_family="PTH"
    game = Game()
    
    page.add(
        game,
    )
    
    
ft.app(target=main)