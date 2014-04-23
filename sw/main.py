from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter

milliseconds = 0
seconds = 0
minutes = 0
attempts = 0
wins = 0
running = "No"

class GameScreen(BoxLayout):
    def click(self, *args):
        score_kv = self.ids['score_kv']
        global running
        global attempts
        global wins
        if running == "No":
            Clock.schedule_interval(self.tick, 0.1)
            running = "Yes"
        else:
            Clock.unschedule(self.tick)
            attempts += 1
            if (milliseconds % 10) == 0:
                wins += 1
            running = "No"
        score_kv.text = str(wins) + "/" + str(attempts)

    def tick(self, *args):
        timer_kv = self.ids['timer_kv']
        global milliseconds
        global seconds
        global minutes
        if milliseconds < 9:
            milliseconds += 1
        else:
            seconds +=1
            milliseconds = 0
        if seconds == 60:
            minutes += 1
            seconds = 0
        if len(str(seconds)) == 1:
            secondsf = "0" + str(seconds)
        else:
            secondsf = seconds
        timer_kv.text = (str(minutes) + ":" + str(secondsf) + "." + str(milliseconds))


class StopWatchApp(App):
    def build(self):
        return GameScreen()



StopWatchApp().run()