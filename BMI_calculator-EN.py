import tkinter as tk

def bmi_calculator():
    try:
        weight = float(entry1.get().replace(',','.'))
        height = float(entry2.get().replace(',','.'))
        
        height_square = height ** 2
        
        BMI = weight / height_square
        
        if BMI < 18.5:
            result = 'Underweight'
            color = '#ccff00'
        elif BMI <= 24.9:
            result = 'Healthy Weight / Normal'
            color = '#09ff00'
        elif BMI <= 29.9:
            result = 'Overweight'
            color = '#ffe600'
        elif BMI <= 34.9:
            result = 'Class I Obesity'
            color = '#ffaa00'
        elif BMI <= 39.9:
            result = 'Class II Obesity'
            color = '#ff6200'
        else:
            result = 'Class III Obesity (Severe)'
            color = '#ff0000'
        
        frame.pack(pady=10)
        final_text1.config(text=f'Your BMI value is: {BMI:.2f}\n {result}', fg=color, bg='black')
        final_text2.config(text='''Below 18.5: Underweight
18.5 – 24.9: Normal Weight (Healthy)
25.0 – 29.9: Overweight
30.0 – 34.9: Grade I Obesity
35.0 – 39.9: Grade II Obesity (Severe)
40.0 or higher: Grade III Obesity (Morbid)''')
        label_sup.config(text='')
    except ValueError:
        frame.pack_forget()
        final_text1.config(text="Entry error!", fg="red")
        label_sup.config(text="Use valid numbers (Ex: 70.5 e 1.75)", fg="red")

root = tk.Tk()
root.title('BMI Calculator')
root.geometry('360x400')

text = tk.Label(root, text="Weight (kg):", font=('arial', 12)).pack(pady=5)
entry1 = tk.Entry(root, font=('arial', 11))
entry1.pack()
entry1.focus()

text = tk.Label(root, text="Height (m):", font=('arial', 12)).pack(pady=5)
entry2 = tk.Entry(root, font=('arial', 11))
entry2.pack()

button = tk.Button(root, text="View BMI value", command=bmi_calculator, bg="#e1e1e1", width=20, font=('arial', 12)).pack(pady=15)
root.bind('<Return>', lambda event: bmi_calculator())

final_text1 = tk.Label(root, text='', font=('arial', 12, 'bold'))
final_text1.pack()

label_sup = tk.Label(root, text='', font=('arial', 10, 'bold'))
label_sup.pack()

frame = tk.LabelFrame(root, text="BMI (Body Mass Index) chart:", padx=10, pady=10, bg='#d1cfcf')

final_text2 = tk.Label(frame, text='', justify='left', font=('arial', 10), bg='#d1cfcf')
final_text2.pack()

root.mainloop()