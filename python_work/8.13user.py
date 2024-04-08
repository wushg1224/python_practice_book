def build_profile(first, last, **user_info):
    """"创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('cecilia','gao',
              location = 'sydney',
              job = 'radiographer',
              field = 'it')

print(my_profile)