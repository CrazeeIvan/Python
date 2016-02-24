import pywapi
import tkinter as tk
def getWeather():
#    if (city == Dublin):
    weather_com_result = pywapi.get_weather_from_weather_com('EIXX0014:1:EI')
    weather_com_result = pywapi.get_weather_from_weather_com('EIXX0014:1:EI')
    report = "It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "°C now in Dublin."
    return report

dublinReport = getWeather()
root = tk.Tk()
root.title("Ciaran's simple weather app")
root.geometry("400x300")
label = tk.Label(root, text=dublinReport, fg="dark green")
label.pack()
button = tk.Button(root, text='Update', width=25, command=getWeather())
button.pack()
root.mainloop()

#w = Label(root, text=dublinReport)
#w.pack()




#import tkinter as tk

#class Application(tk.Frame):
#    def __init__(self, master=None):
#        tk.Frame.__init__(self, master)
#        self.pack()
#        self.createWidgets()

#    def createWidgets(self):
#        self.hi_there = tk.Button(self)
#        self.hi_there["text"] = "Hello World\n(click me)"
#        self.hi_there["command"] = self.say_hi
#        self.hi_there.pack(side="top")

#        self.QUIT = tk.Button(self, text="QUIT", fg="red",
#                                            command=root.destroy)
#        self.QUIT.pack(side="bottom")

#    def say_hi(self):
#        print("hi there, everyone!")

#root = tk.Tk()
#app = Application(master=root)
#app.mainloop()