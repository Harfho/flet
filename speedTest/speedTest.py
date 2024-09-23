import flet as ft 
import speedtest_cli as sp
from flet import *
import time
import re
   
st = sp.Speedtest()
def main(page:Page):
    page.title='speed test'
    page.window.width=480
    page.window.height=640
    page.theme_mode='dark'    
    page.vertical_alignment='center'
    page.horizontal_alignment='center'
    page.bgcolor='black'
    page.window.bgcolor='blue'
    page.auto_scroll=True    
    page.fonts={
      "titlefont":"fonts/RoosterPersonalUse-3z8d8.ttf",
      "sourcecode":"fonts/Code7X5Regular-ypBe.ttf",
      "sourcecode1":"SourceCodeProExtralightItalic-dpex.ttf",
    }
     
    appTitle = Row(
        controls=[
            ft.Text("Internet",font_family='titlefont',color='red',size=30),
            ft.Text("Speed",font_family='titlefont',color='yellow',size=30),
        ],
        alignment=MainAxisAlignment.CENTER,
        spacing=0,
        scroll=True
    )
    line=Text(value='',font_family='sourcecode1')
    terminal = Column()
    lines = []
    for i in range(0,8):
        line=Text(value='',font_family='sourcecode')
        if i==0:
            line.value='> Press start'
            line.color='#ffffff'
        elif i==7:
            line.color='#ffffff'            
        elif i==3 or i==6:
            line.color='#fff000'
        else:
            line.color='#1aff1a'
        lines.append(line)
    
    terminal.controls=lines
    speed_container=Container(
        content=terminal,
        width=200,
        height=200,
        bgcolor="#3a3a3a",
        border_radius=30,
        padding=10,
        animate=animation.Animation(1000,'bounceOut')
    )

    def animate_speed_container(e):
        speed_container.update()
        if(speed_container.width>=700):
            for controls in speed_container.content.controls:
                if re.search('text',str(type(controls))):
                    controls.value=''
                else:
                    controls.opacity=0
                      
            speed_container.width=300
            speed_container.height=200
            speed_container.content.controls[0].value='> Press start'
            speed_container.update()
            
        else:
            # speed_container.content=terminal
            speed_container.width=700
            speed_container.height=500
            
            speed_container.content.controls[0].value=f'> Setting up speeds calculation'
            speed_container.update()
            progress=ProgressBar(width=400,color='#1100ff', bgcolor='#ffffff',opacity=1)    
            progressbar3=Row(controls=[progress],)
            time.sleep(2)
            speed_container.content.controls.insert(1,progressbar3)
            speed_container.update()
            
            
            time.sleep(1)
            server=st.get_best_server()
            progressbar3.controls[0].value=1
            speed_container.content.controls[1]=progressbar3
            speed_container.update()
            print(server)
                                
            city=server['name']
            country=server['country']
            cc = server['cc']
            
            speed_container.content.controls[2].value=f'> The best possible server is ({city}),({country}),({cc})'
            speed_container.update()
            time.sleep(2)
            
            speed_container.content.controls[3].value=f'> Connection established, status OK, Fetching download speed'
            speed_container.update()
            progress=ProgressBar(width=400,color='#1100ff', bgcolor='#ffffff',opacity=1)    
            progressbar1=Row(controls=[progress],)
            time.sleep(2)
            speed_container.content.controls.insert(4,progressbar1)
            speed_container.update()
            
            download =st.download()/1024/1024
            speed_container.content.controls[5].value=f'> download speed {str(round(download,2))} mp/s'
            print(progressbar1.controls)
            progressbar1.controls[0].value=1
            speed_container.content.controls[4]=progressbar1
            speed_container.update()
            time.sleep(2)
            
            speed_container.content.controls[6].value=f'> Connection established, status OK, Fetching upload speed'            
            speed_container.update()
            progress=ProgressBar(width=400,color='#1100ff', bgcolor='#ffffff',opacity=1)
            time.sleep(2)
            progressbar2=Row(controls=[progress],)
            speed_container.content.controls.insert(7,progressbar2)
            speed_container.update()
            
            
            upload =st.upload()/1024/1024
            speed_container.content.controls[8].value=f'> upload speed {str(round(upload,2))} mp/s'
            print(progressbar2.controls)
            progressbar2.controls[0].value=1
            speed_container.content.controls[7]=progressbar2
            speed_container.update()
            
            
            speed_container.content.controls[9].color='#ffffff' 
            speed_container.content.controls[9].value=f'\n> task completed successfully\n\n>> app developed by Harfho'
            
            # terminal.controls=lines
            # speed_container.content=terminal            
            speed_container.update()
        
        speed_container.update()
        
    icon =IconButton(icon=icons.PLAY_CIRCLE_FILL_OUTLINED,icon_color='green',on_click=animate_speed_container)
    page.add(
        appTitle,
        speed_container,
        icon,
    )
    
    



ft.app(target=main,assets_dir="assets")