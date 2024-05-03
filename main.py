from telebot import *
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import sqlite3
import datetime

        


abmarkaz="6247457720:AAHQGzpg3DospmU56lFGkFOtCrTp63B6gaU"
bot=TeleBot(abmarkaz)

class tanlov:
    def __init__(self,msg) -> None:
        self.jins=""
        self.yil=""
        self.viloyat=""
        self.qidiruv(msg)
    def qidiruv(self,msg):
        bot.send_message(msg.chat.id,"Qaysi jinsdagi odamni qidiramiz",reply_markup=gender)
        bot.register_next_step_handler(msg,self.q_jins)

    def q_jins(self,msg):
        if str(msg.text) in ["Yigit","Qiz"]:
            self.jins=str(msg.text)
            bot.send_message(msg.chat.id,"Nechanchi yillar orasidagi odamni qidiramiz",reply_markup=yillar)
            bot.register_next_step_handler(msg,self.q_vil)
        else:
            yoz(msg,"Noto'g'ri xabar yuborildi")
            yoz(msg,"Qaysi jinsdagi odamni qidiramiz",gender)
            bot.register_next_step_handler(msg,self.q_jins)

    def q_vil(self,msg):
        if str(msg.text) in ["1990-1995","1996-2000","2001-2005","2006-2010"]:
            self.yil=str(msg.text)
            bot.send_message(msg.chat.id,"Qaysi viloyat odamini qidiramiz",reply_markup=touches1)
            bot.register_next_step_handler(msg,self.q_qidir)
        else:
            yoz(msg,"Noto'g'ri xabar yuborildi")
            bot.send_message(msg.chat.id,"Nechanchi yillar orasidagi odamni qidiramiz",reply_markup=yillar)
            bot.register_next_step_handler(msg,self.q_vil)

    def q_qidir(self,msg):
        if str(msg.text) in ["Toshkent","Andijon","Fargona","Namangan","Jizzax","Sirdaryo","Samarqand","Qoraqalpoq","Qashqadaryo","Navoiy","Buxoro","Xorazm","Sirsaqlash"]:
            self.viloyat=str(msg.text)
            yil_kichik=int(self.yil.split("-")[0])-1
            yil_katta=int(self.yil.split("-")[1])+1
            conn=sqlite3.connect("data.db")
            if self.viloyat=="Aralash":
                baza=conn.execute(f"""SELECT id,tahallusi FROM flar WHERE jinsi='{self.jins}' AND yili>{yil_kichik} AND yili<{yil_katta}""")
            else:
                baza=conn.execute(f"""SELECT id,tahallusi FROM flar WHERE jinsi='{self.jins}' AND yili>{yil_kichik} AND yili<{yil_katta} AND viloyati='{self.viloyat}'""")
            conn.commit()
            try:
                txt="Tahalluslar:\n"
                for i in baza:
                    txt+=f"  {i[1]}\n"
                if txt=="Tahalluslar:\n":
                    txt="Bunday odamlar hali botda ro'yhatdan o'tishmagan"
                bot.send_message(msg.chat.id,txt,reply_markup=buyruqlar)
            except:
                bot.send_message(msg.chat.id,"Bunday odamlar hali botda ro'yhatdan o'tishmagan",reply_markup=buyruqlar)
        else:
            yoz(msg,"Noto'g'ri xabar yuborildi")
            bot.send_message(msg.chat.id,"Qaysi viloyat odamini qidiramiz",reply_markup=touches1)
            bot.register_next_step_handler(msg,self.q_qidir)


rm=ReplyKeyboardRemove()

gender = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
g1 = KeyboardButton("Yigit")
g2 = KeyboardButton("Qiz")

gender.add(g1)
gender.add(g2)

