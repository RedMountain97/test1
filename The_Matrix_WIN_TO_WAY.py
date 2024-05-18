
from termcolor import colored, cprint

init()
#print("\33[92m" +  "on_light_green")
#print("\33[32m" +  "on_light_green")

#print("\033[38;5;28m " + "тыц")
#print("\033[38;5;46m  " + "тыц")

list_of_colors = ["\33[38;5;46m","\33[38;5;40m", "\33[38;5;10m",
                  "\33[38;5;34m", "\33[38;5;2m","\33[38;5;28m",
                  "\33[38;5;22m","\33[38;5;239m","\33[38;5;235m"]
list_of_colors.reverse()

dict_template = {}
random.choice("الروبوتالمتكلمبرغرمصنععداءكوبيتسألعابفانيامصاصةأكلالكثيرمنالبراغيثجلسعلىمقاعدالبدلاءوتوفي")
mas1 = []
#alfa_string = "впрвкщпшк-0у94546е5о46г58и4т6895г486г854ь09568шь905054пклдопшпаьвлдпроыкз9"
#alfa_string = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя12345678"
space_string = "                                                                          "
alfa_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKL"
first_string = ""
space_list = list(space_string)
list_of_random_holes_position = []


def mainloop(alphabet, mas1):
    while True:
        mas1 = create_first_string(alphabet, mas1)
        #print(mas1[-1])
        if len(mas1) < 19:
            drow(mas1)
            time.sleep(1)
            os.system('CLS')
        else:
            #print(mas1[-1])
            mas1 = create_أ(mas1)
            mas1 = create_hole(alphabet, mas1)
            #print(mas1[-1])
            drow(mas1)
            mas1 = restore_lang(mas1)
            time.sleep(1)
            os.system('CLS')


def create_first_string(alphabet, mas1):
    temporary_list_for_dicts = []
    list_of_random_symbol = []
    list_of_random_position = []
    for j in range(random.randint(5, 10)):
        list_of_random_symbol.append(random.choice(alphabet))
        list_of_random_position.append(random.randint(0, len(alphabet)-1))
    if len(mas1) == 0:
        for k in range(len(alphabet)):
            temporary_list_for_dicts.append({k: [" ", 8]})
        mas1.append(temporary_list_for_dicts)
        for h in range(len(list_of_random_position)):
            for z in mas1:
                for p in z:
                    for o in p:
                        if o == list_of_random_position[h]:
                            p[o] = [list_of_random_symbol[h], 8]


        temporary_list_for_dicts = []
        return mas1
    else:

        last_mas_string = copy.deepcopy(mas1[-1])
        # Тут надо найти символ, если он записан.
        # Понизить счётчик цвета. Но проверку на 0 замутить!
        for every_dict in last_mas_string:
            for key in every_dict:
                if every_dict[key][0] != " ":
                    if every_dict[key][1] > 0:
                        every_dict[key][1] = every_dict[key][1] - 1
                    else:
                        every_dict[key][1] = 0



        for h in range(len(list_of_random_position)):
            for z in last_mas_string:
                for p in z:
                        if p == list_of_random_position[h]:
                            z[p] = [list_of_random_symbol[h], 8]
        mas1.append(last_mas_string)
        temporary_list_for_dicts = []
        return mas1





def create_hole(alphabet,mas1):
    list_of_random_holes_position = []
    sum_first_str = ''
    for j in range(random.randint(0, 3)):
        list_of_random_holes_position.append(random.randint(0,len(alphabet)-1))
    #print(list_of_random_holes_position)
    first_string_with_hole_list = list(mas1[-1])
    for j in range(len(list_of_random_holes_position)):
        first_string_with_hole_list[list_of_random_holes_position[j]] = " "
    #print(first_string_with_hole_list)
    #first_string_with_hole_list
    for s in first_string_with_hole_list:
        sum_first_str = sum_first_str + s
    mas1.pop(-1)
    mas1.append(sum_first_str)
    #print(sum_first_str)
    return mas1

def create_أ(mas1):
    mas_with_أ = []
    for string in mas1:
        sum_str = ""
        string_list = list(string)
        for j in range(len(string_list)):
            if string_list[j] != " ":
                doom = random.randint(0,95)
                if doom == 95:
                    string_list[j] = random.choice("الروبوتالمتكلمبرغرمصنععداءكوبيتسألعابفانيامصاصةأكلالكثيرمنالبراغيثجلسعلىمقاعدالبدلاءوتوفي")
            else:
                pass
        for k in string_list:
            sum_str = sum_str + k
        # Тут придётся сделать другой массив
        mas_with_أ.append(sum_str)
    return mas_with_أ

def restore_lang(mas1):
    mas_with_restore = []
    for string in mas1:
        sum_str = ""
        string_list = list(string)
        for j in range(len(string_list)):
            if string_list[j] in \
                    "الروبوتالمتكلمبرغرمصنععداءكوبيتسألعابفانيامصاصةأكلالكثيرمنالبراغيثجلسعلىمقاعدالبدلاءوتوفي":
                doom = random.randint(0, 5)
                if doom == 5:
                    string_list[j] = random.choice(alfa_string)
            else:
                pass
        for k in string_list:
            sum_str = sum_str + k
        # Тут придётся сделать другой массив
        mas_with_restore.append(sum_str)
    return mas_with_restore




def drow(mas1):
    mas1.reverse()
    for mas_of_dict in mas1:
        for again_dict in mas_of_dict:
            for key in again_dict:
                print(list_of_colors[again_dict[key][1]],again_dict[key][0] ,end= "")
        print("\n")
    mas1.reverse()

mainloop(alfa_string, mas1)


