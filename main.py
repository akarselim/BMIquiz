import tkinter as tk

# Create screen
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("800x600")
FONT = ("Verdana", 11, "bold")


# Create label for weight
weight_label = tk.Label(window, text = "Enter your weight (kg)", font= FONT)
# Create entry for users input about weight
text_variable_weight = tk.StringVar()
weight_entry = tk.Entry(window, textvariable= text_variable_weight)

# Create label for height
height_label = tk.Label(window, text = "Enter your height (cm)", font = FONT )
# Create entry for users input about height
text_variable_height = tk.StringVar()
height_entry = tk.Entry(window, textvariable= text_variable_height)



def submit():
    weight = text_variable_weight.get()
    if weight != "":
        weight = float(text_variable_weight.get())

    height = text_variable_height.get()
    if height != "":
        height = float(text_variable_weight.get())




    def switch(bmi_formul):
        if 0<bmi_formul<18.5:
            return "Zayıf"
        elif 18.5<bmi_formul<24.9:
            return "Normal"
        elif 24.9<bmi_formul<29.9:
            return "Fazla kilolu"
        elif 29.9<bmi_formul<100:
            return "Obezite"
        else:
            print("You BMI doesn't calculate")



    if (weight ==0) or (height ==0) or (weight =="") or (height ==""):
        print("Enter both weight and height")

        warning_variable = "Enter both weight and height" # text
        warning_label = tk.Label(window, text= warning_variable)
        warning_label.grid(row =5, column = 1)


    else:
        bmi_formul = (weight / height * height)
        switch(bmi_formul)

        warning_variable = str(switch(bmi_formul)) # text
        warning_label = tk.Label(window, text= warning_variable)
        warning_label.grid(row =4, column = 1)



    text_variable_weight.set("")
    text_variable_height.set("")



cal_btn=tk.Button(window,text = 'Calculate', command = submit)


weight_label.grid(row =0, column = 0)
weight_entry.grid(row =0, column = 1)
height_label.grid(row =1, column = 0)
height_entry.grid(row =1, column = 1)
cal_btn.grid(row =3, column = 1)



window.mainloop()