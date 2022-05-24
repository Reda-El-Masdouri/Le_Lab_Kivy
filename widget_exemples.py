from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, BooleanProperty
from kivy.lang import Builder

Builder.load_file("widget_exemples.kv")


class WidgetExemple(GridLayout):
    mon_texte = StringProperty("0")
    #slider_value_txt = StringProperty("Valeur")
    compteur_actif = BooleanProperty(False)
    compteur = 1
    my_texte_input = StringProperty("Ecrire")
    def on_button_click(self):
        print("Button click")
        if self.compteur_actif:
            self.mon_texte = str(self.compteur)
            self.compteur += 1
    def on_toggle_button_state(self, widget):
        #print("Toggle state: " + widget.state)
        if widget.state == "normal":
            print("OFF")
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            print("ON")
            widget.text = "ON"
            self.compteur_actif = True
    def on_switch_active(self, widget):
        print("Switch: "+ str(widget.active))
    #def on_value_slider(self, widget):
    #    print("The value is:" +str(int(widget.value)))
        #self.slider_value_txt = str(int(widget.value))
    def on_text_validate(self, widget):
        self.my_texte_input = widget.text  