touches = ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
touches1 = ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
touch1 = KeyboardButton("Toshkent")
touch2 = KeyboardButton("Andijon")
touch3 = KeyboardButton("Farg'ona")
touch4 = KeyboardButton("Namangan")
touch5 = KeyboardButton("Jizzax")
touch6 = KeyboardButton("Sirdaryo")
touch7 = KeyboardButton("Samarqand")
touch8 = KeyboardButton("Qoraqalpoq")
touch9 = KeyboardButton("Qashqadaryo")
touch10 = KeyboardButton("Navoiy")
touch11 = KeyboardButton("Buxoro")
touch12 = KeyboardButton("Xorazm")
touch14=KeyboardButton("Aralash")

touches.add(touch1)
touches.add(touch2)
touches.add(touch3)
touches.add(touch4)
touches.add(touch5)
touches.add(touch6)
touches.add(touch7)
touches.add(touch8)
touches.add(touch9)
touches.add(touch10)
touches.add(touch11)
touches.add(touch12)


touches1.add(touch1)
touches1.add(touch2)
touches1.add(touch3)
touches1.add(touch4)
touches1.add(touch5)
touches1.add(touch6)
touches1.add(touch7)
touches1.add(touch8)
touches1.add(touch9)
touches1.add(touch10)
touches1.add(touch11)
touches1.add(touch12)
touches1.add(touch14)

buyruqlar=ReplyKeyboardMarkup(resize_keyboard=True)
buyruq1=KeyboardButton("Do'st qidirish")
buyruq2=KeyboardButton("Tahallusni o'zgartirish")
buyruq3=KeyboardButton("Viloyatni o'zgartirish")
buyruq4=KeyboardButton("Jinsni o'zgartirish")
buyruq5=KeyboardButton("Tug'ilgan yilni o'zgartirish")
buyruqlar.add(buyruq1)
buyruqlar.add(buyruq2)
buyruqlar.add(buyruq3)
buyruqlar.add(buyruq4)
buyruqlar.add(buyruq5)

yillar = ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
yil1 = KeyboardButton("1990-1995")
yil2 = KeyboardButton("1996-2000")
yil3 = KeyboardButton("2001-2005")
yil4 = KeyboardButton("2006-2010")

yillar.add(yil1)
yillar.add(yil2)
yillar.add(yil3)
yillar.add(yil4)


def yoz(msg,text,r_m=None):
    bot.send_message(msg.chat.id,text=text,reply_markup=r_m)

def yil(msg):
    try:
        if int(msg.text)>1900 and int(msg.text)<datetime.datetime.now().year:
            conn=sqlite3.connect("data.db")
            conn.execute(f"""UPDATE flar set yili ='{str(msg.text)}' WHERE f_id={msg.chat.id}""")
            conn.commit()
            bot.delete_message(msg.chat.id,msg.id-2)
            bot.delete_message(msg.chat.id,msg.id-1)
            bot.delete_message(msg.chat.id,msg.id)
            yoz(msg,"Yilingiz saqlandi")
            yoz(msg,"Botdan to'liq foydalanishingiz mumkin",buyruqlar)

        else:
            yoz(msg,"Yil noto'g'ri kiritildi.\nYilingizni qayta kiriting")
            bot.register_next_step_handler(msg,yil)
    except:
        yoz(msg,"Yil noto'g'ri kiritildi.\nYilingizni qayta kiriting")
        bot.register_next_step_handler(msg,yil)

def viloyat(msg):
    if str(msg.text) in ["Toshkent","Andijon","Fargona","Namangan","Jizzax","Sirdaryo","Samarqand","Qoraqalpoq","Qashqadaryo","Navoiy","Buxoro","Xorazm","Sirsaqlash"]:
        conn=sqlite3.connect("data.db")
        if str(msg.text)=="Farg'ona":
            viloyati="Fargona"
        else:
            viloyati=str(msg.text)
        conn.execute(f"""UPDATE flar set viloyati ='{viloyati}' WHERE f_id={msg.chat.id}""")
        conn.commit()
        bot.delete_message(msg.chat.id,msg.id-2)
        bot.delete_message(msg.chat.id,msg.id-1)
        bot.delete_message(msg.chat.id,msg.id)
        yoz(msg,"Viloyatingiz saqlandi")
        yoz(msg,"Yilingizni yuboring")
        bot.register_next_step_handler(msg,yil)
    else:
        yoz(msg,"Viloyat noto'g'ri kiritildi")
        yoz(msg,"Viloyatingizni tanlang",touches)
        bot.register_next_step_handler(msg,viloyat)


