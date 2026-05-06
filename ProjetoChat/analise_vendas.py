import pandas as pd

df = pd.read_csv("dados_vendas.csv")

def categorizar(valor):
    if valor < 200:
        return("Baixo")
    elif valor <=600:
        return("Médio")
    else:
        return("Alto")

df["categoria"] = df["valor"].apply(categorizar)

faturamento_categoria = df.groupby("categoria")["valor"].sum()
faturamento_categoria = faturamento_categoria.reset_index().sort_values(by="valor", ascending=False)


faturamento_categoria.to_csv("faturamento_categoria.csv", index=False)

quantidade_vendas = df.groupby("categoria")["valor"].count()
quantidade_vendas = quantidade_vendas.reset_index(name="quantidade").sort_values(by="quantidade", ascending=False)
quantidade_vendas.to_csv("quantidade_vendas.csv", index=False)

relatorio = df.groupby("categoria")["valor"].agg(quantidade="count", faturamento="sum")
relatorio["ticket_medio"] = relatorio["faturamento"] / relatorio["quantidade"]
relatorio = relatorio.reset_index().sort_values(by="faturamento", ascending=False)

relatorio.to_csv("relatorio.csv", index=False)




