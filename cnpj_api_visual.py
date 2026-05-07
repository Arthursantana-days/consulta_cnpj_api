# importar biblioteca visual
import customtkinter as ctk
# importar biblioteca de requisições
import requests

# aparência da janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window_cnpj = ctk.CTk()
window_cnpj.geometry ('800x600')
window_cnpj.title('Consulta CNPJ')

# Função Consulta CNPJ
def consulta_cnpj():
    cnpj = entry_cnpj.get().strip()

    if not cnpj:
        resultado.configure('CNPJ Inválido')
        return
    try:
        url = f'https://api.opencnpj.org/{cnpj}'
        res = requests.get(url)
        dados = res.json()
        informacao = (
                f'CNPJ: {dados["cnpj"]}\n'
                f'Razão Social: {dados["razao_social"]}\n'
                f'Situação Cadastral: {dados["situacao_cadastral"]}'
    )   
        resultado.configure(text = informacao)
    except: 
        resultado.configure(text = 'Erro na consulta. Verifique o CNPJ e tente novamente.', text_color = "#ff2c2c")

           


# Título da janela
titulo = ctk.CTkLabel(window_cnpj, text = 'Consulta de CNPJ', font =('Arial',22), text_color = "#6d188f")
titulo.pack(pady=10)

# Entrada de dados
entry_cnpj = ctk.CTkEntry(window_cnpj, placeholder_text = "Digite seu CNPJ", width = 400, height = 40, corner_radius=5)
entry_cnpj.pack(pady=20)

# botão
consultar = ctk.CTkButton(window_cnpj, text = "Consultar", width = 200, height = 40, fg_color = "#2d9c45", command= consulta_cnpj)
consultar.pack(pady=20)

# Resultado
resultado = ctk.CTkLabel(window_cnpj, text = 'Resultado', font =('Arial',12), text_color = "#1c8412")
resultado.pack(pady=10)
window_cnpj.mainloop()
