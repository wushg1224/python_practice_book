def make_album(singer_name, album_name, song_number = None):
    """ return to a dic includes singer name, album name and song #"""
    album_info = {'singer': singer_name, 'album': album_name}
    if song_number:
        album_info['song_number'] = song_number
        return album_info

album = make_album('毛不易','小王', song_number= 19)
print(album)
album = make_album('周杰伦', '夜的第七章')
print(album)
album = make_album('hoyomix', 'background music')
print(album)

def make_album(singer_name, album_name, song_number = None):
    """ return to a dic includes singer name, album name and song #"""
    album_info = {'singer': singer_name, 'album': album_name}
    return album_info

while True:
    print("\nPlease tell me singer name: ")
    print("enter 'q' at any time to quit")
    s_name = input("Singer name: ")
    if s_name == 'q':
        break
    a_name = input("Album name: ")
    if a_name == 'q':
        break
    album_infomation = make_album(s_name, a_name)
    print(f"\n{album_infomation}")
