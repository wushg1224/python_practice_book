alien_0 = {
    'color' : 'green',
    'speed' : 'slow'
    }
#get method可以用于不存在的kay
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#如果指定的key[]不存在
#方括号表示法出错
print(alien_0['point'])