def jins(msg):
    if str(msg.text) in ["Yigit","Qiz"]:
        conn=sqlite3.connect("data.db")
        conn.execute(f"""UPDATE flar set jinsi ='{str(msg.text)}' WHERE f_id={msg.chat.id}""")
        conn.commit()
        bot.delete_message(msg.chat.id,msg.id-2)
        bot.delete_message(msg.chat.id,msg.id-1)
        bot.delete_message(msg.chat.id,msg.id)
        yoz(msg,"Jinsingiz saqlandi")
        yoz(msg,"Viloyatingizni tanlang",touches)
        bot.register_next_step_handler(msg,viloyat)
    else:
        yoz(msg,"jins noto'g'ri kiritildi")
        yoz(msg,"Jinsingizni tanlang",gender)
        bot.register_next_step_handler(msg,jins)

def tahallus(msg):
    tahallusi=str(msg.text)
    conn=sqlite3.connect("data.db")
    baza=conn.execute(f"""SELECT tahallusi from flar""")
    for i in baza:
        if i[0]==tahallusi:
            yoz(msg,"Bu tahallus band boshqa tahallus yuboring.")
            bot.register_next_step_handler(msg,tahallus)
    conn.execute(f"""INSERT INTO flar (f_id,tahallusi) VALUES ({msg.chat.id},'{tahallusi}')""")
    conn.commit()
    bot.delete_message(msg.chat.id,msg.id-2)
    bot.delete_message(msg.chat.id,msg.id-1)
    bot.delete_message(msg.chat.id,msg.id)
    yoz(msg,"Tahallusingiz saqlandi")
    yoz(msg,"Jinsingizni tanlang",gender)
    bot.register_next_step_handler(msg,jins)

def change_nickname(msg):
    tahallusi=str(msg.text)
    conn=sqlite3.connect("data.db")
    baza=conn.execute(f"""SELECT tahallusi from flar""")
    for i in baza:
        if i[0]==tahallusi:
            yoz(msg,"Bu tahallus band boshqa tahallus yuboring.")
            bot.register_next_step_handler(msg,change_nickname)
    conn.execute(f"""UPDATE flar set tahallusi ='{tahallusi}' WHERE f_id={msg.chat.id}""")
    conn.commit()
    bot.send_message(msg.chat.id,"Tahallus o'zgartirildi",reply_markup=buyruqlar)

def change_location(msg):
    viloyat=str(msg.text)
    conn=sqlite3.connect("data.db")    
    conn.execute(f"""UPDATE flar set viloyati ='{viloyat}' WHERE f_id={msg.chat.id}""")
    conn.commit()
    bot.send_message(msg.chat.id,"Viloyat o'zgartirildi",reply_markup=buyruqlar)

def change_gender(msg):
    jinsi=str(msg.text)
    conn=sqlite3.connect("data.db")    
    conn.execute(f"""UPDATE flar set jinsi ='{jinsi}' WHERE f_id={msg.chat.id}""")
    conn.commit()
    bot.send_message(msg.chat.id,"Jins o'zgartirildi",reply_markup=buyruqlar)
    
