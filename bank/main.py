import sqlite3

conn=sqlite3.connect("bank.db")

cursor=conn.cursor()
#connecting db

# cursor.execute(f"insert into Account(name,phone,aadhar,dob,gender,address,acc_type,amount,account_num)values('sadhana',9121603136,125678901267,'13-10-2002','FEMALE','hyd','savings',500,1212121212)")
# conn.commit()

# cursor.execute(''' Create Table Account(
#                name varchar(30) not null, phone number(10) check(length(phone=10)),
#                aadhar number(12) unique not null,
#                dob date,
#                address varchar(100) not null,
#                account_num INTEGER PRIMARY KEY AUTOINCREMENT,
#                gender varchar(7),
#                pin number(4) default(0),
#                amount number(8,2),
#                acc_type varchar(10) not null) ''')

def acc_creation(name,phone,dob,address,aadhar,gender,acc_type):
    cursor.execute(f"insert into Account(name,phone,dob,address,aadhar,gender,acc_type,amount)values('{name}',{phone},'{dob}','{address}',{aadhar},'{gender}','{acc_type}',500)")

    conn.commit()
    print("acc created successfully")

def pin_generate(acc,pin,c_pin):
    # data=cursor.execute(f"select * from Account where account_num={acc}")
    # print(data)
    if pin==c_pin:
        cursor.execute(f"update Account set pin={pin} where account_num={acc}")
        conn.commit()
        print("successfully pin have set")
    else:
        print("pin and confirm pin dont match")

def balance(acc,pin):
    data=cursor.execute(f"select * from Account where account_num={acc}")
    result=data.fetchone()

    #print()
    if pin==result[-3]:
        print(f"balance is {result[-2]}")
    else:
        print("invalid pin")
def deposit(acc,pin):
    data=cursor.execute(f"select * from Account where account_num={acc}")
    var=data.fetchone()
    if pin==var[-3]:
        amt=float(input("paisa honaaa"))
        if amt>=100 and amt<=1000:
            money=var[-2]
            cursor.execute(f"update Account set amount={amt+money} where account_num={acc}")
            conn.commit()
            print("sab barabar")
        else:
            print("invalid amt")
    else:
        print("invalid input")

def withdrawl(acc,pin):
    data=cursor.execute(f"select * from Account where account_num={acc}")
    var=data.fetchone()
    if pin==var[-3]:
        money=var[-2]
        amt=float(input("enter the amt:"))
        if amt<=var[-2] and amt<=1000 and amt>=100:
            cursor.execute(f"update Account set amount={money-amt} where account_num={acc}")
            conn.commit()
            print(f"{amt} has been withdrawed successfully")
        else:
            print("invalid amt")
    else:
        print("invalid input")

def acc_transfer(from_acc,to_acc,pin):
    data=cursor.execute(f"select * from Account where account_num={from_acc}")
    from_account=data.fetchone()
    if pin==from_account[-3]:
        amt=float(input("enter the money:"))
        if amt<=from_account[-2] and amt>=100:
            cursor.execute(f"update Account set amount={from_account[-2]-amt} where account_num={from_acc}")
            conn.commit()

            data1=cursor.execute(f"select * from Account where account_num={to_acc}")
            to_account=data1.fetchone()

            cursor.execute(f"update Account set amount={to_account[-2]+amt} where account_num={to_acc}")
            conn.commit()
            print("amt transfered successfully")
        else:
            print("invalid amt")
    else:
        print("invalid input")

print("*"*20)
user_input=int(input('''welcome to SBI\n choose the below options\n1) Account Creation\n2) Pin generation\n3) Balance Enquiry\n4) Withdrawl\n5) Deposit\n6) Account Transfer\n'''))
    #print(user_input)
if user_input==1:
    print("thanks for choosing our bank:")
    name=input("enter your name:")
    dob=input("enter dob:")
    phone=int(input("enter phone number:"))
    address=input("enter your address:")
    aadhar=input("enter your aadhar:")
    gender=input("enter your gender:")
    acc_type=input("enter your acctype:")
    acc_creation(name,phone,dob,address,aadhar,gender,acc_type)
elif user_input==2:
    print("******generate your pin******")
    acc=int(input("enter your acc number:"))
    pin=int(input("enter your pin:"))
    c_pin=int(input("confirm pin:"))
    pin_generate(acc,pin,c_pin)
elif user_input==3:
    acc=int(input("enter acc number:"))
    pin=int(input("enter your pin: "))
    balance(acc,pin)
elif user_input==4:
    acc=int(input("enter acc number:"))
    pin=int(input("enter your pin: "))
    deposit(acc,pin)
elif user_input==5:
    acc=int(input("enter acc number:"))
    pin=int(input("enter your pin: "))
    withdrawl(acc,pin)
elif user_input==6:
    from_acc=int(input("enter from_acc number:"))
    to_acc=int(input("enter to_acc number:"))
    pin=int(input("enter your pin:"))
    acc_transfer(from_acc,to_acc,pin)

else:
    quit()