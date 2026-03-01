import tkinter as tk

def calculadora_imc():
    try:
        peso = float(entrada1.get().replace(',','.'))
        altura = float(entrada2.get().replace(',','.'))
        
        altura_quadrado = altura ** 2
        
        IMC = peso / altura_quadrado
        
        if IMC < 18.5:
            resultado = 'Abaixo do peso'
            cor = '#ccff00'
        elif IMC <= 24.9:
            resultado = 'Peso ideal'
            cor = '#09ff00'
        elif IMC <= 29.9:
            resultado = 'Sobrepeso'
            cor = '#ffe600'
        elif IMC <= 34.9:
            resultado = 'Obesidade grau 1'
            cor = '#ffaa00'
        elif IMC <= 39.9:
            resultado = 'Obesidade grau 2'
            cor = '#ff6200'
        else:
            resultado = 'Obesidade grau 3 (mórbida)'
            cor = '#ff0000'
        
        quadro_tabela.pack(pady=10)
        texto_final1.config(text=f'O valor do seu IMC é: {IMC:.2f}\n {resultado}', fg=cor, bg='black')
        texto_final2.config(text='''Menor que 18,5: Abaixo do Peso
18,5 – 24,9: Peso Normal (Saudável)
25,0 – 29,9: Sobrepeso
30,0 – 34,9: Obesidade Grau I
35,0 – 39,9: Obesidade Grau II (Severa)
Maior que 40,0: Obesidade Grau III (Mórbida)''')
        label_suporte.config(text='')
    except ValueError:
        quadro_tabela.pack_forget()
        texto_final1.config(text="Erro de entrada!", fg="red")
        label_suporte.config(text="Use números válidos (Ex: 70.5 e 1.75)", fg="red")

janela = tk.Tk()
janela.title('Calculadora de IMC')
janela.geometry('360x400')

texto = tk.Label(janela, text="Peso (kg):", font=('arial', 12)).pack(pady=5)
entrada1 = tk.Entry(janela, font=('arial', 11))
entrada1.pack()
entrada1.focus()

texto = tk.Label(janela, text="Altura (m):", font=('arial', 12)).pack(pady=5)
entrada2 = tk.Entry(janela, font=('arial', 11))
entrada2.pack()

botao = tk.Button(janela, text="Ver valor do IMC", command=calculadora_imc, bg="#e1e1e1", width=20, font=('arial', 12)).pack(pady=15)
janela.bind('<Return>', lambda event: calculadora_imc())

texto_final1 = tk.Label(janela, text='', font=('arial', 12, 'bold'))
texto_final1.pack()

label_suporte = tk.Label(janela, text='', font=('arial', 10, 'bold'))
label_suporte.pack()

quadro_tabela = tk.LabelFrame(janela, text="TABELA IMC (Índice de massa corporal)", padx=10, pady=10, bg='#d1cfcf')

texto_final2 = tk.Label(quadro_tabela, text='', justify='left', font=('arial', 10), bg='#d1cfcf')
texto_final2.pack()

janela.mainloop()