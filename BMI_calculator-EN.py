import tkinter as tk

def only_numbers_height(char):
    """Validates if the string `char` is an acceptable number for the Entry.
    Rules:
    - allow empty string (so user can clear field)
    - allow only digits and at most one comma (for decimal separator)
    - do not allow starting with a comma
    - limit length to 3 characters (to prevent excessively long input)
    """
    if char == '':
        return True
    if char.count(',') > 1:
        return False
    if char[0] == ',':
        return False
    if len(char) > 3:
        return False
    if all(c in '0123456789,' for c in char):
        return True
    return False

def only_numbers_weight(char):
    """Validates if the string `char` is an acceptable number for the Entry.
    Rules:
    - allow empty string (so user can clear field)
    - allow only digits and at most one comma (for decimal separator)
    - do not allow starting with a comma
    - limit length to 5 characters (to prevent excessively long input)
    """
    if char == '':
        return True
    if char.count(',') > 1:
        return False
    if char[0] == ',':
        return False
    if len(char) > 5:
        return False
    if all(c in '0123456789,' for c in char):
        return True
    return False

def bmi_calculator():
    try:
        weight = float(entry1.get().replace(',','.'))
        height = float(entry2.get().replace(',','.'))
        if height == 0 or weight == 0:
            final_text1.config(text="Entry a valid height and weight!", fg="red", bg='black')
            label_sup.config(text="Height and weight must be greater than zero.", fg="red")
            frame.pack_forget()
            final_text2.config(text="")
            return
        
        
        height_square = height ** 2
        
        BMI = weight / height_square
        
        if BMI < 18.5:
            result, color = 'Underweight', '#ccff00'
        elif BMI <= 24.9:
            result, color = 'Healthy Weight / Normal', '#09ff00'
        elif BMI <= 29.9:
            result, color = 'Overweight', '#ffe600'
        elif BMI <= 34.9:
            result, color = 'Class I Obesity', '#ffaa00'
        elif BMI <= 39.9:
            result, color = 'Class II Obesity', '#ff6200'
        else:
            result, color = 'Class III Obesity (Severe)', '#ff0000'

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
        label_sup.config(text="Use valid numbers (Ex: 70,5 e 1,75)", fg="red")

root = tk.Tk()
root.title('BMI Calculator')
root.geometry('360x400')

vcmd_height = (root.register(only_numbers_height), '%P')
vcmd_weight = (root.register(only_numbers_weight), '%P')

text = tk.Label(root, text="Weight (kg):", font=('arial', 12)).pack(pady=5)
entry1 = tk.Entry(root, font=('arial', 11), validate='key', validatecommand=vcmd_weight)
entry1.pack()
entry1.focus()

text = tk.Label(root, text="Height (m):", font=('arial', 12)).pack(pady=5)
entry2 = tk.Entry(root, font=('arial', 11), validate='key', validatecommand=vcmd_height)
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