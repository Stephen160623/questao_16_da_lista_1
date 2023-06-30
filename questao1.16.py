# Atribuição de variáveis
   
# Entrada de dados

Rf = float(input("Retorno do ativo sem risco: "))
Rm = float(input("Retorno da carteira de mercado: "))
Bi = float(input("Coeficiente de sensibilidade: "))

#Processamento de dados

Ri = Rf + Bi*(Rm-Rf)

# Saída de dados

print(f"O retorno esperado do ativo é {Ri}")