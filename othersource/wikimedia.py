from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# 함수 정의 부분

#Q1
ei=0
eif=0
def  e1() :
    global ei
    if var1.get() == 1:
        ei=0
    elif var1.get() == 2:
        ei=1
    elif var1.get() == 3:
        ei=2
    elif var1.get() == 4:
        ei=3
def  e2() :
    global eif
    if var2.get() == 1 :
        eif=0
    elif var2.get() == 2 :
        eif=1
    elif var2.get() == 3:
        eif==2
    elif var2.get() == 4:
        eif=3

jp=0
def  e3() :
    global jp
    if var3.get() == 1 :
        jp=0
    elif var3.get() == 2 :
        jp=1
    elif var3.get() == 3:
        jp=2
    elif var3.get() == 4:
        jp=3

tf=0
tff=0
def  e4() :
    global tf
    if var4.get() == 1 :
        tf=0
    elif var4.get() == 2 :
        tf=1
    elif var4.get() == 3:
        tf=2
    elif var4.get() == 4:
        tf=3

def select(event):
    global tff
    value="값 : " + str(scale1.get())
    label_5.config(text=value)
    if scale1.get()==0:
        tff=0
    if scale1.get()==1:
        tff=1
    if scale1.get()==2:
        tff=2
    if scale1.get()==3:
        tff=3

sn=0
def select1(event):
    global sn
    var6="값 : " + str(scale2.get())
    label_6.config(text=var6)
    if scale2.get()==0:
        sn=0
    if scale2.get()==1:
        sn=1
    if scale2.get()==2:
        sn=2
    if scale2.get()==3:
        sn=3

    
