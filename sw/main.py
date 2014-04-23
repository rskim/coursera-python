from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

milliseconds = attempts = wins = 0
running = "No"

def format(milliseconds):
    seconds = milliseconds / 10
    tenths = milliseconds % 10
    minutes = seconds / 60
    seconds %= 60
    return str(minutes) + ":" + str(seconds).rjust(2, '0') + "." + str(tenths)

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
        milliseconds += 1
        timer_kv.text = format(milliseconds)

    def reset(self, *args):
        timer_kv = self.ids['timer_kv']
        score_kv = self.ids['score_kv']
        global milliseconds
        global attempts
        global wins
        milliseconds = attempts = wins = 0
        score_kv.text = "0/0"
        timer_kv.text = "0:00.0"


class StopWatchApp(App):
    def build(self):
        return GameScreen()



StopWatchApp().run()