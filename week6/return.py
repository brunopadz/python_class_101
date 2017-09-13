def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

name = input('Digite seu nome: ')

print(greet(en), name)
print(greet(es), name)
print(greet(fr), name)


# if type(name) != str:
#     print(greet(en),name)
#     print(greet(es),name)
#     print(greet(fr),name)
# else:
#     print('Digite seu nome!')
#     quit()
