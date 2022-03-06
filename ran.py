import random
def generate_number():
    list3 = ["0","1","2","3","4","5","6","7","8","9"]
    number = ""
    for i in range(10):
        number = number + random.choice(list3)
    l2.config(text = number)
import tkinter as tk
window = tk.Tk()
window.geometry("600x200")
window.config(bg="#F39C12")
window.resizable(width=False,height=False)
window.title('Random Mobile Number Generator') 
b1 = tk.Button(text="Click on me to generate a mobile number",font=("Arial",15),bg="#A3E4D7",command=generate_number)
l2 = tk.Label(bg="#F39C12",font=("Arial",30),text="")
b1.place(x=110,y=70)
l2.place(x=165,y=120)
window.mainloop()
