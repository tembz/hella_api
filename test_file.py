from hella_api import HellaApi
from tokens import HELLA

api = HellaApi(HELLA)

get_group = api.methods(method='getGroups', user_id=1)

print(get_group)



