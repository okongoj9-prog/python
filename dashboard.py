from tkinter import*
from PIL import Image,ImageTK #pip install pillow
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Result Managment System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #===icons====
        self.logo_dash= Images.open("")
        #====title====
        title=Label(self.root,text="Student Result Managment System",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #====Menu===
        M


if __name__=="__main__":
    root==Tk()
    obj=RMS(root)
    root.mainloop()