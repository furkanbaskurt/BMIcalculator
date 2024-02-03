import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)

paddingUp = (30, 0)
paddingY = (5, 0)
bmiResult = 0.0

weightText = tkinter.Label(window, text="Enter Your Weight (KG)")
heightText = tkinter.Label(window, text="Enter Your Height (cm)")
resultText = tkinter.Label(window)

weightInput = tkinter.Entry(window, width=10)
heightInput = tkinter.Entry(window, width=10)

weightText.pack(pady=paddingUp)
weightInput.pack(pady=paddingY)
heightText.pack(pady=paddingY)
heightInput.pack(pady=paddingY)


def bmiCalculate():
    global weightInput
    global heightInput
    global bmiResult
    weight = weightInput.get()
    height = heightInput.get()

    try:
        result = int(weight) / ((int(height) / 100) ** 2)
        bmiResult = round(result, 2)

        def control():
            if bmiResult < 18.50:
                resultText.config(text=f"Your BMI is {bmiResult}. You are under weight.")
            elif 18.50 <= bmiResult <= 24.90:
                resultText.config(text=f"Your BMI is {bmiResult}. You are normal weight.")
            elif 24.90 < bmiResult <= 29.90:
                resultText.config(text=f"Your BMI is {bmiResult}. You are over weight.")
            else:
                resultText.config(text=f"Your BMI is {bmiResult}. You are obese.")

        control()
    except:
        resultText.config(text="Please enter a valid value!")


button = tkinter.Button(window, text="CALCULATE", command=bmiCalculate)
button.pack(pady=paddingY)
resultText.pack(pady=paddingUp)


window.mainloop()
