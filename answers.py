def get_unswer(question):
	question = question.lower()
	answers = {"привет":"\nИ тебе привет!\n", "как дела":"\nЛучше всех!\n", "пока":"\nУвидимся\n", "not found":"\nНе понял тебя :(\n"}
	if question in answers:
		return answers[question]
	else:
		return answers["not found"]

while (True):
	question = input("Напиши мне (: ")
	print (get_unswer(question))