def  show() :
    global ei,eif,jp,tf,tff,sn
    mtext=""
    #1,2
    if ei+eif<=2 :
        mtext=mtext+'E'
    else:
        mtext=mtext+'I'
    #6
    if sn<=1 :
        mtext=mtext+'N'
    else: 
        mtext=mtext+'S'
    #4,5   
    if tf+tff<=2:
        mtext=mtext+'T'
    else:
        mtext=mtext+'F'
    #3
    if jp<=1 :
        mtext=mtext+'P'
    else: 
        mtext=mtext+'J'

   
    if mtext=='ISTJ':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 ISTJ입니다!\n당신은 끈기있고 계획적이며,협동적이기 보단 독립적인 일을 선호하는 경향이 있습니다.\n당신은 혼자 자료를 정확히 정리하는 일이 다른 이들과의 소통보다중요하므로,당신에게 추천하는 미디어는 '문자매체'입니다. \n ex. 메모, 편지,메일")
    elif mtext=='ISFJ':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 ISFJ입니다!\n당신은 온화하고 성실한 성격의 소유자로,타인과의 협업에 협조적인 성향을 가지고 있습니다. \n하지만, 당신은 인간관계에서 오는 스트레스를 힘겨워하므로 당신에겐 적당한 소통을 유지할 수 있는'음성매체'를 추천합니다.\n ex. 전화, 음성녹음")
    elif mtext=='INFJ':
        messagebox.showinfo("Result","당신의 MBTI 유형은 INFJ입니다!\n당신은 사람에 관심이 많고 추상적인 걸 선호하며, 타인에게 의존하는 경향이 있습니다. 따라서 당신에겐 타인과 소통을 하게 해주는 '뉴미디어'를 추천합니다.\n ex. 카카오톡, 스냅챗, 페메")
    elif mtext=='INTJ':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 INTJ입니다!\n당신은 팀내에서 중심축을 가지고 비전을 제시하는 중요한 역할을 하면서도, 독립적인 성향이 강합니다.또한 효율성을 중요시하는 당신에겐, '뉴미디어'를 추천합니다. \n ex. 카카오톡, 스냅챗, 페메")
    elif mtext=='ISTP':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 ISTP입니다!\n당신은 상황에 대한 적응력과 논리력이 뛰어나며 효율성을 중요시합니다.허나 계획적이진 않은 당신. 그런 당신에겐 '문자매체'를 추천합니다. \n ex. 메모, 편지,메일")
    elif mtext=='ISFP':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 ISFP입니다!\n당신은 따뜻한 감정과 겸손한 성격의 소유자!하지만, 결단력과 추진력이 부족하기에, 다른 사람들과의 협업으로 이를 충전하기 위해, 당신에겐 '영상(화상)매체'를 추천합니다.  \n ex. 전자화상회의, 영상통화")
    elif mtext=='INFP':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 INFP입니다!\n당신은 배려심이 많고 사교적이나, 당신의 신념이 굉장히 중요하여 이에 대한 침범받는 것을 극도로 싫어합니다. 따라서 당신에겐 적절한 타인과의 소통이 필요하므로 '뉴미디어'를 추천합니다.  \n ex. 카카오톡, 스냅챗, 온라인 그룹웨어")
    elif mtext=='INTP':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 INTP입니다!\n당신은 다른 사람들을 판단하고 비평하는 것을 좋아하고 자신의 감정을 표현하는 데 매우 신중합니다.그렇기에 당신에겐 당신의 감정을 한 번 더 필터링할 수 있는 '뉴미디어(메신저)'를 추천합니다. \n ex. 카카오톡, 스냅챗, 페메")
    elif mtext=='ESTP':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 ESTP입니다!\n당신은 활동적인 것을 선호하며 일을 미루는 경향이 있으며, 갈등이 발생할 땐 누구보다 이성적으로 해결합니다.협업 상황에서 적절한 해결책을 제시할 능력이 있는 당신에겐 , 타인과의 협업으로 자신의 게으름을 보완할 수 있는 '면대 면 매체'를 추천합니다. \n ex. 상담, 인터뷰, 미팅")
    elif mtext=='ESFP':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 ESFP입니다!\n당신은 사교적이며 분위기메이커입니다. 동시에, 혼자 있을 때만 엄청난 집중력을 발휘하므로 당신에겐 적당한 소통이 필요합니다.당신에겐 '음성매체'를 추천합니다. \n ex. 전화, 음성녹음")
    elif mtext=='ENFP':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 ENFP입니다!\n당신은 새로운 것을 좋아하고 즉흥적이며 금세 싫증을 느낍니다.그런 당신에게 '면대면 대화'는 당신이 상대에게 더욱 집중하게 하고, 타인과의 협업으로 끈기를 기를 기회를 제공할 수 있습니다. \n ex. 인터뷰, 상담")
    elif mtext=='ENTP':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 ENTP입니다!\n당신은 상상력이 풍부하고 도전적이며, 환경에 잘 적응하고 잘 맞춰갑니다. 재치 있고 적극적인 당신은 '음성매체'를 통해서도 타인과 충분히 풍부하게 소통할 수 있습니다. \n ex. 전화, 음성녹음")
    elif mtext=='ESTJ':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 ESTJ입니다!\n당신은 끈기있고 계획적이며, 현실적이고 완벽주의자 성향이 있고, 공감능력이 적어 사람들과 어울리기 힘들어합니다.  따라서 당신에겐 당신의 작업을 혼자 정리한 시간이 필요하므로 '문자매체'를 추천합니다.  \n ex. 편지, 메모, 메일")
    elif mtext=='ESFJ':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 ESFJ입니다!\n당신은 친절하면서도 현실적이고, 호응을 잘하는 성격이지만 실행력 및 추진력이 부족합니다. 그런 당신에겐 타인의 존재를 의식하면서 자신의 부족한 부분을 발전시킬 수 있도록 하는 '영상(화상)매체'를 추천합니다.  \n ex. 전자화상회의, 영상통화 ")
    elif mtext=='ENFJ':
        messagebox.showinfo("Result", "당신의 MBTI 유형은 ENFJ입니다!\n당신은 협동적이며 타인의 약점과 강점을 잘 파악하기에, 타인의 성장을 도모하는 역할을 합니다. 또한 의사소통에도 능하기 때문에, 당신에게 추천하는 매체는 '면대면 매체'입니다.  \n ex. 상담, 인터뷰, 미팅")
    else:
        messagebox.showinfo("Result", "당신의 MBTI 유형은 ENTJ입니다!\n당신은 리더로서 사람들을 이끌며, 자신만의 비전이 확고하고 끈기와 책임감이 강합니다. 그런 당신은 '영상(화상)매체'로도 자신의 일을 완벽히 수행하고 동료를 잘 이끌 수 있습니다.   \n ex. 전자화상회의, 영상통화 ")


        
        

# 메인 코드 부분
window = Tk()
window.title('Wiki-Media')
window.geometry("1280x720")
window.resizable(False,False)

wall=PhotoImage(file="insta.png")
wall_label = Label(image = wall)

gif=PhotoImage(file="insta.png")
wall_label = Label(image = wall)

label_title = Label(window, text="Media MBTI")
label1 = Label(window, text="1st. 나이대를 선택해주세요!")

label2 = Label(window, text="2nd. 당신은 어떤 성격의 소유자 인가요?")
 
label3 = Label(window, text="3rd. 미디어를 사용하는 업무는 주로 어떤 종류인가요?")

label4 = Label(window, text="4th. 평소 미디어를 사용할 때, 당신은 어떤 방식으로 감정을 표현하나요?")

label5 = Label(window, text="5th. 공동작업에서, 당신은 미디어를 통해 얼만큼 타인의 존재감을 느끼고 싶나요? ")

label6 = Label(window, text="6th. 미디어 사용에 있어, 편리성은 얼마나 중요한가요?")


var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

#Q1
b1 = Radiobutton(window, text="10대", variable=var1, value = 1,command=e1)
b2 = Radiobutton(window, text="20대", variable=var1, value = 2,command=e1)
b3 = Radiobutton(window, text="30대", variable=var1, value = 3,command=e1)
b4 = Radiobutton(window, text="40대", variable=var1, value = 4,command=e1)

