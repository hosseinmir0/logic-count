# made by : hossein_mir0
# telegram id : hossein_mir0

vorodi = input('enter your text: ')
list_khali = []

for shomaresh in vorodi :
    if shomaresh not in list_khali :
        num = 0
        list_khali.append(shomaresh)
        for teadad in vorodi :
            if teadad == shomaresh :
                num += 1
        
        print (f'word is: {shomaresh} , counts is: {num}')
        
# filter repeated word
# is 👇🏽

# vorodi = input('enter your text: ')
# list_khali = []

# for shomaresh in vorodi :
#     if shomaresh not in list_khali :
#         num = 0
#         list_khali.append(shomaresh)
#         for teadad in vorodi :
#             if teadad == shomaresh :
#                 num += 1
#         if num >= 2 and teadad  :
#             print (f'word is: {shomaresh} , counts is: {num}')
