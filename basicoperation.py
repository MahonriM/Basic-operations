from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
Builder.load_string('''
<MyGrid>:
    num1:num1
    num2:num2
    rst:rst
    GridLayout:
        cols:1
        size:root.width,root.height
        GridLayout:
            cols:3
            Label:
                text:"This program is made by Mahonri Mtz"
            Label:
                text:"Introduce a number"
            TextInput:
                id:num1
                multiline:False
            Label:
                text:"Introduce other number"
            TextInput:
                id:num2
                multiline:False
            Label:
                id:rst
                text:""
            Button:
                text:"Suma"
                on_press:root.suma()
            Button:
                text:"Resta"
                on_press:root.resta()
            Button:
                text:"Multiplicacion"
                on_press:root.mul()
        Button:
            text:"Division"
            on_press:root.div()
''')
class MyGrid(Widget):
    num1=ObjectProperty(None)
    num2=ObjectProperty(None)
    def suma(self):
        num1=int(self.num1.text)
        num2=int(self.num2.text)
        su=num1.__add__(num2)
        self.rst.text=("La suma es {0}".format(su))
    def resta(self):
        num1=int(self.num1.text)
        num2=int(self.num2.text)
        r=num1-num2
        self.rst.text=("La resta es {0}".format(r))
    def mul(self):
        num1=int(self.num1.text)
        num2=int(self.num2.text)
        m=num1.__mul__(num2)
        self.rst.text=("La multiplicacion es {0}".format(m))
    def div(self):
        num1=int(self.num1.text)
        num2=int(self.num2.text)
        d=num1/num2
        self.rst.text=("La division es {0}".format(d))        
class MyApp(App):
    def build(self):
        return MyGrid()
if __name__ =="__main__":
    MyApp().run() 
