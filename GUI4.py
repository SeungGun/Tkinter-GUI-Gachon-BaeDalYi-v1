from tkinter import *
import tkinter.messagebox
# 메인화면
myfile = open("person_Info.txt","a+")
win = Tk()
win.title('가천배달이 made by 태현,승건')
win.geometry('800x550+100+100')
win.resizable(False,False)

main = Frame(win,bg="#12EAFF",relief="solid",width=800,height=800)
register = Frame(win,bg="#12EAFF",relief="solid",width=800,height=800)
category = Frame(win,bg="gray",relief="solid",width=800,height=800)
bunsik = Frame(win,bg="gray",relief="solid",width=800,height=800)
chicken = Frame(win,bg="gray",relief="solid",width=800,height=800)
chicken_c1 = Frame(win,bg='gray',relief='solid',width=800,height=800)
pizza = Frame(win,bg='gray',relief='solid',width=800,height=800)
bunsik_r1 = Frame(win,bg="gray",relief="solid",width=800,height=800)
r1_pay = Frame(win,bg='gray',relief='solid',width=800,height=800)

for frame in (main,register, category,bunsik,chicken,bunsik_r1,r1_pay,pizza,chicken_c1):
    frame.grid(row=0, column=0,sticky="news")

class Person:
    def __init__(self):
        self.name = input_name.get()
        self.ID = input_id.get()
        self.PW = input_pw.get()
        self.addr = input_addr.get()

def raise_main():
    main.tkraise()
    input_id.delete(0,END)
    input_pw.delete(0,END)
    input_name.delete(0,END)
    input_addr.delete(0,END)
def raise_register():
    register.tkraise()
    ID.delete(0,END)
    PW.delete(0,END)

def raise_category():
    category.tkraise()

def raise_bunsik():
    bunsik.tkraise()

def raise_chicken():
    chicken.tkraise()

def raise_yup():
    bunsik_r1.tkraise()

def raise_r1pay():
    #r1_pay.tkraise()
    tkinter.messagebox.showinfo("주문","엽기떡볶이 주문이 완료되었습니다!\n감사합니다.")

def raise_pizza():
    pizza.tkraise()

def raise_gup():
    chicken_c1.tkraise()

def raise_c1pay():
    tkinter.messagebox.showinfo("주문","굽네치킨 주문이 완료되었습니다!\n감사합니다.")

#def reg_Info():
    # p1 = Person()
    # myfile.write(p1.ID + "  " + p1.PW + "\n")
    # myfile.close()
    # print(p1.ID, p1.PW)
def login():
    f = open("person_account.txt", 'r')
    f_info = open("person_Info.txt", 'r')
    key_ID = 0
    key_PW = 0
    flag = 0
    cnt = 0
    fail = 0
    line = f.read()
    line = line.split()
    for i in line:
        if i == ID.get():
            key_ID = key_ID + 1

        if i == PW.get():
            key_PW = key_PW + 1

        if key_ID == 1 & key_PW == 1:
            while True:
                f_info1 = f_info.readline()
                f_info2 = f_info1.split()
                #print(f_info2)
                if not f_info2: break
                for j in f_info2:
                    if j == ID.get():
                        flag = flag + 1

                    if j == PW.get():
                        flag = flag + 1

                    if flag == 2:
                        user = Person()
                        flag = 0
                        #print("일치하는 계정 존재")
                        for z in f_info2:
                            if cnt == 0:
                                #print("test_name")
                                user.name = z
                                #print(user.name)
                                cnt = cnt + 1
                            elif cnt == 1:
                                #print("test_ID")
                                user.ID = z
                                #print(user.ID)
                                cnt = cnt + 1
                            elif cnt == 2:
                                #print("test_PW")
                                user.PW = z
                                #print(user.PW)
                                cnt = cnt + 1
                            elif cnt == 3:
                                #print("test_addr")
                                user.addr = z
                                #print(user.addr)
                                cnt = cnt + 1
                        break
            # global global_name
            # global global_ID
            # global global_PW
            # global global_addr
            # global_name = user.name
            # global_ID = user.ID
            # global_PW = user.PW
            # global_addr = user.addr

            tkinter.messagebox.showinfo("로그인","로그인되었습니다.")
            fail = fail + 1
            raise_category()
            tkinter.messagebox.showinfo("회원 정보", "회원 이름 : {}\n회원 ID : {}\n회원 PW : {}\n회원 주소지 : {}".format(user.name,user.ID,user.PW,user.addr))
            print(user.name+" "+user.ID+" "+user.PW+" "+user.addr)
            break

    if(fail != 1):
        tkinter.messagebox.showinfo("로그인실패", "존재하지 않는 계정입니다.")

    f.close()

