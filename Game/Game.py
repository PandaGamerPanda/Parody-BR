from tkinter import *
import random


global reapeter
global lfdlr
global lfplr1
global plr1trn
global dlrtrn
reapeter = 2
mag=[]
plr1trn = True  #player 1 turn
dlrtrn = False  #dealer turn
cntrnd = 0  #count round
lfplr1 = 3  #life player 1
lfdlr = 3  #life dealer
allbul = [0, 1]
allpack = [[1, 0], [1, 1, 0], [1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 0, 0],
           [1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0]]
ntbrk = True  #not break


def death():
    global plr1trn
    a = random.randint(1,100)
    if (a == 52 and plr1trn == False)  or (a == 69 and plr1trn == False)  or (a == 14 and plr1trn == False)  or (a == 88 and plr1trn == False)  or (a == 78 and plr1trn == False):
        bg_photo.config(image=image_pashalko)
        window.update()
        window.after(3000)
        window.update()
        ntbrk = False
        window.after(1000)
        window.destroy()
    elif plr1trn == False:
        bg_photo.config(image=image_dead_u)
        window.update()
        window.after(3000)
        window.update()
        ntbrk = False
        window.after(1000)
        window.destroy()
    else:
        bg_photo.config(image=image_dead_dlr)
        window.update()
        window.after(3000)
        window.update()
        ntbrk = False
        window.after(1000)
        window.destroy()

def kill_dlr():
    global reapeter
    global lfdlr
    global lfplr1
    global plr1trn
    global dlrtrn
    if mag[0] == 0:
        bg_photo.config(image=image_u_vs_dlr)
        choose_button1.place_forget()
        choose_button2.place_forget()
        window.update()
        bg_photo.after(2000)
        text_bg.config(text='щелчок, вы пропускаете ход')
        window.update()
        window.after(2000)
        plr1trn = False
        dlrtrn = True
        mag.pop(0)
        reapeter = 2
        
    elif mag[0] == 1:
        bg_photo.config(image=image_u_vs_dlr)
        choose_button1.place_forget()
        choose_button2.place_forget()
        bg_photo.after(2000)  
        window.update()
        text_bg.config(text='ВЫСТРЕЛ, вы пропукаете ход')
        window.update()
        bg_photo.config(image=image_u_kill_dlr)
        window.update()
        bg_photo.after(200)
        bg_photo.config(image=image_u_vs_dlr)
        window.update()
        window.after(2000)
        plr1trn = False
        dlrtrn = True
        lfdlr = lfdlr - 1
        mag.pop(0)
        reapeter = 2
        
    
def kill_u():
    global reapeter
    global lfdlr
    global lfplr1
    global plr1trn
    global dlrtrn
    if mag[0] == 0:
        bg_photo.config(image=image_u_vs_u)
        choose_button1.place_forget()
        choose_button2.place_forget()
        window.update()
        bg_photo.after(2000)
        text_bg.config(text='щелчок, дилер пропускает ход')
        window.update()
        window.after(2000)
        plr1trn = True
        dlrtrn = False
        mag.pop(0)
        reapeter = 2

    elif mag[0] == 1:
        bg_photo.config(image=image_u_vs_u)
        choose_button1.place_forget()
        choose_button2.place_forget()
        window.update()
        bg_photo.after(2000)
        text_bg.config(text='ВЫСТРЕЛ')
        window.update()
        bg_photo.config(image=image_u_kill_u)
        window.update()
        bg_photo.after(200)
        bg_photo.config(image=image_u_vs_u)
        window.update()
        window.after(2000)
        plr1trn = False
        dlrtrn = True
        lfplr1 = lfplr1 - 1
        mag.pop(0)
        reapeter = 2
        

    
#создаем окно
window = Tk()
window.geometry('250x384')
window.title("Вы что, играете?")

