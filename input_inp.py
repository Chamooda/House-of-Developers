import mysql.connector
#import HashToIMG
import HackathonEncrypt
import HackatonImageGenerator


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS test1;")
mycursor.execute("USE test1;")
mycursor.execute("CREATE TABLE IF NOT EXISTS flappy_bird (user_id VARCHAR(20), password VARCHAR(20), score int(5), hash VARCHAR(1000));")
mydb.commit()



count=HackatonImageGenerator.kitne_user()
a=HackatonImageGenerator.ImgGenerator(count)
hash=HackathonEncrypt.Encrypt(a)


def inp():
    boo1=False
    use_id=input("Enter your username : ")
    passw=input("Enter password : ")
    mycursor.execute("SELECT user_id FROM flappy_bird;")
    result=mycursor.fetchall()
    comp=''
    compare=0
    for i in result:
        if str(i[0])==use_id: 
            boo1=True
    if boo1==False:       
        sql="INSERT INTO flappy_bird (user_id,password,score,hash) VALUES(%s,%s,%s,%s)"
        val=(use_id,passw,0,hash)
        mycursor.execute(sql,val)
        mydb.commit()
        log = "Login Successful"
        comp=input("Who do you want to compete with : ")
        sql3=("SELECT score FROM flappy_bird WHERE user_id=%s")
        val3=(comp,)
        mycursor.execute(sql3,val3)
        compare=mycursor.fetchall()[0][0]
    else:
        sql8=("SELECT user_id,password FROM flappy_bird WHERE user_id=%s")
        val8=(use_id,)
        mycursor.execute(sql8,val8)
        result3=mycursor.fetchall()
        if result3[0][1]==passw:
            log = "Login Successful"
            comp=input("Who do you want to compete with : ")
            sql3=("SELECT score FROM flappy_bird WHERE user_id=%s")
            val3=(comp,)
            mycursor.execute(sql3,val3)
            compare=mycursor.fetchall()[0][0]
        else:
            log = "Login Failed"
    credentials=[use_id,log,comp,compare]
    return credentials


def score(name,sco):
    sql="UPDATE flappy_bird SET score=%s WHERE user_id =%s"
    val=(sco,name)
    mycursor.execute(sql,val)
    mydb.commit()

def winner(use_id,sco,comp,compare):
    if sco>compare:
        print("Congratulations, you won your bet against ",comp)
        sql4=("SELECT INSTR(hash,' ') FROM flappy_bird WHERE user_id=%s")
        val4=(comp,)
        mycursor.execute(sql4,val4)
        space_pos=mycursor.fetchall()[0][0]
        sql5=("SELECT REVERSE(SUBSTR(REVERSE(hash),%s)) FROM flappy_bird WHERE user_id=%s")
        val5=(-space_pos,comp)
        mycursor.execute(sql5,val5)
        concat=mycursor.fetchall()[0][0]
        sql6=("UPDATE flappy_bird SET hash=SUBSTR(hash,%s) WHERE user_id=%s")
        val6=(space_pos,comp)
        mycursor.execute(sql6,val6)
        mydb.commit()
        sql7=("UPDATE flappy_bird SET hash=CONCAT(%s,hash) WHERE user_id=%s")
        val7=(concat,use_id)
        mycursor.execute(sql7,val7)
        mydb.commit()
    elif sco==compare:
        print("It's a Tie with ",comp)
    else:
        print("Sorry, you lost your bet against ",comp)





"""def dislayProfile():
    userid = input("Enter Username to view")
    stment = "SELECT hash FROM flappy_bird where user_id = %s"
    val = (userid,)
    mycursor.execute(stment,val)
    mydb.commit()

    hashls = mycursor.fetchall();
    
    for i in hashls:
        HashToIMG(i)"""





    
    
   

