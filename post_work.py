import vk_api
import openpyxl

my_token = 'vk1.a.vKG_r4RwJAUsQUg_vzRTFV-UNnBNFkwndc3M3YvSxqScmPUU7P_9NA50XZCvjHuXKv9bXI1NVpojSGgdDrIY_bYfoAkCF9U19KgNR7' \
           'r0qFYSe8CkyS0o3UMFcV2bhBNmX0OnaEYqIPWBjlxCz5zJr98ZFetlo6nTQKWB47yki5kqPRnZRqHvPLXJW-WnZArTMQyhb87lIMlCHLY' \
           'fil-wRg'
vk_session = vk_api.VkApi(token = my_token)
vk = vk_session.get_api()

message_const = '''📍Самовывоз с примеркой: Москва, Малая Грузинская улица, 54 (м. Белорусская / м. Улица 1905г).
📦Отправка любой ТК по РФ.
🚶Собственная доставка по Москве с примеркой!'''

def Excel_groups():
    global groups_list
    groups_list = []
    wb = openpyxl.open("/Users/artem_1/Desktop/python/First-suggest/vk.xlsx")
    wb = wb['groups']
    sheet = wb
    count = 2
    a = ''
    print('Группы:')
    while a != 'None':
        a = str(sheet[count][0].value)
        if a != 'None':
            groups_list.append(str(sheet[count][1].value))
            print(a)
    #Проверить правильно ли считывает
        count +=1 
    group_length = len(groups_list)
    print(f'Длина таблицы = {group_length} строк')


def Requester():
    global good_attachments, good_message
    good_attachments = []
    wb = openpyxl.open("/Users/artem_1/Desktop/python/First-suggest/vk.xlsx")
    wb = wb['goods']
    sheet = wb
    count = 2
    a = ''
    print('Тщвары:')
    while a != 'None':
        a = str(sheet[count][0].value)
        if a != 'None':
            print(a)
            count += 1
    goods_length = count
    good = input('Введите название вещи')
    for i in range(1, goods_length):
        if good == str(sheet[i][0].value):
            good_attachments.append(str(sheet[i][2].value))
            good_attachments.append(str(sheet[i][3].value))
            good_attachments.append(str(sheet[i][4].value))
            good_attachments.append(str(sheet[i][5].value))
            good_attachments.append(str(sheet[i][6].value))
            good_attachments.append(str(sheet[i][7].value))
            good_message = str(sheet[i][1].value)


def Sender():
    for i in groups_list:
        print(vk.wall.post(owner_id = int(f'-{i}'), message = good_message +'\n\n'+ message_const,
                        attachments = good_attachments))

Excel_groups()
Requester()
Sender()