def change_birthday(msg):
    year=str(msg.text)
    conn=sqlite3.connect("data.db")    
    conn.execute(f"""UPDATE flar set yili ='{year}' WHERE f_id={msg.chat.id}""")
    conn.commit()
    bot.send_message(msg.chat.id,"Tug'ilgan yil o'zgartirildi",reply_markup=buyruqlar)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id,f"Salom {msg.from_user.username} \nChat botga hush kelibsiz!!!\nBu bot orqali ko'plab do'stlar va sevgingizni topishingiz mumkin!!!")
    conn=sqlite3.connect("data.db")
    flar=conn.execute(f"""SELECT f_id FROM flar""")
    baza=conn.execute(f"""SELECT tahallusi,jinsi,viloyati,yili FROM flar WHERE f_id={msg.chat.id}""")
    conn.commit()
    bormi="yoq"
    for i in flar:
        if i[0]==msg.chat.id:
            bormi="ha"
            for j in baza:
                yoz(msg,f"Siz avval ro'yhatdan o'tgansiz\nSizning tahallusingiz {j[0]}, \nJinsingiz {j[1]}, \nViloyatingiz {j[2]}, \nTug'ilgan yilingiz {j[3]}\n\n",buyruqlar)
                yoz(msg,"Botdan to'liq foydalanish haqidagi qo'llanma uchun /help buyrug'ini yuboring")
    if bormi=="yoq":
        bot.send_message(msg.chat.id,f"Botda sizning shaxsingiz sir saqlanadi. \nBoshqalar sizni tahallusingiz orqali tanishadi.\n\nMenga tahallusingzni yuboring")
        bot.register_next_step_handler(msg,tahallus)

@bot.message_handler(commands=['help'])
def yordam(msg):
    yoz(msg,"Do'stlarni topish uchun \nDo'st qidirish knopkasini bosing va qidirilayotgan do'stning \njinsi, \nyili, \nviloyatini yuboring. \nBot sizga to'g'ri keladigan do'stlar ro'yhatini yuboradi. \n\nSiz o'zingizga yoqqan tahallusdagi odamga habar yo'llashingiz mumkin. \n\nBuning uchun uning tahallusini yozamiz va ikki nuqta(:) qo'yib habarni yuboramiz.",buyruqlar)


@bot.message_handler(content_types=['text'])
def matn(msg):
    xabar=str(msg.text)
    if xabar=="Do'st qidirish":
        tanlov(msg)
    elif xabar=="Tahallusni o'zgartirish":
        bot.send_message(msg.chat.id,f"Yangi tahallusni yuboring",reply_markup=rm)
        bot.register_next_step_handler(msg,change_nickname)
    elif xabar=="Viloyatni o'zgartirish":
        bot.send_message(msg.chat.id,f"Viloyatingizni tanlang",reply_markup=touches)
        bot.register_next_step_handler(msg,change_location)
    elif xabar=="Jinsni o'zgartirish":
        bot.send_message(msg.chat.id,f"Jinsingizni tanlang",reply_markup=gender)
        bot.register_next_step_handler(msg,change_gender)
    elif xabar=="Tug'ilgan yilni o'zgartirish":
        bot.send_message(msg.chat.id,f"Tug'ilgan yilingizni yuboring",reply_markup=rm)
        bot.register_next_step_handler(msg,change_birthday)
    else:
        try:
            xabar=str(msg.text)
            f_tahallusi=xabar.split(":")[0]
            xabar=xabar.replace(f"{f_tahallusi}","")
            xabar=xabar.replace(":","")
            conn=sqlite3.connect("data.db")
            baza=conn.execute(f"""SELECT f_id FROM flar WHERE tahallusi='{f_tahallusi}'""")
            baza2=conn.execute(f"""SELECT tahallusi FROM flar WHERE f_id='{msg.chat.id}'""")
            conn.commit()
            for i in baza:
                for j in baza2:
                    txt=""
                    txt+=j[0]+":"+xabar
                    bot.send_message(int(i[0]),txt)
                    bot.send_message(msg.chat.id,"Xabar yuborildi")
        except:
            yoz(msg,"Bunday buyruq mavjud emas",buyruqlar)


bot.infinity_polling()