# Refazendo exercícios do curso de programação em Python da USP
# Projeto FizzBuzz.py
# Todo número divisivel por 3 será substituído por "Fizz"
# e todo divisível por 5 será por "Buzz"
# os que são simultaneamente divisivel por 3 e 5 serão substituídos por "FizzBuzz"

print("FizzBuzz")

numero = int(input("Digite o número máximo de iterações")) # até que número o usuário deseja que seja contado

contador = 0

while contador <= numero:
	
	if contador % 3 == 0 and contador % 5 == 0:
		print("FizzBuzz")

	elif contador % 3 == 0:
		print("Fizz")

	elif contador % 5 == 0:
		print("Buzz")

	else:
		print(contador)

	contador += 1

