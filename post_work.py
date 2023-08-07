import time

import vk_api
import openpyxl
import sys

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
    good_attachments = []
    wb = openpyxl.load_workbook("vk.xlsx")
    #wb = openpyxl.open("/Users/artem_1/Desktop/python/First-suggest/vk.xlsx")
    wb = wb['goods']
    sheet = wb
    count = 2
    a = ''
    print('Выберите позицию из списка товаров:\n')
    while a != 'None':
        a = str(sheet[count][0].value)
        if a != 'None':
            print(a)
            count += 1
    goods_length = count
    good = input('\nВведите название вещи\n')
    in_stock=0
    for i in range(1, goods_length):
        if good == str(sheet[i][0].value):
            in_stock = 1
            good_attachments.append(str(sheet[i][2].value))
            good_attachments.append(str(sheet[i][3].value))
            good_attachments.append(str(sheet[i][4].value))
            good_attachments.append(str(sheet[i][5].value))
            good_attachments.append(str(sheet[i][6].value))
            good_attachments.append(str(sheet[i][7].value))
            good_message = str(sheet[i][1].value)
            sender()
        elif good == 'Выйти' or good == 'выйти' or good == 'стоп' or good == 'stop' or good == 'exit':
            sys.exit()
    if in_stock == 0:
        print('\nТакого товара нет в наличии, выберите другой')
        requester()


def sender():
    list_groups = vk.groups.get(user_id=800884715)['items']
    for i in list_groups:
        try:
            print(vk.wall.post(owner_id = int(f'-{i}'), message = good_message +'\n\n'+ message_const,
                        attachments = good_attachments) + vk.groups.getById(group_id= i)[0]['name'])
            time.sleep(5)
        except Exception as e:
            name_group = vk.groups.getById(group_id= i)[0]
            print(e, name_group['name'])


while True:
    requester()