#затем добавляем все кадры
image_afk = PhotoImage(file="Images/dealer_afk.gif")
image_dlr_vs_u = PhotoImage(file="Images/dealer_vs_you.gif")
image_dlr_vs_dlr = PhotoImage(file="Images/dealer_vs_dealer.gif")
image_u_vs_dlr = PhotoImage(file="Images/you_vs_dealer.gif")
image_u_vs_u = PhotoImage(file="Images/you_vs_you.gif")
image_dlr_kill_u = PhotoImage(file="Images/dealer_vs_you_death.gif")
image_dlr_kill_dlr = PhotoImage(file="Images/dealer_vs_dealer_death.gif")
image_u_kill_dlr = PhotoImage(file="Images/you_vs_dealer_death.gif")
image_u_kill_u = PhotoImage(file="Images/you_vs_you_death.gif")
image_pashalko = PhotoImage(file="Images/you_vs_dealer_pashalko_death.gif")
image_dead_dlr = PhotoImage(file="Images/max_death_from_dealer.gif")
image_dead_u = PhotoImage(file="Images/max_death_from_you.gif")

#создаем фон
bg_photo = Label(window, image=image_afk)
bg_photo.place(x=0, y=0)

#создаем текст
text_bg = Label(window, text="Здесь будет текст", bg='gray')
text_bg.place(x=10, y=265)


while (ntbrk is True):
    window.update()
    if lfplr1 > 0 and lfdlr > 0 and len(mag) == 0:
        cntrnd = cntrnd + 1
        text_bg.config(text='раунд ' + str(cntrnd))
        window.update()
        bg_photo.after(2000)
    if len(mag) == 0:
        mag = random.choice(allpack)
        for i in range(2):
            random.shuffle(mag)
        if (mag.count(0) == 1) and (mag.count(1) == 1):
            text_bg.config(text=str(mag.count(0)) + ' холостой, ' + str(mag.count(1)) + ' боевой')
        elif mag.count(0) > 1 and mag.count(1) == 1:
            text_bg.config(text=str(mag.count(0)) + ' холостых, ' + str(mag.count(1)) + '  боевой')
        elif (mag.count(0) == 1) and (mag.count(1) > 1):
            text_bg.config(text=str(mag.count(0)) + ' холостой, ' + str(mag.count(1)) + ' боевых')
        else:
            text_bg.config(text=str(mag.count(0)) + ' холостых, ' + str(mag.count(1)) + ' боевых')
    #print(mag)
    
#player1
    while (len(mag) > 0) and (ntbrk == True) and (plr1trn == True):
        a = 'вы - '+ str(lfplr1)+ ' дилер - '+str(lfdlr)
        #print(a)
        bg_photo.config(image=image_afk)
        if reapeter == 2:
            reapeter -= 1
            window.update()
            window.after(2000)
            text_bg.configure(text=(a))
            window.update()
            #создаем кнопки выбора
            choose_button1 = Button(text='Выстрелить в дилера', command=kill_dlr, activebackground='red', bg='gray')
            choose_button1.place(x=10, y=295)

            choose_button2 = Button(text='Выстрелить в себя', command=kill_u, activebackground='red', bg='gray')
            choose_button2.place(x=10, y=325)
        
        elif reapeter == 1:
            reapeter -= 1
            window.after(3000)
            window.update()
            
        if (lfplr1 <= 0) or (lfdlr <= 0):
            ntbrk = False
            mag.pop(0)
        choose_button1.update()
        choose_button2.update()              
