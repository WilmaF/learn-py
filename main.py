import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

kivy.require('1.9.1')

var = 0
def soma_um(instance):
  global var
  var +=1
  instance.text = str(var)

class MeuApp(App):
  def build(self):
      layout = BoxLayout(orientation='vertical',
                         padding=[40,20,40,20])

      layout.add_widget(Label(text='Olá do Kivy!'))
      btn = Button(text='Pressione-me!',size=(100,50))

      btn.bind(on_press=soma_um)
      layout.add_widget(btn)
      return layout
if __name__ =='__main__':
      MeuApp().run()
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
