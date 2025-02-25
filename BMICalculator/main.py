import tkinter

# Window
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width= 200, height= 200)
window.config(padx= 10, pady= 10)

# Calculate Functions
def calculate_bmi():
    weight = weight_entry.get()
    height = height_entry.get()

    if weight == "" or height == "":
        result_label.config(text= "Please enter both weight and height!")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)

            result_label.config(text= result_string)
        except:
            result_label.config(text= "Please enter a valid number!")

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "

    if bmi <= 16:
        result_string += "severely thin."
    elif 16 < bmi <= 17:
        result_string += "moderately thin."
    elif 17 < bmi <= 18.5:
        result_string += "mild thin."
    elif 18.5 < bmi <= 25:
        result_string += "normal."
    elif 25 < bmi <= 30:
        result_string += "overweight."
    elif 30 < bmi <= 35:
        result_string += "obese class 1."
    elif 35 < bmi <= 40:
        result_string += "obese class 2."
    else:
        result_string += "obese class 3."

    return result_string

# Label
weight_label = tkinter.Label(text= "Enter your weight (KG)", font= ("Arial", 10, "normal"))
weight_label.config(padx= 5, pady= 5)
weight_label.pack()

# Entry
weight_entry = tkinter.Entry(width= 15)
weight_entry.pack(padx= 5, pady= 5)

# Label
height_label = tkinter.Label(text= "Enter your height (cm)", font= ("Arial", 10, "normal"))
height_label.config(padx= 5, pady= 5)
height_label.pack()

# Entry
height_entry = tkinter.Entry(width= 15)
height_entry.pack(padx= 5, pady= 5)

# Button
calculate_button = tkinter.Button(text= "Calculate", command= calculate_bmi)
calculate_button.pack()

# Label
result_label = tkinter.Label()
result_label.pack()

window.mainloop()