#Q2
b2_1 = Radiobutton(window, text="완전 외향", variable=var2, value = 1,command=e2)
b2_2 = Radiobutton(window, text="케바케 외향", variable=var2, value = 2,command=e2)
b2_3 = Radiobutton(window, text="케바케 내향", variable=var2, value = 3,command=e2)
b2_4 = Radiobutton(window, text="완전 내향", variable=var2, value = 4,command=e2)

#Q3
b3_1 = Radiobutton(window, text="아이디어 OR 계획 세우기", variable=var3, value = 1,command=e3)
b3_2 = Radiobutton(window, text="협동 및 타협", variable=var3, value = 2,command=e3)
b3_3 = Radiobutton(window, text="지식 사용", variable=var3, value = 3,command=e3)
b3_4 = Radiobutton(window, text="결정 및 판단", variable=var3, value = 4,command=e3)

#Q4
b4_1 = Radiobutton(window, text="문자(글자)", variable=var4, value = 1,command=e4)
b4_2 = Radiobutton(window, text="기호", variable=var4, value = 2,command=e4)
b4_3 = Radiobutton(window, text="이모티콘", variable=var4, value = 3,command=e4)
b4_4 = Radiobutton(window, text="음성메시지", variable=var4, value = 4,command=e4)

#Q5
var5=IntVar()
scale1=Scale(window, variable=var5, orient='horizontal', showvalue=True,
                             tickinterval=1, to=3, length=200, command=select)
label_5=Label(window, text='0')


#Q6
var6=IntVar()
scale2=Scale(window, variable=var6, orient='horizontal', showvalue=True,
                             tickinterval=1, to=3, length=200, command=select1)
label_6=Label(window, text='0')

#submit
button=Button(window, width=15, height=2, text='submit', command=show)


#label.pack()

wall_label.place(x=0,y=0);
label_title.place(x=621,y=63);
label_title.config(font = ('현대하모니 L', 17, 'bold'),fg='purple',bg='white');
label1.place(x=300, y=130);
label1.config(font = ('현대하모니 L', 15, 'bold'),fg='white',bg='purple');

label2.place(x=300, y=210);
label2.config(font = ('현대하모니 L', 15, 'bold'),fg='white',bg='purple');

label3.place(x=300, y=290);
label3.config(font = ('현대하모니 L', 15, 'bold'),fg='white',bg='purple');

label4.place(x=300, y=370);
label4.config(font = ('현대하모니 L', 15, 'bold'),fg='white',bg='purple');

label5.place(x=300, y=450);
label5.config(font = ('현대하모니 L', 15, 'bold'),fg='white',bg='purple');

label6.place(x=300, y=560);
label6.config(font = ('현대하모니 L', 15, 'bold'),fg='white',bg='purple');

#Question 1 : button1.pack()

b1.pack(side=LEFT,padx=10);
b1.place(x=300, y=170);
b2.pack(side=LEFT,padx=10);
b2.place(x=364, y=170);
b3.pack(side=LEFT,padx=10);
b3.place(x=428, y=170);
b4.pack(side=LEFT,padx=10);
b4.place(x=492, y=170);

#Question 2 : button1.pack()

b2_1.pack(side=LEFT,padx=10);
b2_1.place(x=300, y=250);
b2_2.pack(side=LEFT,padx=10);
b2_2.place(x=390, y=250);
b2_3.pack(side=LEFT,padx=10);
b2_3.place(x=490, y=250);
b2_4.pack(side=LEFT,padx=10);
b2_4.place(x=590, y=250);

#Question 3 : button1.pack()

b3_1.pack(side=LEFT,padx=10);
b3_1.place(x=300, y=330);
b3_2.pack(side=LEFT,padx=10);
b3_2.place(x=470, y=330);
b3_3.pack(side=LEFT,padx=10);
b3_3.place(x=570, y=330);
b3_4.pack(side=LEFT,padx=10);
b3_4.place(x=660, y=330);

#Question 4 : button1.pack()

b4_1.pack(side=LEFT,padx=10);
b4_1.place(x=300, y=410);
b4_2.pack(side=LEFT,padx=10);
b4_2.place(x=390, y=410);
b4_3.pack(side=LEFT,padx=10);
b4_3.place(x=450, y=410);
b4_4.pack(side=LEFT,padx=10);
b4_4.place(x=530, y=410);

#Question 5 : button1.pack()
scale1.pack();
scale1.place(x=300, y=490);
label_5.pack();
label_5.place(x=550, y=510);


#Question 6 : button1.pack()
scale2.pack();
scale2.place(x=300, y=600);
label_6.pack();
label_6.place(x=550, y=620);



#submit
button.pack();
button.place(x=900, y=610);



window.mainloop()
