import vk_api

my_token = 'vk1.a.vKG_r4RwJAUsQUg_vzRTFV-UNnBNFkwndc3M3YvSxqScmPUU7P_9NA50XZCvjHuXKv9bXI1NVpojSGgdDrIY_bYfoAkCF9U19KgNR7' \
           'r0qFYSe8CkyS0o3UMFcV2bhBNmX0OnaEYqIPWBjlxCz5zJr98ZFetlo6nTQKWB47yki5kqPRnZRqHvPLXJW-WnZArTMQyhb87lIMlCHLY' \
           'fil-wRg'

vk_session = vk_api.VkApi(token = my_token)

vk = vk_session.get_api()


cock = [135644682, 86195472, 130693663, 135471942, 92504944]

for j in range(50):
    for i in range(len(cock)):
        print(vk.wall.post(owner_id = -cock[i], message = 'зилибоба',
                    attachments = ['photo-33598391_457382619', 'photo-33598391_457382620']))