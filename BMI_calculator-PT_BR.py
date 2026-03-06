import tkinter as tk

def somente_numeros_altura(texto):
    """Valida se a string `texto` é um número aceitável para o Entry.
    Regras:
    - aceita string vazia (permite apagar o campo)
    - permite somente dígitos e no máximo uma vírgula (para separador decimal)
    - não permite começar com vírgula
    - limita o comprimento a 3 caracteres (para evitar entradas excessivamente longas)
    """
    if texto == '':
        return True
    if texto.count(',') > 1:
        return False
    if texto[0] == ',':
        return False
    if len(texto) > 3:
        return False
    if all(c in '0123456789,' for c in texto):
        return True
    return False

def somente_numeros_peso(texto):
    """Valida se a string `texto` é um número aceitável para o Entry.
    Regras:
    - aceita string vazia (permite apagar o campo)
    - permite somente dígitos e no máximo uma vírgula (para separador decimal)
    - não permite começar com vírgula
    - limita o comprimento a 5 caracteres (para evitar entradas excessivamente longas)
    """
    if texto == '':
        return True
    if texto.count(',') > 1:
        return False
    if texto[0] == ',':
        return False
    if len(texto) > 5:
        return False
    if all(c in '0123456789,' for c in texto):
        return True
    return False

def calculadora_imc():
    try:
        peso = float(entrada1.get().replace(',','.'))
        altura = float(entrada2.get().replace(',','.'))
        if altura == 0 or peso == 0:
            texto_final1.config(text="Entre com valores válidos para altura e peso!", fg="red", bg='black')
            label_suporte.config(text="Altura e peso devem ser maiores que zero.", fg="red")
            quadro_tabela.pack_forget()
            texto_final2.config(text="")
            return
        
        altura_quadrado = altura ** 2
        
        IMC = peso / altura_quadrado
        
        if IMC < 18.5:
            resultado, cor = 'Abaixo do peso', '#ccff00'
        elif IMC <= 24.9:
            resultado, cor = 'Peso ideal', '#09ff00'
        elif IMC <= 29.9:
            resultado, cor = 'Sobrepeso', '#ffe600'
        elif IMC <= 34.9:
            resultado, cor = 'Obesidade grau 1', '#ffaa00'
        elif IMC <= 39.9:
            resultado, cor = 'Obesidade grau 2', '#ff6200'
        else:
            resultado, cor = 'Obesidade grau 3 (mórbida)', '#ff0000'
        
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
        label_suporte.config(text="Use números válidos (Ex: 70,5 e 1,75)", fg="red")

janela = tk.Tk()
janela.title('Calculadora de IMC')
janela.geometry('360x400')

vcmd_altura = (janela.register(somente_numeros_altura), '%P')
vcmd_peso = (janela.register(somente_numeros_peso), '%P')

texto = tk.Label(janela, text="Peso (kg):", font=('arial', 12)).pack(pady=5)
entrada1 = tk.Entry(janela, font=('arial', 11), validate='key', validatecommand=vcmd_peso)
entrada1.pack()
entrada1.focus()

texto = tk.Label(janela, text="Altura (m):", font=('arial', 12)).pack(pady=5)
entrada2 = tk.Entry(janela, font=('arial', 11), validate='key', validatecommand=vcmd_altura)
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