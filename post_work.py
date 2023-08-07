import time
import vk_api
import openpyxl
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext

my_token = 'vk1.a.vKG_r4RwJAUsQUg_vzRTFV-UNnBNFkwndc3M3YvSxqScmPUU7P_9NA50XZCvjHuXKv9bXI1NVpojSGgdDrIY_bYfoAkCF9U19KgNR7' \
           'r0qFYSe8CkyS0o3UMFcV2bhBNmX0OnaEYqIPWBjlxCz5zJr98ZFetlo6nTQKWB47yki5kqPRnZRqHvPLXJW-WnZArTMQyhb87lIMlCHLY' \
           'fil-wRg'
vk_session = vk_api.VkApi(token = my_token)
vk = vk_session.get_api()

message_const = '''📍Самовывоз с примеркой: Москва, Малая Грузинская улица, 54 (м. Белорусская / м. Улица 1905г).
📦Отправка любой ТК по РФ.
🚶Собственная доставка по Москве с примеркой!'''


def requester():
    global good_attachments, good_message
    goods_length = len(combo['values'])
    good = combo.get()
    good_attachments = []
    wb = openpyxl.load_workbook("./vk.xlsx")
    wb = wb['goods']
    sheet = wb
    for i in range(2, goods_length+2):
        if good == str(sheet[i][0].value):
            good_attachments.append(str(sheet[i][2].value))
            good_attachments.append(str(sheet[i][3].value))
            good_attachments.append(str(sheet[i][4].value))
            good_attachments.append(str(sheet[i][5].value))
            good_attachments.append(str(sheet[i][6].value))
            good_attachments.append(str(sheet[i][7].value))
            good_message = str(sheet[i][1].value)
            print(good_message)
            sender()


def sender():
    list_groups = vk.groups.get(user_id=800884715)['items']
    time.sleep(5)
    for i in list_groups:
        try:
            print(vk.wall.post(owner_id=int(f'-{i}'), message=good_message + '\n\n' + message_const,
                               attachments=good_attachments))
            print('Успешно в ' + str(vk.groups.getById(group_id=i)[0]['name']))
            txt.insert(INSERT, 'Успешно в ' + str(vk.groups.getById(group_id=i)[0]['name'] + '\n'))
            window.update()
            time.sleep(5)
        except Exception as e:
            name_group = vk.groups.getById(group_id=i)[0]
            print(e, name_group['name'])
            txt.insert(INSERT, f"{e} {name_group['name']} \n")
            window.update()


wb = openpyxl.load_workbook("./vk.xlsx")
wb = wb['goods']
sheet = wb
count = 2
a = ''
goods_list = []
while a != 'None':
    a = str(sheet[count][0].value)
    if a != 'None':
        goods_list.append(a)
        count += 1


window = Tk()
window.title("Ёбка Вконтакте")
window.geometry('900x600')
l0 = Label( text='     \n   ', height=5)
l0.grid(column=0, row=0)
combo = Combobox(window, width=70)
combo['values'] = goods_list
combo.grid(column=0, row=1)
btn = Button(window, text="Начать рассылку", command=requester, height=2)
btn.grid(column=1, row=1)
l1 = Label( text='     \n   ', height=8)
l1.grid(column=0, row=2)
txt = scrolledtext.ScrolledText(window, width=120, height=20)
txt.grid(row=3, columnspan=2)
window.mainloop()
