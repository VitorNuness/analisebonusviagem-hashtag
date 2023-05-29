import pandas as pd
from twilio.rest import Client

# Passo a passo da solução

account_sid = 'AC91f00088d55991676bcc763e6a446ccf'
auth_token = 'a215c8b7466f3e01c4ba9a075f648b86'
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"planilhas\{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        message = client.messages.create(
                              body=f"No mês de {mes} o vendedor {vendedor} bateu a meta com {vendas} vendas.",
                              from_='+13159225801',
                              to='+5514997061888'
                          )

        print(message.sid)