def uploadFile():
    Name = input_name.get()
    Id = input_id.get()
    Pw = input_pw.get()
    Addr = input_addr.get()
    myfile = open("person_account.txt","a+")
    myfile2 = open("person_account.txt","r")
    myfile3 = open("person_info.txt","a+")

    flag = 0
    f = Id+" "+Pw+"\n" #형식
    while True:
        line = str(myfile2.readline())
        #tkinter.messagebox.showinfo("result",line + ',' +f)

        if line == f:
            tkinter.messagebox.showinfo("알림","이미 있는 아이디이거나 비밀번호입니다!")
            flag = 1
            break

        if not line:
            break
    if flag == 0:
        myfile.write(f)
        myfile3.write(Name + " " + Id + " " + " " + Pw + " " + Addr + "\n")
        tkinter.messagebox.showinfo("회원가입","회원가입이 성공적으로 완료되었습니다.")

    myfile.close()
    myfile2.close()
    myfile3.close()


reg_btn = Button(register,text="가입하기",width=10,height=3,command=uploadFile)
reg_btn.place(x=250,y=300)


back_inregister = Button(register,text="로그인화면으로 가기",width=25,height=3,command=raise_main)
back_inregister.place(x=350, y=300)

# 메인화면 창
main_logo = PhotoImage(file="logo.PNG")
logo = Label(main, image=main_logo, width=600, height=250)
logo.place(x=100, y=10)

id_ex = Label(main, text="ID", bg="white", fg="Black", width=3, height=1)
id_ex.place(x=220, y=300)
ID = Entry(main, width=50)
ID.place(x=260, y=300)
pw_ex = Label(main, text="PW", bg="white", fg="black", width=3, height=1)
pw_ex.place(x=220, y=325)
PW = Entry(main, show='*', width=50)
PW.place(x=260, y=325)

login_btn = Button(main, text="Login", width="10", height=2, command=login)
login_btn.place(x=320, y=360)

reg_btn = Button(main, text="Register", width=10, height=2, command=raise_register)  # 회원가입 창으로 이동
reg_btn.place(x=420, y=360)

cr = Label(main,text="Made By 태현,승건",bg='white',fg='black')
cr.place(x=670,y=530)

#회원가입 창

reg_logo = Label(register,text="회원가입",relief="solid",borderwidth=2,bg="#4182EC",fg="white",width=30,height=3,font=('Arial',13))
reg_logo.place(x=250,y=10)

name = Label(register,text="이름",bg='white',fg='black',width=3,height=1)
name.place(x=200,y=100)

input_name = Entry(register,width=50)
input_name.place(x=230,y=100)

reg_id = Label(register,text="ID",bg="white",fg="black",width=3,height=1)
reg_id.place(x=200,y=150)

input_id = Entry(register,width=50)
input_id.place(x=230,y=150)

reg_pw = Label(register,text='PW',bg='white',fg='black',width=3,height=1)
reg_pw.place(x=200,y=200)

input_pw = Entry(register,width=50,show='*')
input_pw.place(x=230,y=200)

reg_addr = Label(register,text='Address(Not Including empty)',bg='white',fg='black',height=1)
reg_addr.place(x=58,y=250)

input_addr = Entry(register,width=65)
input_addr.place(x=230,y=250)

#reg_btn = Button(register,text="가입하기",width=10,height=3,command=reg_Info)
#reg_btn.place(x=250,y=300)

# 카테고리 창
category_logo = Label(category,text="음식 카테고리",relief="ridge",borderwidth=2,bg="#FFFF75",fg="red",width=30,height=3)
category_logo.place(x=300,y=10)

dis_line5 = Label(category,width=800,height=0,bg='white')
dis_line5.place(x=0,y=70)
back_inmain = Button(category,text="이전화면으로 돌아가기",width=30,height=3,command=raise_main)
back_inmain.place(x=280,y=300)

cat1 = Button(category,text="분식",command=raise_bunsik,width=10,height=4)
cat1.place(x=190,y=130)

cat2 = Button(category,text="치킨",command=raise_chicken,width=10,height=4)
cat2.place(x=340, y=130)

cat3 = Button(category,text="피자",command=raise_pizza,width=10,height=4)
cat3.place(x=490,y=130)

# 분식 창
bun_logo = Label(bunsik,text="분식",bg="#FFFF75",relief="ridge",borderwidth=2,fg='red',width=30,height=3)
bun_logo.place(x=300,y=10)

dis_line2 = Label(bunsik,width=0,height=800,bg="white")
dis_line2.place(x=153,y=0)

back_inbun = Button(bunsik,text="이전화면으로 돌아가기",command=raise_category,width=18,height=3)
back_inbun.place(x=10,y=10)

