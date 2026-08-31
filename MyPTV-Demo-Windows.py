import tkinter as tk
from pathlib import Path
INK="#071a1d"; RAIL="#041316"; CARD="#12363b"; CREAM="#f6f0df"; MUTED="#9fb6b2"; CORAL="#ff6b4a"; LIME="#c8f169"
class Demo:
 def __init__(self,r):
  self.r=r;r.title("MyPTV V2.0 — Portfolio Demo");r.geometry("1080x700");r.configure(bg=INK);self.logo=tk.PhotoImage(file=str(Path(__file__).with_name('myptv-logo.png')));r.iconphoto(True,self.logo)
  rail=tk.Frame(r,bg=RAIL,width=220);rail.pack(side='left',fill='y');rail.pack_propagate(False);self.small=self.logo.subsample(max(1,self.logo.width()//58));h=tk.Frame(rail,bg=RAIL);h.pack(padx=18,pady=20);tk.Label(h,image=self.small,bg=RAIL).pack(side='left');tk.Label(h,text=' MyPTV\n DEMO',bg=RAIL,fg=CORAL,font=('Segoe UI',17,'bold')).pack(side='left')
  self.body=tk.Frame(r,bg=INK);self.body.pack(fill='both',expand=True)
  for n in ('Home','Provider categories','Favourites','Refresh guide','Live sport','On demand'):tk.Button(rail,text=n,command=lambda x=n:self.show(x),bg=RAIL,fg=CREAM,activebackground=CARD,activeforeground=LIME,relief='flat',anchor='w',font=('Segoe UI',11,'bold'),padx=22,pady=10).pack(fill='x')
  tk.Label(rail,text='PORTFOLIO SIMULATION\nNo network access',bg=RAIL,fg=MUTED,justify='left').pack(side='bottom',anchor='w',padx=22,pady=20);self.show('Home')
 def show(self,page):
  for w in self.body.winfo_children():w.destroy()
  titles={'Home':'Your television, less ordinary','Provider categories':'Browse channel worlds','Favourites':'Your favourites','Refresh guide':'Guide refresh','Live sport':'Never miss the main event','On demand':'Movies & series'};tk.Label(self.body,text=titles[page],bg=INK,fg=CREAM,font=('Segoe UI',25,'bold'),anchor='w').pack(fill='x',padx=32,pady=(28,15));hero=tk.Frame(self.body,bg=CORAL);hero.pack(fill='x',padx=32);tk.Label(hero,text='SAFE DEMO\nFind something worth watching.',bg=CORAL,fg=INK,font=('Georgia',19,'italic'),justify='left').pack(anchor='w',padx=24,pady=20);tk.Label(self.body,text='GUIDE HEALTH   Healthy / 1,058 fictional channels / 52,262 fictional listings',bg='#0d2b30',fg=LIME,padx=16,pady=12,anchor='w').pack(fill='x',padx=32,pady=15)
  area=tk.Frame(self.body,bg=INK);area.pack(fill='both',expand=True,padx=25);samples=[('DEMO SPORT HD','Weekend Football Preview'),('DEMO CINEMA','Sample Feature Presentation'),('DEMO NATURE','Wildlife After Dark'),('DEMO SERIES','The Sample Detective')]
  for i,(c,t) in enumerate(samples):f=tk.Frame(area,bg=CARD,highlightbackground='#315e65',highlightthickness=1);f.grid(row=i//2,column=i%2,sticky='nsew',padx=7,pady=7);tk.Label(f,text=c,bg=CARD,fg='#62d5e5').pack(anchor='w',padx=16,pady=(15,3));tk.Label(f,text=t,bg=CARD,fg=CREAM,font=('Georgia',15,'bold')).pack(anchor='w',padx=16,pady=(0,15))
  area.grid_columnconfigure((0,1),weight=1);area.grid_rowconfigure((0,1),weight=1)
if __name__=='__main__':r=tk.Tk();Demo(r);r.mainloop()
