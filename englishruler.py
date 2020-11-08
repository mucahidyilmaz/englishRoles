
def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += '' + tick_label
    print(line)


def draw_interval(center_length):
    if center_length > 0:  
        draw_interval(center_length - 1)  
        draw_line(center_length)  
        draw_interval(center_length - 1)  


def draw_ruler(cetvelUzunlugu, enUzunBölüt ):
    draw_line(enUzunBölüt , str(0))  
    for j in range(1, 1 + cetvelUzunlugu):
        draw_interval(enUzunBölüt  - 1)  
        draw_line(enUzunBölüt,str(j)) 


if __name__ == '__main__':
    draw_ruler(1, 5)

