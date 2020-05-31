def get_vat(payment, percent = 18):
		vat = round(payment / 100 * percent,2)
		return '\nСумма НДС составит: {}\n'.format(vat).upper()

ex = 0
while (ex < 1):
	try:
		payment = input('Введи сумму: ')
		payment = float(payment)

		percent = input('\nВведи ставку: ')
		percent = float(percent)

		ex = 1

	except (ValueError, TypeError):
		print("Введите именно цифры!\n")

result = get_vat(payment,percent)
print(result)







