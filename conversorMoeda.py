import tkinter as tk
from moeda import apidolar

def dolar():
    cotacao = float(apidolar())
    reais = float(valor.get())
    conta = round(reais / cotacao ,2)
    mensagem = f' R$ {reais} reais compra-se $ {conta} dólares'
    resposta.config(text=mensagem)
    #return mensagem 

janela = tk.Tk()
janela.geometry('500x300')
janela.title('Aula 04 - Tkinter')
janela.configure(bg='#B4BEC9')

titulo = tk.Label(janela, text='Coversor de Reais para Dólar', font=('Verdana', 16), fg='#002333', bg='#B4BEC9')
titulo.pack(pady=10)

rotulo = tk.Label(janela, text='Digite o valor em Reais para converter:', font=('Verdana', 12), fg='#002333', bg='#B4BEC9')
rotulo.pack(pady=10)

valor = tk.Entry(janela, bg='#72F2EB', fg='#747F7F')
valor.pack(pady=10)

botao = tk.Button(janela, text='Converter' , command=dolar, bg='#00CCC0', fg='#002333')
botao.pack(pady=10)

resposta = tk.Label(janela, text='', font=('Verdana', 12), fg='#002333', bg='#B4BEC9')
resposta.pack(pady=10)

janela.mainloop()




