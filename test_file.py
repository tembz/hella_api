''' В коде показаны два разных способа! '''
from hella_api import Handler, HellaApi
from tokens import HELLA

hella = Handler(HELLA)

get_sticker = hella.getSticker(product_id=1, sticker_id=None) #информация о стикер-паке

hella2 = HellaApi(HELLA)

get_groups = hella2.methods(method='getGroups', user_id=1) #информация о группах пользователя

#разработчик апи: vk.com/robert_meow, в случае непоняток апи обращаться к нему

#создатель модуля: vk.com/tembz, в случае багов библиотеки обращаться к нему

#получить токен от hella api можно в группе vk.com/hella_api
