from tkinter import *
import tkinter.messagebox as tmsg
import time


val0='O'
val1='X'
choose=0
temp=0
lst=['']*10
res=0
name1=None
name2=None
def check1():
    global choose
    choose+=1
    b1()
    
def check2():
    global choose
    choose+=1
    b2()
def check3():
    global choose
    choose+=1
    b3()
  
def check4():
    global choose
    choose+=1
    b4()
  
def check5():
    global choose
    choose+=1
    b5()
  
def check6():
    global choose
    choose+=1
    b6()
  
def check7():
    global choose
    choose+=1
    b7()
def check8():
    global choose
    choose+=1
    b8()
  
def check9():
    global choose
    choose+=1
    b9()
  

  

def check_1():
    time.sleep(0.5)
    global b_3,lst,b_4,b_5,b_6,b_7,b_8,b_9,b_10,b_11
    r1=lst[1]+lst[2]+lst[3]
    r2=lst[4]+lst[5]+lst[6]
    r3=lst[7]+lst[8]+lst[9]
    c1=lst[1]+lst[4]+lst[7]
    c2=lst[2]+lst[5]+lst[8]
    c3=lst[3]+lst[6]+lst[9]
    d1=lst[1]+lst[5]+lst[9]
    d2=lst[3]+lst[5]+lst[7]
    v='XXX'
    
    if r1==v:
        print("ROW 1")
        b_3=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_3.place(x=120,y=110)
        b_4=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_4.place(x=215,y=110)
        b_5=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_5.place(x=310,y=110)
    elif r2==v:
        b_6=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_6.place(x=120,y=205)
        b_7=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_7.place(x=215,y=205)
        b_8=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_8.place(x=310,y=205)
    elif r3==v:
        b_9=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_9.place(x=120,y=300)
        b_10=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_10.place(x=215,y=300)
        b_11=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_11.place(x=310,y=300)
    
    elif c1==v:
        b_3=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_3.place(x=120,y=110)
        b_6=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_6.place(x=120,y=205)
        b_9=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_9.place(x=120,y=300)
    elif c2==v:
        b_4=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_4.place(x=215,y=110)
        b_7=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_7.place(x=215,y=205)
        b_10=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_10.place(x=215,y=300)
    elif c3==v:
        b_5=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_5.place(x=310,y=110)
        b_8=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_8.place(x=310,y=205)
        b_11=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_11.place(x=310,y=300)
    
    elif d1==v:
        b_3=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_3.place(x=120,y=110)
        b_7=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_7.place(x=215,y=205)
        b_11=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_11.place(x=310,y=300)
    else:
        b_5=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_5.place(x=310,y=110)
        b_7=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_7.place(x=215,y=205)
        b_9=Button(root2,bg="orange",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_9.place(x=120,y=300)
        
        
    
def check_2():
    time.sleep(0.5)
    global b_3,lst,b_4,b_5,b_6,b_7,b_8,b_9,b_10,b_11
    r1=lst[1]+lst[2]+lst[3]
    r2=lst[4]+lst[5]+lst[6]
    r3=lst[7]+lst[8]+lst[9]
    c1=lst[1]+lst[4]+lst[7]
    c2=lst[2]+lst[5]+lst[8]
    c3=lst[3]+lst[6]+lst[9]
    d1=lst[1]+lst[5]+lst[9]
    d2=lst[3]+lst[5]+lst[7]
    
    v='OOO'
    if r1==v:
        print("ROW 1")
        b_3=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_3.place(x=120,y=110)
        b_4=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_4.place(x=215,y=110)
        b_5=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_5.place(x=310,y=110)
    elif r2==v:
        b_6=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_6.place(x=120,y=205)
        b_7=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_7.place(x=215,y=205)
        b_8=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_8.place(x=310,y=205)
    elif r3==v:
        b_9=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_9.place(x=120,y=300)
        b_10=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_10.place(x=215,y=300)
        b_11=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_11.place(x=310,y=300)
    
    elif c1==v:
        b_3=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_3.place(x=120,y=110)
        b_6=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_6.place(x=120,y=205)
        b_9=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_9.place(x=120,y=300)
    elif c2==v:
        b_4=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_4.place(x=215,y=110)
        b_7=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_7.place(x=215,y=205)
        b_10=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_10.place(x=215,y=300)
    elif c3==v:
        b_5=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_5.place(x=310,y=110)
        b_8=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_8.place(x=310,y=205)
        b_11=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_11.place(x=310,y=300)
    
    elif d1==v:
        b_3=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_3.place(x=120,y=110)
        b_7=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_7.place(x=215,y=205)
        b_11=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_11.place(x=310,y=300)
    else:
        b_5=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_5.place(x=310,y=110)
        b_7=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_7.place(x=215,y=205)
        b_9=Button(root2,bg="orange",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_9.place(x=120,y=300)
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    


def b1():
    
    
    global b_3,root2,val0,val1,choose,x_1,lst,temp,res,name1,name2,canvas,b_4
    if temp==1:
        return
    
    if choose%2==0:
        x_1=Label(root2,text=name1+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_3=Button(root2,bg="white",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_3.place(x=120,y=110)
        lst[1]=val0
    else:
        x_1=Label(root2,text=name2+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_3=Button(root2,bg="white",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_3.place(x=120,y=110)
        lst[1]=val1
    
    #print(lst)
    r1=lst[1]+lst[2]+lst[3]
    r2=lst[4]+lst[5]+lst[6]
    r3=lst[7]+lst[8]+lst[9]
    c1=lst[1]+lst[4]+lst[7]
    c2=lst[2]+lst[5]+lst[8]
    c3=lst[3]+lst[6]+lst[9]
    d1=lst[1]+lst[5]+lst[9]
    d2=lst[3]+lst[5]+lst[7]
    #print(r1)
    #print(r2)
    #print(r3)
    #print(c1)
    #print(c2)
    #print(c3)
    #print(d1)
    #print(d2)
    
    v_1='XXX'
    if r1==v_1 or r2==v_1 or r3==v_1 or c1==v_1 or c2==v_1 or c3==v_1 or d1==v_1 or d2==v_1:
        #print('1st User win the game')
        res=1
        temp=1
    
    v_2='OOO'
    if r1==v_2 or r2==v_2 or r3==v_2 or c1==v_2 or c2==v_2 or c3==v_2 or d1==v_2 or d2==v_2:
       # print("2nd user win the game")
        temp=1
        res=2
        
    if res==1:
        x_1=Label(root2,text=name1+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)

        print("1st USER WIN THE GAME")
        v='XXX'
        
        check_1()
        
        
        '''if r1==v:
            print("ROW 1")
            
            
            

        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    elif res==2:
        x_1=Label(root2,text=name2+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)
        
        check_2()

        
        '''print("2nd user WIN THE GAME")
        v='OOO'
        if r1==v:
            print("ROW 1")
            
            
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    else:
       # print(lst)
        count=0
        for i in range(1,len(lst)):
            if lst[i] in ['X','O']:
                count+=1
        #print(count)
        if count==9:
            x_1=Label(root2,text='NO ONE WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
            x_1.place(x=140,y=430)

            


    

def b2():
    
    
    global b_4,root2,val0,val1,choose,x_1,lst,temp,res,name1,name2
    
    if temp==1:
        return
    
    if choose%2==0:
        x_1=Label(root2,text=name1+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_4=Button(root2,bg="white",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_4.place(x=215,y=110)
        lst[2]=val0
    else:
        x_1=Label(root2,text=name2+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_4=Button(root2,bg="white",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_4.place(x=215,y=110)
        lst[2]=val1
    
    #print(lst)
    r1=lst[1]+lst[2]+lst[3]
    r2=lst[4]+lst[5]+lst[6]
    r3=lst[7]+lst[8]+lst[9]
    c1=lst[1]+lst[4]+lst[7]
    c2=lst[2]+lst[5]+lst[8]
    c3=lst[3]+lst[6]+lst[9]
    d1=lst[1]+lst[5]+lst[9]
    d2=lst[3]+lst[5]+lst[7]
    #print(r1)
    #print(r2)
    #print(r3)
    #print(c1)
    #print(c2)
    #print(c3)
    #print(d1)
    #print(d2)
    
    v_1='XXX'
    if r1==v_1 or r2==v_1 or r3==v_1 or c1==v_1 or c2==v_1 or c3==v_1 or d1==v_1 or d2==v_1:
        #print('1st User win the game')
        temp=1
        res=1
    
    v_2='OOO'
    if r1==v_2 or r2==v_2 or r3==v_2 or c1==v_2 or c2==v_2 or c3==v_2 or d1==v_2 or d2==v_2:
        #print("2nd user win the game")
        temp=1
        res=2
        
    if res==1:
        x_1=Label(root2,text=name1+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)
        check_1()

        '''print("1st USER WIN THE GAME")
        
        v='XXX'
        if r1==v:
            print("ROW 1")
            
            
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    elif res==2:
        x_1=Label(root2,text=name2+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)
        check_2()

        '''print("2nd user WIN THE GAME")
        v='OOO'
        if r1==v:
            print("ROW 1")
            
            
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    else:
        count=0
        for i in range(1,len(lst)):
            if lst[i] in ['X','O']:
                count+=1
        if count==9:
            x_1=Label(root2,text='NO ONE WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
            x_1.place(x=140,y=430)



    

        

def b3():
    
    
    global b_5,root2,val0,val1,choose,temp,res
    if temp==1:
        return
    
    if choose%2==0:
        x_1=Label(root2,text=name1+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_5=Button(root2,bg="white",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_5.place(x=310,y=110)
        lst[3]=val0
    else:
        x_1=Label(root2,text=name2+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_5=Button(root2,bg="white",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_5.place(x=310,y=110)
        lst[3]=val1
    
   # print(lst)
    r1=lst[1]+lst[2]+lst[3]
    r2=lst[4]+lst[5]+lst[6]
    r3=lst[7]+lst[8]+lst[9]
    c1=lst[1]+lst[4]+lst[7]
    c2=lst[2]+lst[5]+lst[8]
    c3=lst[3]+lst[6]+lst[9]
    d1=lst[1]+lst[5]+lst[9]
    d2=lst[3]+lst[5]+lst[7]
    #print(r1)
    #print(r2)
    #print(r3)
    #print(c1)
    #print(c2)
    #print(c3)
    #print(d1)
    #print(d2)
    
    v_1='XXX'
    if r1==v_1 or r2==v_1 or r3==v_1 or c1==v_1 or c2==v_1 or c3==v_1 or d1==v_1 or d2==v_1:
        #print('1st User win the game')
        temp=1
        res=1
    
    v_2='OOO'
    if r1==v_2 or r2==v_2 or r3==v_2 or c1==v_2 or c2==v_2 or c3==v_2 or d1==v_2 or d2==v_2:
        #print("2nd user win the game")
        temp=1
        res=2
    
    if res==1:
        x_1=Label(root2,text=name1+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)
        check_1()

        
        '''print("1st USER WIN THE GAME")
        v='XXX'
        if r1==v:
            print("ROW 1")
           
            
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    elif res==2:
        x_1=Label(root2,text=name2+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)
        check_2()

        '''print("2nd user WIN THE GAME")
        v='OOO'
        if r1==v:
            print("ROW 1")
            
            
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    
    else:
        count=0
        for i in range(1,len(lst)):
            if lst[i] in ['X','O']:
                count+=1
        if count==9:
            x_1=Label(root2,text='NO ONE WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
            x_1.place(x=140,y=430)



    


def b4():
    
    
    global b_6,root2,val0,val1,choose,temp,res
    if temp==1:
        return
    
    if choose%2==0:
        x_1=Label(root2,text=name1+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_6=Button(root2,bg="white",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_6.place(x=120,y=205)
        lst[4]=val0
    else:
        x_1=Label(root2,text=name2+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_6=Button(root2,bg="white",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_6.place(x=120,y=205)
        lst[4]=val1
        
    #print(lst)
    r1=lst[1]+lst[2]+lst[3]
    r2=lst[4]+lst[5]+lst[6]
    r3=lst[7]+lst[8]+lst[9]
    c1=lst[1]+lst[4]+lst[7]
    c2=lst[2]+lst[5]+lst[8]
    c3=lst[3]+lst[6]+lst[9]
    d1=lst[1]+lst[5]+lst[9]
    d2=lst[3]+lst[5]+lst[7]
    #print(r1)
    #print(r2)
    #print(r3)
    #print(c1)
    #print(c2)
    #print(c3)
    #print(d1)
    #print(d2)
    
    v_1='XXX'
    if r1==v_1 or r2==v_1 or r3==v_1 or c1==v_1 or c2==v_1 or c3==v_1 or d1==v_1 or d2==v_1:
        #print('1st User win the game')
        temp=1
        res=1
    
    v_2='OOO'
    if r1==v_2 or r2==v_2 or r3==v_2 or c1==v_2 or c2==v_2 or c3==v_2 or d1==v_2 or d2==v_2:
        #print("2nd user win the game")
        temp=1
        res=2
    
    if res==1:
        x_1=Label(root2,text=name1+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)

        check_1()
        '''print("1st USER WIN THE GAME")
        v='XXX'
        if r1==v:
            print("ROW 1")
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    elif res==2:
        x_1=Label(root2,text=name2+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)
        check_2()

        '''print("2nd user WIN THE GAME")
        v='OOO'
        if r1==v:
            print("ROW 1")
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    else:
        count=0
        for i in range(1,len(lst)):
            if lst[i] in ['X','O']:
                count+=1
        if count==9:
            x_1=Label(root2,text='NO ONE WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
            x_1.place(x=140,y=430)



    

def b5():
    
    
    global b_7,root2,val0,val1,choose,temp,res
    if temp==1:
        return
    
    if choose%2==0:
        x_1=Label(root2,text=name1+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_7=Button(root2,bg="white",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_7.place(x=215,y=205)
        lst[5]=val0
    else:
        x_1=Label(root2,text=name2+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_7=Button(root2,bg="white",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_7.place(x=215,y=205)
        lst[5]=val1
    
    #print(lst)
    r1=lst[1]+lst[2]+lst[3]
    r2=lst[4]+lst[5]+lst[6]
    r3=lst[7]+lst[8]+lst[9]
    c1=lst[1]+lst[4]+lst[7]
    c2=lst[2]+lst[5]+lst[8]
    c3=lst[3]+lst[6]+lst[9]
    d1=lst[1]+lst[5]+lst[9]
    d2=lst[3]+lst[5]+lst[7]
    #print(r1)
    #print(r2)
    #print(r3)
    #print(c1)
    #print(c2)
    #print(c3)
    #print(d1)
    #print(d2)
    
    v_1='XXX'
    if r1==v_1 or r2==v_1 or r3==v_1 or c1==v_1 or c2==v_1 or c3==v_1 or d1==v_1 or d2==v_1:
        #print('1st User win the game')
        temp=1
        res=1
    
    v_2='OOO'
    if r1==v_2 or r2==v_2 or r3==v_2 or c1==v_2 or c2==v_2 or c3==v_2 or d1==v_2 or d2==v_2:
        #print("2nd user win the game")
        temp=1
        res=2
    
    if res==1:
        x_1=Label(root2,text=name1+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)

        check_1() 
        '''print("1st USER WIN THE GAME")
        v='XXX'
        if r1==v:
            print("ROW 1")
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    elif res==2:
        x_1=Label(root2,text=name2+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)
        check_2()

        '''print("2nd user WIN THE GAME")
        v='OOO'
        if r1==v:
            print("ROW 1")
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    else:
       count=0
       for i in range(1,len(lst)):
           if lst[i] in ['X','O']:
               count+=1
       if count==9:
           x_1=Label(root2,text='NO ONE WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
           x_1.place(x=140,y=430)


    
        

def b6():
    
    
    global b_8,root2,val0,val1,choose,temp,res
    if temp==1:
        return
    
    if choose%2==0:
        x_1=Label(root2,text=name1+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_8=Button(root2,bg="white",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_8.place(x=310,y=205)
        lst[6]=val0
    else:
        x_1=Label(root2,text=name2+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_8=Button(root2,bg="white",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_8.place(x=310,y=205)
        lst[6]=val1
    
    #print(lst)
    r1=lst[1]+lst[2]+lst[3]
    r2=lst[4]+lst[5]+lst[6]
    r3=lst[7]+lst[8]+lst[9]
    c1=lst[1]+lst[4]+lst[7]
    c2=lst[2]+lst[5]+lst[8]
    c3=lst[3]+lst[6]+lst[9]
    d1=lst[1]+lst[5]+lst[9]
    d2=lst[3]+lst[5]+lst[7]
    #print(r1)
    #print(r2)
    #print(r3)
    #print(c1)
    #print(c2)
    #print(c3)
    #print(d1)
    #print(d2)
    
    v_1='XXX'
    if r1==v_1 or r2==v_1 or r3==v_1 or c1==v_1 or c2==v_1 or c3==v_1 or d1==v_1 or d2==v_1:
        #print('1st User win the game')
        temp=1
        res=1
    
    v_2='OOO'
    if r1==v_2 or r2==v_2 or r3==v_2 or c1==v_2 or c2==v_2 or c3==v_2 or d1==v_2 or d2==v_2:
        #print("2nd user win the game")
        temp=1
        res=2
    
    if res==1:
        x_1=Label(root2,text=name1+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)

        check_1()
        '''print("1st USER WIN THE GAME")
        v='XXX'
        if r1==v:
            print("ROW 1")
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    elif res==2:
        x_1=Label(root2,text=name2+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)
        check_2()

        '''print("2nd user WIN THE GAME")
        v='OOO'
        if r1==v:
            print("ROW 1")
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    else:
       count=0
       for i in range(1,len(lst)):
           if lst[i] in ['X','O']:
               count+=1
       if count==9:
           x_1=Label(root2,text='NO ONE WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
           x_1.place(x=140,y=430)


    
    

def b7():
    
    
    global b_9,root2,val0,val1,choose,temp,res
    if temp==1:
        return
    
    if choose%2==0:
        x_1=Label(root2,text=name1+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_9=Button(root2,bg="white",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_9.place(x=120,y=300)
        lst[7]=val0
    else:
        x_1=Label(root2,text=name2+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_9=Button(root2,bg="white",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_9.place(x=120,y=300)
        lst[7]=val1
    
    #print(lst)
    r1=lst[1]+lst[2]+lst[3]
    r2=lst[4]+lst[5]+lst[6]
    r3=lst[7]+lst[8]+lst[9]
    c1=lst[1]+lst[4]+lst[7]
    c2=lst[2]+lst[5]+lst[8]
    c3=lst[3]+lst[6]+lst[9]
    d1=lst[1]+lst[5]+lst[9]
    d2=lst[3]+lst[5]+lst[7]
    #print(r1)
    #print(r2)
    #print(r3)
    #print(c1)
    #print(c2)
    #print(c3)
    #print(d1)
    #print(d2)
    
    v_1='XXX'
    if r1==v_1 or r2==v_1 or r3==v_1 or c1==v_1 or c2==v_1 or c3==v_1 or d1==v_1 or d2==v_1:
        #print('1st User win the game')
        temp=1
        res=1
    
    v_2='OOO'
    if r1==v_2 or r2==v_2 or r3==v_2 or c1==v_2 or c2==v_2 or c3==v_2 or d1==v_2 or d2==v_2:
       # print("2nd user win the game")
        temp=1
        res=2
    
    if res==1:
        x_1=Label(root2,text=name1+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)

        check_1()
        '''print("1st USER WIN THE GAME")
        v='XXX'
        if r1==v:
            print("ROW 1")
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    elif res==2:
        x_1=Label(root2,text=name2+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)
        check_2()

        '''print("2nd user WIN THE GAME")
        v='OOO'
        if r1==v:
            print("ROW 1")
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    else:
       count=0
       for i in range(1,len(lst)):
           if lst[i] in ['X','O']:
               count+=1
       if count==9:
           x_1=Label(root2,text='NO ONE WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
           x_1.place(x=140,y=430)


    
            
    

def b8():
    
    
    global b_10,root2,val0,val1,choose,temp,res
    if temp==1:
        return
    
    if choose%2==0:
        x_1=Label(root2,text=name1+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_10=Button(root2,bg="white",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_10.place(x=215,y=300)
        lst[8]=val0
    else:
        x_1=Label(root2,text=name2+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_10=Button(root2,bg="white",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_10.place(x=215,y=300)
        lst[8]=val1
        
    #print(lst)
    r1=lst[1]+lst[2]+lst[3]
    r2=lst[4]+lst[5]+lst[6]
    r3=lst[7]+lst[8]+lst[9]
    c1=lst[1]+lst[4]+lst[7]
    c2=lst[2]+lst[5]+lst[8]
    c3=lst[3]+lst[6]+lst[9]
    d1=lst[1]+lst[5]+lst[9]
    d2=lst[3]+lst[5]+lst[7]
    #print(r1)
    #print(r2)
    #print(r3)
    #print(c1)
    #print(c2)
    #print(c3)
    #print(d1)
    #print(d2)
    
    v_1='XXX'
    if r1==v_1 or r2==v_1 or r3==v_1 or c1==v_1 or c2==v_1 or c3==v_1 or d1==v_1 or d2==v_1:
        #print('1st User win the game')
        temp=1
        res=1
    
    v_2='OOO'
    if r1==v_2 or r2==v_2 or r3==v_2 or c1==v_2 or c2==v_2 or c3==v_2 or d1==v_2 or d2==v_2:
        #print("2nd user win the game")
        temp=1
        res=2
    
    
    if res==1:
        x_1=Label(root2,text=name1+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)

        check_1()
        '''print("1st USER WIN THE GAME")
        v='XXX'
        if r1==v:
            print("ROW 1")
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    elif res==2:
        x_1=Label(root2,text=name2+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)
        check_2()

        '''print("2nd user WIN THE GAME")
        v='OOO'
        if r1==v:
            print("ROW 1")
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    else:
       count=0
       for i in range(1,len(lst)):
           if lst[i] in ['X','O']:
               count+=1
       if count==9:
           x_1=Label(root2,text='NO ONE WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
           x_1.place(x=140,y=430)


    
        
    
def b9():
    
    
    global b_11,root2,val0,val1,choose,temp,res
    if temp==1:
        return
    
    if choose%2==0:
        x_1=Label(root2,text=name1+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_11=Button(root2,bg="white",text=val0,font='comicsansms 19 bold',padx=15,pady=10)
        b_11.place(x=310,y=300)
        lst[9]=val0
    else:
        x_1=Label(root2,text=name2+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
        x_1.place(x=150,y=430)

        b_11=Button(root2,bg="white",text=val1,font='comicsansms 19 bold',padx=15,pady=10)
        b_11.place(x=310,y=300)
        lst[9]=val1
    
    #print(lst)
    r1=lst[1]+lst[2]+lst[3]
    r2=lst[4]+lst[5]+lst[6]
    r3=lst[7]+lst[8]+lst[9]
    c1=lst[1]+lst[4]+lst[7]
    c2=lst[2]+lst[5]+lst[8]
    c3=lst[3]+lst[6]+lst[9]
    d1=lst[1]+lst[5]+lst[9]
    d2=lst[3]+lst[5]+lst[7]
    '''print(r1)
    print(r2)
    print(r3)
    print(c1)
    print(c2)
    print(c3)
    print(d1)
    print(d2)'''
    
    v_1='XXX'
    if r1==v_1 or r2==v_1 or r3==v_1 or c1==v_1 or c2==v_1 or c3==v_1 or d1==v_1 or d2==v_1:
        #print('1st User win the game')
        temp=1
        res=1
    
    v_2='OOO'
    if r1==v_2 or r2==v_2 or r3==v_2 or c1==v_2 or c2==v_2 or c3==v_2 or d1==v_2 or d2==v_2:
        #print("2nd user win the game")
        temp=1
        res=2
    
    
    if res==1:
        x_1=Label(root2,text=name1+'  WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)

        check_1()
        '''print("1st USER WIN THE GAME")
        v='XXX'
        if r1==v:
            print("ROW 1")
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    elif res==2:
        x_1=Label(root2,text=name2+' WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
        x_1.place(x=140,y=430)
        check_2()

        '''   print("2nd user WIN THE GAME")
        v='OOO'
        if r1==v:
            print("ROW 1")
        elif r2==v:
            print("ROW 2")
        elif r3==v:
            print("ROW 3")
        elif c1==v:
            print("COL 1")
        elif c2==v:
            print("COL 2")
        elif c3==v:
            print("COL 3")
        elif d1==v:
            print("DGN 1")
        else:
            print("DGN 2")'''
    else:
       count=0
       for i in range(1,len(lst)):
           if lst[i] in ['X','O']:
               count+=1
       if count==9:
           x_1=Label(root2,text='NO ONE WIN THE GAME',fg='white',bg='yellowgreen',font='papyrue 10 bold',relief='sunken',bd=1,padx=40,pady=23)
           x_1.place(x=140,y=430)


    
        


    
    
def user():
    global b_3,root2,root4,name1,canvas
    root4.destroy()
    root2=Tk()
    root2.title("TIC TOE GAME")
    root2.geometry('500x500')
    root2.config(bg='orange red')
    
    x=Label(root2,text='LETS PLAY THE GAME',fg='white',bg='black',font='papyrue 15 bold',relief='sunken',bd=10,padx=40)
    x.place(x=90,y=30)

    b_3=Button(root2,fg='black',text='',bd=7,pady=30,padx=40,bg='yellowgreen',font='comicsansms 9 bold',command=check1)
    b_3.place(x=105,y=100)
    b_4=Button(root2,fg='black',text='',bd=7,pady=30,padx=40,bg='yellowgreen',font='comicsansms 9 bold',command=check2)
    b_4.place(x=200,y=100)
    b_5=Button(root2,fg='black',text='',bd=7,pady=30,padx=40,bg='yellowgreen',font='comicsansms 9 bold',command=check3)
    b_5.place(x=295,y=100)
    b_6=Button(root2,fg='black',text='',bd=7,pady=30,padx=40,bg='yellowgreen',font='comicsansms 9 bold',command=check4)
    b_6.place(x=105,y=195)
    
    b_7=Button(root2,fg='black',text='',bd=7,pady=30,padx=40,bg='yellowgreen',font='comicsansms 9 bold',command=check5)
    b_7.place(x=200,y=195)
    
    b_8=Button(root2,fg='black',text='',bd=7,pady=30,padx=40,bg='yellowgreen',font='comicsansms 9 bold',command=check6)
    b_8.place(x=295,y=195)
    
    b_9=Button(root2,fg='black',text='',bd=7,pady=30,padx=40,bg='yellowgreen',font='comicsansms 9 bold',command=check7)
    b_9.place(x=105,y=290)
    
    b_10=Button(root2,fg='black',text='',bd=7,pady=30,padx=40,bg='yellowgreen',font='comicsansms 9 bold',command=check8)
    b_10.place(x=200,y=290)
    
    b_11=Button(root2,fg='black',text='',bd=7,pady=30,padx=40,bg='yellowgreen',font='comicsansms 9 bold',command=check9)
    b_11.place(x=295,y=290)
    
    x_1=Label(root2,text=name1+' TURN',fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=10,padx=40)
    x_1.place(x=150,y=430)

    
    
def submit():
    
    global name1,name2,root4
    name1=identry.get()
    name2=identry1.get()
    
    print(name1,name2)
    if len(name1)>=4 and len(name2)>=4:
        user()
    
    else:
        tmsg.showerror("ERROR","ENTER A VALID NAME")
        



def detail():
    
    global root,identry,identry1,root4
    root.destroy()
    root4=Tk()
    root4.title('LOGIN DETAILS')
    root4.geometry('400x200')
    root4.config(bg='pale violet red')
    x=Label(root4,text='ENTER YOUR DETAILS',fg='black',bg='yellowgreen',font='papyrue 15 bold',relief='sunken',bd=1,padx=40)
    x.place(x=55,y=30)
    x1=Label(root4,text='Name-1',fg='white',bg="black",font='papyrue 10 bold',relief='sunken',bd=1,padx=4)
    x1.place(x=80,y=90)
    x2=Label(root4,text='Name-2',fg='white',bg="black",font='papyrue 10 bold',relief='sunken',bd=1,padx=4)
    x2.place(x=80,y=120)
    
    
    identry=Entry(root4)
    identry.place(x=160,y=90)
    identry1=Entry(root4)
    identry1.place(x=160,y=120)
    b_1=Button(root4,fg='black',text='Submit',bd=2,pady=5,padx=20,bg='yellow',font='comicsansms 7 bold',command=submit)
    b_1.place(x=145,y=155)
    
    
    

    
    

    


    
    
    
    
    
root=Tk()
root.title('ANSH GUI')
root.geometry('500x500')
root.config(bg='cyan')
x=Label(root,text='TIC TOE GAME',fg='white',bg='black',font='papyrue 15 bold',relief='sunken',bd=10,padx=40)
x.place(x=125,y=50)
b_1=Button(root,fg='black',text='USER',bd=5,pady=10,padx=50,bg='yellowgreen',font='comicsansms 9 bold',command=detail)
b_1.place(x=180,y=200)
# b_2=Button(root,fg='black',text='COMPUTER',bd=5,pady=10,padx=50,bg='yellowgreen',font='comicsansms 9 bold')
# b_2.place(x=165,y=280)


#b_1=Button(root,fg='black',text='Submit',bd=2,pady=5,padx=20,bg='white',font='comicsansms 7 bold')
#b_1.place(x=200,y=250)
#b_2=Button(root,fg='black',text='Quit',bd=2,pady=5,padx=20,bg='white',font='comicsansms 7 bold')
#b_2.place(x=390,y=250)


root.mainloop()
#print(lst)
