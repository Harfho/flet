from flet import *
import flet as ft
import time
import threading

class timer(UserControl):
    
    def __init__(self,time=10):
        super().__init__()
        self.seconds=time
    
    def did_mount(self):
        self.runnning=True
        self.my_thread = threading.Thread(target=self.update_timer,args={},daemon=False)
        self.my_thread.start()
    
    def will_unmount(self):
        self.runnning=False
    
    def update_timer(self):
        while self.runnning and self.seconds:
            mins,secs = divmod(self.seconds,60)
            self.countdown.value=f"{mins:02d}:{secs:02d}"
            self.update()
            time.sleep(1)
            self.seconds-=1
            
    def build(self):
        self.countdown=Text()
        return self.countdown
        
class Mytimer(Column):
    def __init__(self,sec):
        super().__init__()
        self.sec=sec
        self.df_sec=self.sec
        self.text=Text()
        self.controls=[self.text]
        # self.update()
    
    @staticmethod
    def seconds_to_minutes(seconds):
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{minutes}:{remaining_seconds:02d}"
    
    def count_down(self):
        while self.sec:
            self.sec-=1
            timer=self.seconds_to_minutes(self.sec)
            self.text.value=timer
            time.sleep(1)
            self.text.update()
        
        if(self.sec==0):
            self.controls.append(ft.ElevatedButton(text='Reset',icon=ft.icons.RESTORE,on_click=self.reset))
            self.update()
    def reset(self,e):
        print(self.controls)
        self.controls.pop()
        self.sec=self.df_sec
        self.update()
        self.did_mount()
        
    def did_mount(self):
        threading.Thread(target=self.count_down,args=[],daemon=True).start()
        
def main(page:Page):
    page.window.width=200
    page.window.height=200
    ft1=Mytimer(60) 
    ft2=Mytimer(120)
    page.add(Column(controls=[
        ft1,
        ft2]
                    ))    
    
    
ft.app(target=main)