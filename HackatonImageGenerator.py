import hashlib
from PIL import Image
import random
import mysql.connector
def kitne_user():    
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger"
    )
    mycursor = mydb.cursor()
    mycursor.execute("USE test1;")
    mycursor.execute("select count(*) from flappy_bird;")
    user_count=mycursor.fetchall()
    user_count=(int(user_count[0][0]))
    return user_count




def ImgGenerator(user_count):
    flag = False
    imag = Image.open("bird 2.png","r")
    rgba = imag.convert('RGBA')
    # pix = list(rgba.getdata())

    da_list = []

    # for i in pix:
    #     i = list(i)

    # rgba.putdata(pix)
    while(True):
        for i in range (1032):
            #da_string = str(i[0])+str(i[1])+str(i[2])+str(i[3])+"-"
            da_tuple = []
            for j in range (4):
                da_tuple.append(random.randint(0,255))
            
            da_list.append(tuple(da_tuple))


        rgba.putdata(da_list)
        rgba.save('transparent_image'+ f"{user_count}"+ ".png", 'PNG')
        #rgba.save(f'transparent_image.png'+{user_count}, 'PNG')
        

        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="tiger"
        )
        mycursor = mydb.cursor()
        mycursor.execute("USE test2;")
        mycursor.execute("select hash from hash_image")
        check_lst = mycursor.fetchall()
        for item in check_lst:
            flag = True
        if flag == False:
            break
    return ('transparent_image'+ f"{user_count}"+ '.png')


    

    # #5d4bc4deda63297907dbb0dceeb8400e6d7fc21aa52bc74778c62999fb807806





