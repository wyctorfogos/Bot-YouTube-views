import kivy
import os
kivy.require('2.0.0')
os.environ['KIVY_GL_BACKEND']='angle_sdl2'
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput   
import Bot_view_video as AV

class YouTubeviews(App):
    def build(self):
        self.window=GridLayout()
        self.window.cols=1
        self.window.size_hint=(0.7,0.7)
        self.window.pos_hint={"center_x":0.5,"center_y":0.5}

        self.window.add_widget(Image(source="YouTubeviews.jpg"))
        
        #Label_1=self.greeting
        self.Label_1=Label(text="Escreva o nome do vídeo:",font_size=18, color='#00FFCE')
        self.window.add_widget(self.Label_1)

        self.user1=TextInput(multiline=False, padding_y=(20,15),size_hint=(1,1))
        self.window.add_widget(self.user1)

        self.Label_2=Label(text="Escreva a duração da visualização do vídeo:",font_size=18, color='#00FFCE')
        self.window.add_widget(self.Label_2)

        self.user2=TextInput(multiline=False, padding_y=(20,15),size_hint=(1,1))
        self.window.add_widget(self.user2)

        self.Label_3=Label(text="Escreva o n° visualizações do vídeo:",font_size=18, color='#00FFCE')
        self.window.add_widget(self.Label_3)

        self.user3=TextInput(multiline=False, padding_y=(20,15),size_hint=(1,1))
        self.window.add_widget(self.user3)

        self.button=Button(text="GREET",size_hint=(1,0.5),bold=True,background_color='#00FFCE')
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        
        return self.window

    def callback(self, instance):
        self.Label_1.text= "Vídeo: " + self.user1.text
        self.Label_2.text= "Tempo (s): " + self.user2.text
        self.Label_3.text="N° de Visualizações: " + self.user3.text
        url=self.user1.text
        tempo_visualizacao=int(self.user2.text)
        num_visualizacoes=int(self.user3.text)
        AV.Assistir_video_YouTube.Video(url,num_visualizacoes,tempo_visualizacao)

if __name__=="__main__":
    YouTubeviews().run()