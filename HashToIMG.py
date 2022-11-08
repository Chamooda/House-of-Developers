import HackatonImageGenerator
import HackathonEncrypt
import mysql.connector
import base64
from PIL import Image
import io

user_count=HackatonImageGenerator.kitne_user()




imgName = HackatonImageGenerator.ImgGenerator(user_count)

def Hash_Assignment(user_count):
    
    hash1 = HackathonEncrypt.Encrypt(imgName)
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS test1;")
    mycursor.execute("USE test1;")
    mycursor.execute("CREATE TABLE IF NOT EXISTS hash_image (hash VARCHAR(200), name VARCHAR(30),image BLOB);")
    mydb.commit()




    # hash=616
    file=open(imgName,'rb').read()
    file=base64.b64encode(file)
    args=(hash1,imgName,file)
    query='INSERT INTO hash_image VALUES(%s,%s,%s)'
    mycursor.execute(query,args)
    mydb.commit()
        #Add the relation of imgName and haash
        


def Hash_To_IMAGE(hash):
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger"
    )
    mycursor = mydb.cursor()
    mycursor.execute("USE test1;")
    query1="SELECT image FROM hash_image WHERE name=%s;"
    val=(imgName,)
    mycursor.execute(query1,val)
    data=mycursor.fetchall()
    
    image1=data[0][0]
    binary_data=base64.b64decode(image1)
    image1=Image.open(io.BytesIO(binary_data))
    #image1.show()
    
imgName = HackatonImageGenerator.ImgGenerator(user_count)
hash1 = HackathonEncrypt.Encrypt(imgName)   
 
#Hash_Assignment(1)
# Hash_To_IMAGE(hash1)




"""mycursor.execute("INSERT INTO hash_image (hash,image) VALUES(hash,LOAD_FILE('C:/Users/agraw/Downloads/test.txt));')")
mydb.commit()    
Hash_Assignment(user_count)
"""