#dealer
    while (dlrtrn == True) and (len(mag) > 0) and (ntbrk == True):
        bg_photo.config(image=image_afk)
        window.update()
        if (lfplr1 <= 0) or (lfdlr <= 0):
            ntbrk = False
            mag.pop(0)
        elif (mag.count(0) > mag.count(1)) and (mag[0] == 0):
            bg_photo.config(image=image_dlr_vs_dlr)
            window.update()
            bg_photo.after(2000)
            text_bg.config(text='дилер стреляет в себя')
            text_bg.after(1000)
            text_bg.config(text='щелчок, вы пропускаете ход')
            plr1trn = False
            dlrtrn = True
            mag.pop(0)
            bg_photo.after(2000)
        elif (mag.count(0) > mag.count(1)) and (mag[0] == 1):
            text_bg.config(text='дилер стреляет в себя')
            bg_photo.config(image=image_dlr_vs_dlr)
            window.update()
            bg_photo.after(2000)
            text_bg.config(text='ВЫСТРЕЛ')
            bg_photo.config(image=image_dlr_kill_dlr)
            window.update()
            bg_photo.after(200)
            bg_photo.config(image=image_dlr_vs_dlr)
            window.update()
            dlrtrn = False
            plr1trn = True
            lfdlr = lfdlr - 1
            mag.pop(0)
        elif (mag.count(0) < mag.count(1)) and (mag[0] == 0):
            
            text_bg.config(text='дилер стреляет в вас')
            bg_photo.config(image=image_dlr_vs_u)
            window.update()
            bg_photo.after(2000)
            text_bg.config(text='щелчок, дилер пропускает ход')
            plr1trn = True
            dlrtrn = False
            mag.pop(0)
        elif (mag.count(0) < mag.count(1)) and (mag[0] == 1):
            text_bg.config(text='дилер стреляет в вас')
            bg_photo.config(image=image_dlr_vs_u)
            window.update()
            bg_photo.after(2000)
            text_bg.after(1000)
            text_bg.config(text='ВЫСТРЕЛ')
            bg_photo.config(image=image_dlr_kill_u)
            window.update()
            bg_photo.after(200)
            bg_photo.config(image=image_dlr_vs_u)
            window.update()
            dlrtrn = False
            plr1trn = True
            lfplr1 = lfplr1 - 1
            mag.pop(0)
        elif mag.count(0) == mag.count(1):
            if (random.choice(allbul) == 0) and (mag[0] == 0):
                text_bg.config(text='дилер стреляет в себя')
                bg_photo.config(image=image_dlr_vs_dlr)
                window.update()
                bg_photo.after(2000)
                text_bg.after(1000)
                text_bg.config(text='щелчок, вы пропускаете ход')
                text_bg.after(1000)
                bg_photo.after(1000)
                dlrtrn = True
                plr1trn = False
                mag.pop(0)
            elif (random.choice(allbul) == 0) and (mag[0] == 1):
                text_bg.config(text='дилер стреляет в себя')
                bg_photo.config(image=image_dlr_vs_dlr)
                window.update() 
                bg_photo.after(2000)
                text_bg.after(1000)
                text_bg.config(text='ВЫСТРЕЛ')
                text_bg.after(1000)
                bg_photo.config(image=image_dlr_kill_dlr)
                window.update()
                bg_photo.after(200)
                bg_photo.config(image=image_dlr_vs_dlr)
                window.update()
                dlrtrn = False
                plr1trn = True
                lfdlr = lfdlr - 1
                mag.pop(0)
            elif (random.choice(allbul) == 1) and (mag[0] == 0):
                text_bg.config(text='дилер стреляет в вас')
                bg_photo.config(image=image_dlr_vs_u)
                window.update()
                bg_photo.after(2000)
                text_bg.after(1000)
                text_bg.config(text='щелчок, дилер пропускает ход')
                text_bg.after(1000)
                dlrtrn = False
                plr1trn = True
                mag.pop(0)
            elif (random.choice(allbul) == 1) and (mag[0] == 1):
                text_bg.config(text='дилер стреляет в вас')
                bg_photo.config(image=image_dlr_vs_u)
                window.update()
                window.after(2000)
                text_bg.after(1000)
                text_bg.config(text='ВЫСТРЕЛ')
                bg_photo.config(image=image_dlr_kill_u)
                window.update()
                window.after(200)
                bg_photo.config(image=image_dlr_vs_u)
                window.update()
                dlrtrn = False
                plr1trn = True
                lfplr1 = lfplr1 - 1
                mag.pop(0)

        if lfplr1 <= 0:
            text_bg.config(text='вы мертвы, дилер победил!')
            death()
        elif lfdlr <= 0:
            ntbrk = False
            text_bg.config(text='дилер мёртв, вы победили!')
            window.after(2000)
            window.destroy()


"text_bg.config(text='Выбери 1 кнопку')"
