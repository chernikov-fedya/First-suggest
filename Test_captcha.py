import time
import vk_api


my_token = 'vk1.a.vKG_r4RwJAUsQUg_vzRTFV-UNnBNFkwndc3M3YvSxqScmPUU7P_9NA50XZCvjHuXKv9bXI1NVpojSGgdDrIY_bYfoAkCF9U19KgNR7' \
           'r0qFYSe8CkyS0o3UMFcV2bhBNmX0OnaEYqIPWBjlxCz5zJr98ZFetlo6nTQKWB47yki5kqPRnZRqHvPLXJW-WnZArTMQyhb87lIMlCHLY' \
           'fil-wRg'
vk_session = vk_api.VkApi(token = my_token)
vk = vk_session.get_api()



def post(i = 0):
    for i in range(200):
        try:
            print(vk.wall.post(owner_id = -184644042, message = f"bad_message {i}", attachments = 'photo-33598391_457382619'))
        except Exception as e:
            print("Капчу хочу")
            time.sleep(5)
            post()


post()
