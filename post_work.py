import time
import vk_api
import openpyxl
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext


my_token = 'vk1.a.vKG_r4RwJAUsQUg_vzRTFV-UNnBNFkwndc3M3YvSxqScmPUU7P_9NA50XZCvjHuXKv9bXI1NVpojSGgdDrIY_bYfoAkCF9U19Kg' \
           'NR7r0qFYSe8CkyS0o3UMFcV2bhBNmX0OnaEYqIPWBjlxCz5zJr98ZFetlo6nTQKWB47yki5kqPRnZRqHvPLXJW-WnZArTMQyhb87lIMl' \
           'CHLYfil-wRg'
vk_session = vk_api.VkApi(token = my_token)
vk = vk_session.get_api()

message_const = '''📍Самовывоз с примеркой: Москва, Малая Грузинская улица, 54 (м. Белорусская / м. Улица 1905г).
📦Отправка любой ТК по РФ.
🚶Собственная доставка по Москве с примеркой!'''


class Goods:
    def __int__(self, name, length):
        self.name = name
        self.length = length


def requester():
    global good_attachments, good_message
    goods_length = len(combo['values'])
    good = combo.get()
    print(good)
    print(goods_length)
    good_attachments = []
    wb = openpyxl.load_workbook("./vk.xlsx")
    wb = wb['goods']
    sheet = wb
    for i in range(1, goods_length + 1):
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
            txt = scrolledtext.ScrolledText(window, width=60, height=20)
            txt.grid(column=0, row=1)
            txt.insert(INSERT, 'Успешно в ' + str(vk.groups.getById(group_id=i)[0]['name']))
            time.sleep(5)
        except Exception as e:
            name_group = vk.groups.getById(group_id=i)[0]
            print(e, name_group['name'])
            txt = scrolledtext.ScrolledText(window, width=60, height=20)
            txt.grid(column=0, row=1)
            txt.insert(INSERT, f"{e} {name_group['name']}")


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


def goods_length(goods_list): return len(goods_list)



window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('900x600')
combo = Combobox(window)
combo['values'] = goods_list
combo.grid(column=0, row=0)
btn = Button(window, text="Начать рассылку", command=requester)
btn.grid(column=1, row=0)
txt = scrolledtext.ScrolledText(window, width=60, height=20)
txt.grid(column=0, row=1)
window.mainloop()
