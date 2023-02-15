import re

emails =  [
    'm_akhmadi@kbtu.kz',
    'y_ruchanov%kbtu.kz143872396',
    'aidanaisnai@',
    'aidana@isnai.',
    'makhmadi@kbtu.kz'
]
pattern2 = r'^.+@[a-z] + \.[a-z]'
pattern3 = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
for i in emails:
    if re.match(pattern3, i):
        print(f'Email {i} is valid')
    else:
        print(f'Email {i} is not valid')
    