im1 = PhotoImage(file="logo2.png")
r1 = Label(bunsik,image=im1,height=132)
r1.place(x=190,y=110)
r1_btn = Button(bunsik,text="동대문엽기떡볶이 성남태평점\n★4.4 최소주문 14,000원 \n 43~53분",bg='white',width=25,height=5,command=raise_yup,relief="solid",font=('Arial',16))
r1_btn.place(x=370,y=110)

# 치킨 창
chic_logo = Label(chicken,text="치킨",bg="#FFFF75",fg='red',width=30,height=3,relief="ridge",borderwidth=2)
chic_logo.place(x=300,y=10)

dis_line3 = Label(chicken,width=0,height=800,bg="white")
dis_line3.place(x=153,y=0)

back_inchic = Button(chicken,text="이전화면으로 돌아가기",command=raise_category,width=18,height=3)
back_inchic.place(x=10,y=10)

im2 = PhotoImage(file="logo3.png")
c1 = Label(chicken,image=im2)
c1.place(x=190,y=110)

c1_btn = Button(chicken,text="굽네치킨 성남복정점\n★4.4 최소주문 15,000원\n 36~45분",bg='white',width=25,height=5,command=raise_gup,relief='solid',font=('Arial',16))
c1_btn.place(x=450,y=110)

#피자 창
piz_logo = Label(pizza,text="피자",bg="#FFFF75",fg='red',width=30,height=3,relief="ridge",borderwidth=2)
piz_logo.place(x=300,y=10)

dis_line4 = Label(pizza,width=0,height=800,bg="white")
dis_line4.place(x=153,y=0)

back_inpiz = Button(pizza,text="이전화면으로 돌아가기",command=raise_category,width=18,height=3)
back_inpiz.place(x=10,y=10)


# 분식 - 식당1 메뉴 창
yup = PhotoImage(file='logo2.png')
ph = Label(bunsik_r1,width=140,height=160)
ph["image"] = yup
ph.place(x=170,y=5)

dis_line = Label(bunsik_r1,width=0,height=800,bg="white")
dis_line.place(x=153,y=0)

back_inyup = Button(bunsik_r1,text="이전화면으로 돌아가기",command=raise_bunsik,width=18,height=3)
back_inyup.place(x=10,y=10)

yup_top = Label(bunsik_r1,text="동대문엽기떡볶이\n성남태평점\n★★★★☆4.4\n최근리뷰 378 | 최근사장님댓글 382",width=50,height=8,font=('Arial',13))
yup_top.place(x=335,y=5)

menu1 = Button(bunsik_r1,text='A set\n17,000원\n주문하기',command=raise_r1pay,width=20,height=5)
menu1.place(x=220,y=190)

yup1 = PhotoImage(file="YUPA.png")
aset = Label(bunsik_r1,image=yup1)
aset.place(x=400,y=170)

menu2 = Button(bunsik_r1,text='B set\n19,000원\n주문하기',command=raise_r1pay,width=20,height=5)
menu2.place(x=220,y=290)

yup2 = PhotoImage(file="yupb.png")
bset = Label(bunsik_r1,image=yup2,width=359,height=170)
bset.place(x=400,y=360)


# 치킨 - 식당1 메뉴 창
gup = PhotoImage(file='logo3.png')
ph2 = Label(chicken_c1,image=gup)
ph2.place(x=170,y=5)

dis_line6 = Label(chicken_c1,width=0,height=800,bg="white")
dis_line6.place(x=153,y=0)

back_ingup = Button(chicken_c1,text="이전화면으로 돌아가기",command=raise_chicken,width=18,height=3)
back_ingup.place(x=10,y=10)

gup_top = Label(chicken_c1,text='굽네치킨 성남복정점\n★★★★☆4.4\n최근리뷰 52 | 최근사장님댓글 0',width=35,height=8,font=('Arial',13))
gup_top.place(x=450,y=5)

menu3 = Button(chicken_c1,text="굽네 갈비천왕\n17,000원\n주문하기",command=raise_c1pay,width=20,height=5)
menu3.place(x=220,y=190)

menu4 = Button(chicken_c1,text="굽네 볼케이노\n17,000원\n주문하기",command=raise_c1pay,width=20,height=5)
menu4.place(x=220,y=350)

gup1 = PhotoImage(file='gup1.png')
m1 = Label(chicken_c1,image=gup1,height=160)
m1.place(x=400,y=170)

gup2 = PhotoImage(file='gup2.png')
m2 = Label(chicken_c1,image=gup2,height=170)
m2.place(x=410,y=350)


#피자 - 식당1 메뉴 창
ready = Label(pizza,text="준비중입니다.......\n나중을 기약하세요^^",bg="white",fg='gray',relief="sunken",width=30,height=5,font=('Arial',16))
ready.place(x=200,y=120)

main.tkraise()
win.mainloop()