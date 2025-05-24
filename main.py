import tkinter as tk

output = 0


def mile_to_km():
    global output
    mile = float(input_entry.get())
    output = mile * 1.60934
    output_label["text"] = round(output, 2)


window = tk.Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)

miles_label = tk.Label(text="Miles")
miles_label.config(padx=10, pady=10)
miles_label.grid(column=3, row=0)

equals_label = tk.Label(text="is Equal to:")
equals_label.config(padx=10, pady=10)
equals_label.grid(column=0, row=1)

km_label = tk.Label(text="Km")
km_label.config(padx=10, pady=10)
km_label.grid(column=3, row=1)

output_label = tk.Label(text=output)
output_label.config(padx=10, pady=10)
output_label.grid(column=1, row=1)

input_entry = tk.Entry(width=7)
input_entry.grid(column=1, row=0)

convert_button = tk.Button(text="Convert!", command=mile_to_km)
convert_button.grid(column=1, row=2)

window.mainloop()
