# number = int(input("Kvadreatning A tomonini kiriting \n>>> "))
# p = 4 * number
# y = number * number
#
# print('Kvadratning perimetri ', p)
# print('Kvadratning yuzasi ', y)

# a = int(input("A sonini kiriting: "))
# b = int(input("B sonini kiriting: "))
# print("A va B sonlarini o'rta arifmetigi: ", (a+b) // 2)

# a = int(input("ikki honali son kiriting: "))
# b = a % 10
# c = a // 10
#
# print(a, " sonining raqamalarini yeg'indisi: ", b + c)

# a = int(input("Uch xonali son kiriting: "))
# b = a // 100
# c = a % 100 // 10 * 10
# d = a % 10 * 100
# result = d+c+b
#
# print(type(result))

#
# telefon  = "men yangi 📱"
# oldim = "oldim"
# print(telefon, oldim)

# name = 'Nurilloh'
# familia = 'Ramazanov'
# fullname = f"{name} {familia}"
# fullname = fullname.upper()
# print(fullname.capitalize())

# mehmonlar = ['Ali', 'Vali', 'Sherxon', 'Hasan', 'Husan', 'Botir']
#
# for mehmon in mehmonlar:
#     print(mehmon == 'Sherxon')
#
# sonlar = list(range(11))
# print(sonlar)
# for son in sonlar:
#     print(f'{son} ning kvadrati {son ** 2} ga teng')

# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son ** 2)
#
# print(sonlar_kvadrati)

# dostlar = []
#
# for dost in range(5):
#     dostlar.append(input(f'{dost+1} - dostingizni ismini kiriting\n>>> '))
# print(dostlar)

# avtolar = ['bmw', 'mercedez', 'chevrolet', 'ferrari', 'porsche']
#
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# son = input("Juft son kiritin:\n>>> ")
# if int(son) % 2 == 0: print('Raxmat')
# else: print(f'{son} soni juft emas')

# user_age = int(input("Yoshingizni kiriting:\n>>> "))
# naxr = 0
# if user_age <= 4 and user_age >= 60: naxr = 0
# elif user_age < 18: naxr = 10000
# else: narx = 20000
#
# print(f"Sizga muzeyga kirish {narx} so'm")

# products = ['apple', 'laimon', 'banana', 'kiwi', 'abricos', 'pepsi', 'bread', 'milk', 'coffee', 'chessee']
# cart = []

# for product in range(5):
#     cart.append(input(f"{product+1} - Mahsulotni kiriting:\n>>> ").lower())
# for product in cart:
#     if product in products:
#         print(f'{product} dokonimizda bor')
#     else: print(f"{product} dokonimizda yoq")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x == y:
#     print(f"{x}={y}")
# elif x < y:
#     print(f'{x}<{y}')
# else:
#     print(f"{x}>{y}")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else:
#     print("Savatingiz bo'sh")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#
# savat = []
# for n in range(5):
#     savat.append(input(f'''Savatga {n + 1}-mahsulotni qo\'shing: '''))
#
#     bor_mahsulotlar = []
#     mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
#
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# users = ['alisher1983','aziza','yasina' 'umar']
#
# login = input("Yangi login tanlang: ")
#
# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")