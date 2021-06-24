import matplotlib.pyplot as plt

#Dados
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
meses1 = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']

ano19 = [109.577, 92.962, 98.027, 105.925, 113.293]
ano20 = [111.768, 93.597, 107.286, 114.908, 132.714]
ano21 = [135.277, 124.435, 188.372, 186.604, 162.345]

titulo = 'Mortes registradas por mês'
eixox = 'Meses'
eixoy = 'Mortes'

#Títulos
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(meses, ano19, label = '2019')
plt.plot(meses1, ano20, label = '2020')
plt.plot(meses, ano21, label = '2021')
plt.legend()
plt.show()
