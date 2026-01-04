import tkinter as tk

saldo = 100 

def janelaPix():
    janelaPix = tk.Toplevel(janela)
    janelaPix.geometry("640x1038")
    janelaPix.title('Pix')
    janelaPix.configure(bg='black')

    entrada = tk.Entry(janelaPix, bg='gold')
    entrada.pack(pady=10)

    entrada2 = tk.Entry(janelaPix, bg='gold')
    entrada2.pack(pady=10)

    dinheiro = tk.Label(janelaPix, text=f'saldo: {saldo}', fg='gold', bg='black')
    dinheiro.place(x=22, y=13)

    def fazerPix():
        global saldo
        codigo = float(entrada.get())
        valor = float(entrada2.get())

        if saldo > valor:
            saldo = saldo - valor
            dinheiro.config(text=f'saldo: {saldo}')  
        else:
            dinheiro.config(text=f'Saldo insuficiente: {saldo}')

    
    butao = tk.Button(janelaPix, text='pix', command=fazerPix)
    butao.place(x=22, y=61)
    butao.configure(bg='gold')



def janelaPagar ():
    janelaPagar = tk.Tk()
    janelaPagar.geometry("640x1038")
    janelaPagar.title('Pagar')
    janelaPagar.configure(bg='black')

    entrada4 = tk.Entry(janelaPagar,bg='gold')
    entrada4.pack(pady = 10)



    dinheiro = tk.Label(janelaPagar,text=f'saldo: {saldo}',fg='gold',bg='black')
    dinheiro.place(x=22 , y=13)

    def pagarConta ():
        global saldo
        valor = float(entrada4.get())

        if saldo > valor:
            saldo = saldo - valor
            dinheiro.config(text=f'saldo: {saldo}')  
        else:
            dinheiro.config(text=f'Saldo insuficiente: {saldo}')

    butao = tk.Button(janelaPagar, text='pagar', command=pagarConta)
    butao.place(x=22, y=61)
    butao.configure(bg='gold')
    

    janela.mainloop()
def janelaTransferir ():
    janelaTransferir = tk.Tk()
    janelaTransferir.geometry("640x1038")
    janelaTransferir.title('Transferir')
    janelaTransferir.configure(bg='black')


    entrada5 = tk.Entry(janelaTransferir,bg='gold')
    entrada5.pack(pady = 10)

    entrada6 = tk.Entry(janelaTransferir,bg='gold')
    entrada6.pack(pady = 10)

    dinheiro = tk.Label(janelaTransferir,text=f'saldo: {saldo}',fg='gold',bg='black')
    dinheiro.place(x=22 , y=13)

    def transferir():
        global saldo
        codigo = float(entrada5.get())
        valor = float(entrada6.get())

        if saldo > valor:
            saldo = saldo - valor
            dinheiro.config(text=f'saldo: {saldo}')  
        else:
            dinheiro.config(text=f'Saldo insuficiente: {saldo}')         
        
    butao = tk.Button(janelaTransferir, text='trasferir', command=transferir)
    butao.place(x=22, y=61)
    butao.configure(bg='gold')

    janelaTransferir.mainloop()



def janelaDepositar ():
    janelaDepositar = tk.Tk()
    janelaDepositar.geometry("640x1038")
    janelaDepositar.title('Depositar')
    janelaDepositar.configure(bg='black')


    entrada3 = tk.Entry(janelaDepositar,bg='gold')
    entrada3.pack(pady = 10)

    dinheiro = tk.Label(janelaDepositar,text=f'saldo: {saldo}',fg='gold',bg='black')
    dinheiro.place(x=22 , y=13)

    def depositar():
        global saldo
        valor = float(entrada3.get())

        if valor >= 0:
            saldo = saldo + valor
            dinheiro.config(text=f'saldo: {saldo}')  
        else:
            dinheiro.config(text=f'valor insuficiente: {saldo}')

    butao = tk.Button(janelaDepositar, text='depositar', command=depositar)
    butao.place(x=22, y=61)
    butao.configure(bg='gold')

    janelaDepositar.mainloop()







janela = tk.Tk()
janela.geometry("640x1038")
janela.title('banco vip')
janela.configure(bg='black')


dinheiro = tk.Label(janela,text=f'saldo: {saldo}',fg='gold',bg='black')
dinheiro.place(x=22 , y=13)



butao = tk.Button(janela,text='pix',command=janelaPix)
butao.place(x=22 , y=61)
butao.configure(bg='gold')

butao2 = tk.Button(janela,text='pagar',command=janelaPagar)
butao2.place(x=183 , y=61)
butao2.configure(bg='gold')

butao3 = tk.Button(janela,text='transferir',command=janelaTransferir)
butao3.place(x=351 , y=61)
butao3.configure(bg='gold')

butao4 = tk.Button(janela,text='depositar',command=janelaDepositar)
butao4.place(x=519 , y=61)
butao4.configure(bg='gold')



janela.mainloop()
