###############################################################################
#Tutorial from
#http://thecodeinn.blogspot.ie/2013/07/tutorial-weather-forecast-in-python.html
###############################################################################
import pywapi
import tkinter as tk

report = "Please select where you'd like your weather report for!"

def getWeatherTullamore():
    weather_com_result = pywapi.get_weather_from_weather_com('EIXX0046:1:EI')
    r = "It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "°C now in Tullamore."
    lblReport.config(text=r)


def getWeatherDublin():
    weather_com_result = pywapi.get_weather_from_weather_com('EIXX0014:1:EI')
    r = "It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "°C now in Dublin."
    lblReport.config(text=r)



root = tk.Tk()
root.title("Ciaran's simple weather app")
root.geometry("400x300")

lblReport = tk.Label(root, text=report, fg="dark green")
lblReport.pack()



btnSelectDublin = tk.Button(root, text='Dublin', width=25, command=getWeatherDublin)
btnSelectDublin.pack()

btnSelectTullamore = tk.Button(root, text='Tullamore', width=25, command=getWeatherTullamore)
btnSelectTullamore.pack()

btnExit = tk.Button(root, text='Exit', width=25, command=root.destroy)
btnExit.pack()

root.mainloop()