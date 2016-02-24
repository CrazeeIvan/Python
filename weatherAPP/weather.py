import pywapi
import tkinter as tk
def getWeather():
#    if (city == Dublin):
    weather_com_result = pywapi.get_weather_from_weather_com('EIXX0014:1:EI')
    weather_com_result = pywapi.get_weather_from_weather_com('EIXX0014:1:EI')
    report = "It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "°C now in Dublin."
    return report
#city = input("Enter city name: ")
dublinReport = getWeather()
root = tk.Tk()
root.title("Ciaran's simple weather app")
root.geometry("400x300")
lblReport = tk.Label(root, text=dublinReport, fg="dark green")
lblReport.pack()
btnUpdate = tk.Button(root, text='Update', width=25, command=getWeather())
btnUpdate.pack()
btnExit = tk.Button(root, text='Exit', width=25, command=root.destroy)
btnExit.pack()

root.mainloop()