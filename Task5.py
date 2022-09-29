"""
Дан словарь email-адресов студентов, в качестве ключа используется домен, а в качестве значения список имен.
Необходимо вывести все email-адреса в формате Имя@домен.
"""
emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
      	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
      	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
      	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
      	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
for name in emails['mgu.edu']:
	print(name + '@mgu.edu')

for name in emails['gmail.com']:
	print(name + '@gmail.com')

for name in emails['msu.edu']:
	print(name + '@msu.edu')

for name in emails['yandex.ru']:
	print(name + '@yandex.ru')

for name in emails['harvard.edu']:
	print(name + '@harvard.edu')

for name in emails['mail.ru']:
	print(name + '@mail.ru')

