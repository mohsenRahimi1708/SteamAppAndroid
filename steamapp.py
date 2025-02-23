
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from pyXSteam.XSteam import XSteam


class SteamCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.steam_table = XSteam(XSteam.UNIT_SYSTEM_MKS)

    def calculate(self):
        try:
            # Retrieve and convert inputs to floats
            flow_ms = float(self.ids.flow_ms_input.text)
            t_ms = float(self.ids.t_ms_input.text)
            p_ms = float(self.ids.p_ms_input.text)
            flow_spray = float(self.ids.flow_spray_input.text)
            t_spray = float(self.ids.t_spray_input.text)
            p_spray = float(self.ids.p_spray_input.text)
            t_demand = float(self.ids.t_demand_input.text)
            #p_spray_demand = float(self.ids.p_spray_demand_input.text)
            #t_spray_demand = float(self.ids.t_spray_demand_input.text)
            p_spray_demand=p_spray
            t_spray_demand=t_spray


            # Perform calculations using pyXSteam
            h_ms = self.steam_table.h_pt(p_ms, t_ms)
            h_spray = self.steam_table.h_pt(p_spray, t_spray)
            h_mix = (flow_ms * h_ms + flow_spray * h_spray) / (flow_ms + flow_spray)
            t_out = self.steam_table.t_ph(p_ms, h_mix)
            h_demand = self.steam_table.h_pt(p_ms, t_demand)
            h_spray_demand = self.steam_table.h_pt(p_spray_demand, t_spray_demand)
            demand_spray = flow_ms * (h_ms - h_demand) / (h_demand - h_spray_demand)

            # Format result
            result = (
                f" {flow_spray:.1f} t/h spreay result ----->  {t_ms:.1f} °C drop to {t_out:.2f} °C\n"
                f"Spray Needed for {t_demand} °C: {demand_spray:.2f} t/h"
            )
            self.show_result(result)

        except ValueError:
            self.show_result("Error: Please enter valid numerical values.")
        except Exception as e:
            self.show_result(f"Error: {str(e)}")

    def show_result(self, result_text):
        popup = Popup(
            title="Calculation Result",
            content=Label(text=result_text),
            size_hint=(0.8, 0.8),
            auto_dismiss=True
        )
        popup.open()


class SteamApp(App):
    def build(self):
        return SteamCalculator()


if __name__ == "__main__":
    SteamApp().run()