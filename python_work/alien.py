#字典
alien_0={'color': 'green','points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0={'color': 'green','points': 5}
new_points = alien_0['points']
print(f'You just earned {(new_points)} points!')


#改变
print(alien_0)
alien_0['x_position']= 0 
alien_0['y_position']= 25 
print(alien_0)

#添加
alien_1= {} 
alien_1['color']='green'
alien_1['points']= 5 
print(alien_1)
print(f'The alien is {alien_1['color']}.')
alien_1['color']='yellow'
print(f'The alien is now {alien_1['color']}.')


alien_2 = {'x_position': 0 , 'y_position' : 25 ,'speed' : "medium"}
alien_2['speed']= 'fast'
print(f'Original position: {alien_2['x_position']}')
#向右移动alien
#根据speed将alien向右移动多远
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2 
else:
    x_increment= 3
#新位置是旧位置加上increments
alien_2['x_position'] = alien_2['x_position'] + x_increment
print(f"New position: {alien_2['x_position']}")

#删除
del alien_0['points']
print(alien_0)
