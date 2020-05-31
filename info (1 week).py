user_info = {'first_name':'', 'last_name':''}

user_info['first_name'] = input('Введите имя:')
user_info['last_name'] = input("Введите фамилию:")

print ('Привет, {} {}'.format(user_info['first_name'],user_info['last_name']))