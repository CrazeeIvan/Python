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