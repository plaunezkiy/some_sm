from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.graphics import *
from math import cos, sin, radians
import re
import function as func

var = 'AB', '<ACB', 'BC', '<BAC', 'AC', '<ABC'
input_list = []

"""from kivy.config import Config
Config.set('graphics', 'resizable',0)"""


class FloatInput(TextInput):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        self.multiline = False
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)


class Wid(Widget):
    def __init__(self, **kwargs):
        super(Wid, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)

    def update_canvas(self, *args):
        pointse = toch
        self.canvas.clear()
        with self.canvas:
            Color(0.5,0.5,0.5,0.5)
            Triangle(points=toch)
        # print(toch)

# 300, 125, 400, 250, 500, 125


class Plaungles(App):
    global toch

    def build(self):
        def sol():
            global toch
            for i in range(6):
                if input_list[i].text == '':
                    input_list[i].text = '0'
            global solv
            resul = func.solve(float(input_list[2].text), float(input_list[4].text), float(input_list[0].text),
                               float(input_list[3].text), float(input_list[5].text), float(input_list[1].text))
            for i in range(6):
                input_list[i].text = str(round(resul[i], 2))
        # -----------------------
            if not resul[0] and not resul[1] and not resul[2] and not resul[3] and not resul[4] and not resul[5]:
                popup = Popup(title='Ошибка', content=Button(text='Что-то пошло не так', size_hint=(0.8, 0.8),
                                                             on_press=lambda a: popup.dismiss()),
                              size_hint=(None, None), size=(400, 150))
                popup.open()
                for i in range(6):
                    input_list[i].text = ''
                return
        # -----------------------
            c = resul[0]
            ce = resul[1]
            a = resul[2]
            al = resul[3]
            b = resul[4]
            be = resul[5]

            a = a / b * 150
            c = c / b * 150
            b = 175
        # -----------------------
            toch = list(map(lambda x: x.text, input_list))
            toch = (300, 125, 300+a, 125, 300+cos(radians(be))*c, 125+sin(radians(be))*c)
        # -----------------------
            if solv == 1:
                return
            solv = 1
            global gr, grap
            grap = 0
            gr = Button(text='Построить',size_hint=('1', '0.2'), on_press=lambda a: gra())
            bl.add_widget(gr)
        # -----------------------

        def cler():
            bl.remove_widget(clr)
            bl.remove_widget(can)
            global grap
            for i in range(6):
                input_list[i].text = ''
            grap = 0
        # ------------------------

        def gra():
            global grap
            if grap != 0:
                return
            grap = 1
            global clr,can
            can = Wid(size_hint=('1', '0.6'))
            bl.add_widget(can)
            clr = Button(text='Очистить',size_hint=('1','0.2'),on_press=lambda a:cler())
            bl.add_widget(clr)
        # -------------------------
        global bl
        bl = BoxLayout(orientation='vertical',spacing=5,padding=2)
        gl = GridLayout(cols=4,spacing=2,size_hint=('1','0.5'))
        # -------------------------
        for i in range(6):
            gl.add_widget(Label(text=var[i]))
            input_list.append(FloatInput())
            gl.add_widget(input_list[i])
        input_list[0].focus = True
        bl.add_widget(gl)
        # but = BoxLayout(spacing=2.5,size_hint=('1','0.2'))
        global solv
        solv = 0
        bl.add_widget(Button(text='Решить',size_hint=('1','0.2'),on_press=lambda a:sol()))
        return bl

    
if __name__ == "__main__":
    Plaungles().run()