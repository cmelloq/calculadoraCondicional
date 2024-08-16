import tkinter as tk
from tkinter import ttk

# Função para gerenciar a seleção dos botões
def gerenciar_selecao(ferramenta):
    # Verifica se a ferramenta já está selecionada
    if ferramenta_selecionada.get() == ferramenta:
        # Se estiver selecionada, desmarque-a
        ferramenta_selecionada.set(None)
        atualizar_cores()
    else:
        # Caso contrário, selecione a ferramenta e atualize as cores
        ferramenta_selecionada.set(ferramenta)
        atualizar_cores()

# Função para atualizar a cor dos botões com base na seleção
def atualizar_cores():
    for ferramenta, botao in botoes_ferramentas.items():
        if ferramenta_selecionada.get() == ferramenta:
            # Aplica o estilo "pressionado" quando o botão está selecionado
            botao.config(bg="lightblue", relief=tk.SUNKEN)
        else:
            # Volta ao estilo normal quando o botão não está selecionado
            botao.config(bg="SystemButtonFace", relief=tk.RAISED)

# Função de cálculo (mesma lógica de antes)
def calcular_sequencia(numero_desejado, sequencia_final):
    numero_pre_calculo = numero_desejado - sum(sequencia_final)
    
    botoes_positivos = [16, 13, 7, 2]
    botoes_negativos = [-15, -9, -6, -3]
    
    resultado = []
    valor_atual = 0

    while valor_atual != numero_pre_calculo:
        if valor_atual < numero_pre_calculo:
            adicionado = False
            for botao in sorted(botoes_positivos, reverse=True):
                if valor_atual + botao <= numero_pre_calculo:
                    valor_atual += botao
                    resultado.append(f"+{botao}")
                    adicionado = True
                    break
            if not adicionado:
                break
        elif valor_atual > numero_pre_calculo:
            subtraido = False
            for botao in sorted(botoes_negativos):
                if valor_atual + botao >= numero_pre_calculo:
                    valor_atual += botao
                    resultado.append(f"{botao}")
                    subtraido = True
                    break
            if not subtraido:
                break

 # Aplicando a sequência final
    for move in sequencia_final:
        if move > 0:
            resultado.append(f"+{move}")  # Adiciona '+' explicitamente para números positivos
        else:
            resultado.append(str(move))  # Números negativos já têm o '-' automaticamente
        
        valor_atual += move  # Aplica o valor da sequência final ao cálculo

    return resultado, valor_atual

def calcular():
    try:
        numero_desejado = int(entry_numero.get())
        
        # Verifica se uma sequência manual foi inserida
        sequencia_manual = entry_sequencia_manual.get().strip()
        if sequencia_manual:
            try:
                # Converte a sequência manual em uma lista de números
                sequencia = [int(x.strip()) for x in sequencia_manual.split(',')]
            except ValueError:
                resultado_label.config(text="Sequência manual inválida. Use números separados por vírgula.")
                return
        else:
            # Usa a sequência da ferramenta selecionada
            ferramenta = ferramenta_selecionada.get()
            if ferramenta:
                sequencia = sequencias_finais[ferramenta]
            else:
                resultado_label.config(text="Selecione uma ferramenta ou insira uma sequência manual.")
                return
        
        # Calcula a sequência e o valor final após aplicar a sequência final
        resultado, valor_final = calcular_sequencia(numero_desejado, sequencia)
        
        # Double check: garantir que o valor final seja igual ao desejado
        if valor_final == numero_desejado:
            resultado_label.config(text=f"Resultado: {resultado}")
        else:
            resultado_label.config(text=f"Erro: Não foi possível atingir o valor solicitado. Valor obtido: {valor_final}")
    
    except ValueError:
        resultado_label.config(text="Por favor, insira um número válido.")

# Sequências finais predefinidas
sequencias_finais = {
    'Ferramenta 1': [-15, +7, +2],
    'Ferramenta 2': [-9, +13],
    'Ferramenta 3': [-6, +16]
}

# Interface gráfica
root = tk.Tk()
root.title("Calculadora de Sequências")
root.geometry("1100x600")
root.configure(bg="#e6f7ff")

# Fonte padrão
default_font = ("Monocraft", 12)

# Campo de entrada para o número desejado
entry_label = ttk.Label(root, text="Digite o número desejado:", font=default_font, background="#e6f7ff")
entry_label.pack(pady=10)

entry_numero = ttk.Entry(root, font=default_font)
entry_numero.pack(pady=5)

# Rótulo para escolher a sequência final
seq_label = ttk.Label(root, text="Escolha a sequência final ou digite a sua:", font=default_font, background="#e6f7ff")
seq_label.pack(pady=10)

# Variável para rastrear a ferramenta selecionada
ferramenta_selecionada = tk.StringVar()

# Frame para centralizar os botões de ferramentas
frame_sequencias = tk.Frame(root, bg="#e6f7ff")
frame_sequencias.pack(pady=10)

# Botões de escolha da sequência final com animação de pressionado
botoes_ferramentas = {}

botao_ferramenta1 = tk.Button(frame_sequencias, text="Ferramenta 1", font=default_font, 
                              command=lambda: gerenciar_selecao('Ferramenta 1'))
botao_ferramenta1.pack(side=tk.LEFT, padx=10)
botoes_ferramentas['Ferramenta 1'] = botao_ferramenta1

botao_ferramenta2 = tk.Button(frame_sequencias, text="Ferramenta 2", font=default_font, 
                              command=lambda: gerenciar_selecao('Ferramenta 2'))
botao_ferramenta2.pack(side=tk.LEFT, padx=10)
botoes_ferramentas['Ferramenta 2'] = botao_ferramenta2

botao_ferramenta3 = tk.Button(frame_sequencias, text="Ferramenta 3", font=default_font, 
                              command=lambda: gerenciar_selecao('Ferramenta 3'))
botao_ferramenta3.pack(side=tk.LEFT, padx=10)
botoes_ferramentas['Ferramenta 3'] = botao_ferramenta3

# Campo de entrada para a sequência final manual
manual_label = ttk.Label(root, text="Ou insira uma sequência manual: ", font=default_font, background="#e6f7ff")
manual_label.pack(pady=10)

entry_sequencia_manual = ttk.Entry(root, font=default_font)
entry_sequencia_manual.pack(pady=5)

# Botão para calcular
calcular_btn = ttk.Button(root, text="Calcular", command=calcular, style='TButton')
calcular_btn.pack(pady=20)

# Rótulo para mostrar o resultado
resultado_label = ttk.Label(root, text="Resultado: ", font=default_font, background="#e6f7ff")
resultado_label.pack(pady=10)

# Aplicando estilos aos botões
style = ttk.Style(root)
style.configure('TButton', font=('Monocraft', 12), padding=6)

root.mainloop()
