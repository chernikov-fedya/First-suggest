import vk_api
import openpyxl



my_token = 'vk1.a.vKG_r4RwJAUsQUg_vzRTFV-UNnBNFkwndc3M3YvSxqScmPUU7P_9NA50XZCvjHuXKv9bXI1NVpojSGgdDrIY_bYfoAkCF9U19KgNR7' \
           'r0qFYSe8CkyS0o3UMFcV2bhBNmX0OnaEYqIPWBjlxCz5zJr98ZFetlo6nTQKWB47yki5kqPRnZRqHvPLXJW-WnZArTMQyhb87lIMlCHLY' \
           'fil-wRg'
vk_session = vk_api.VkApi(token = my_token)
vk = vk_session.get_api()

list_groups = vk.groups.get(user_id = 800884715)['items']
print(list_groups)
name_group = vk.groups.getById(group_id = list_groups[0])[0]
print(name_group['name'])
    # wb = openpyxl.load_workbook("vk.xlsx")
    # wb = wb['groups']
    # sheet = wb
    # for i in range(len(list_groups)):
    #     sheet[i + 1][0].value = list_groups[i]
    # wb.save("vk.xlsx")
