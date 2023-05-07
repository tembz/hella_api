from hella_api import HellaApi, Handler
from tokens import HELLA

api = HellaApi(HELLA)
api2 = Handler(HELLA)

#Option 1:
get_group = api.methods(method='getGroups', user_id=1)
print(get_group)

#Option 2:
get_group = api2.getGroups(user_id=1)
print(get_group)



