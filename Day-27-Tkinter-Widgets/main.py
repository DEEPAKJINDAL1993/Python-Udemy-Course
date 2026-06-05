import tkinter

window = tkinter.Tk()
window.title('Mile to KM Converter')
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

# Label
# my_label = tkinter.Label(window, text='My Label',font=('Arial', 20,'bold'))
# my_label.place(x=50, y=50)

FONT = ('Arial', 16,'normal')

label = tkinter.Label(window, text='is equal to', font=FONT)
Miles_label = tkinter.Label(window, text='Miles', font=FONT)
Km_label = tkinter.Label(window, text='Km', font=FONT)
km_result = tkinter.Label(window, text=0)
label.grid(row=1, column=0)
Miles_label.grid(row=0, column=2)
Km_label.grid(row=1, column=2)
km_result.grid(row=1, column=1)

# my_label.config(font=('Arial', 24,'bold'))
# my_label['text'] = 'New Label'

# Button
def miles_to_km():
    miles = float(miles_input.get())
    km_result['text'] = round(miles*1.609,2)
    return km_result


calc_button = tkinter.Button(text='Calculate', command=miles_to_km)
calc_button.grid(row=2, column=1)

# Entry

miles_input = tkinter.Entry(width=10)
miles_input.grid(row=0, column=1)
#input.place(x=50, y=150)
#input.grid(column=0, row=0)








window.mainloop()
