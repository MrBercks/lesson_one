sheet = [2,3,4,5,6,7]
print(sheet)

sheet.append('sheet')
print(sheet)

for i in sheet:
	print(i)
sheet.reverse()

for i in sheet:
	print(i)

del sheet[0]
sheet = sorted(sheet)

sheet.append('Python')
print(sheet[0])
print(sheet[-1])
print()
for i in sheet[1:4]:
	print(i)

print(len(sheet))
print()

count = 0
for i in sheet:
	if i == 6:
		print(count)
		break
	count = count + 1



