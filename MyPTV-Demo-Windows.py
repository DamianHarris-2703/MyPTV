import tkinter as tk
from pathlib import Path

INK = "#050c1b"
NAVY = "#071329"
CARD = "#10243d"
CREAM = "#f5f8ff"
MUTED = "#b1c1d3"
MINT = "#70f1c4"
SKY = "#73bfff"


class Demo:
    def __init__(self, root):
        self.root = root
        root.title("MyPTV V3.0 Stable — Portfolio Demo")
        root.geometry("1080x700")
        root.configure(bg=INK)
        self.logo = tk.PhotoImage(file=str(Path(__file__).with_name("myptv-logo.png")))
        root.iconphoto(True, self.logo)
        self.small = self.logo.subsample(max(1, self.logo.width() // 48))
        top = tk.Frame(root, bg=NAVY, padx=20, pady=13)
        top.pack(fill="x")
        tk.Label(top, image=self.small, bg=NAVY).pack(side="left")
        tk.Label(top, text=" MyPTV  V3.0", bg=NAVY, fg=MINT, font=("Segoe UI", 17, "bold")).pack(side="left")
        for page, label in (
            ("Refresh", "REFRESH"), ("Favourites", "FAVOURITES"), ("Following", "FOLLOWING"),
            ("Sport", "SPORT"), ("Channels", "CHANNELS"), ("Home", "HOME"),
        ):
            tk.Button(
                top, text=label, command=lambda value=page: self.show(value), bg=CARD, fg=CREAM,
                activebackground=MINT, activeforeground=INK, relief="flat", padx=11, pady=8,
            ).pack(side="right", padx=3)
        self.body = tk.Frame(root, bg=INK)
        self.body.pack(fill="both", expand=True)
        self.show("Home")

    def show(self, page):
        for widget in self.body.winfo_children():
            widget.destroy()
        titles = {
            "Home": "Your television, less ordinary", "Channels": "Browse channel worlds",
            "Sport": "Never miss the main event", "Following": "Your followed competitions",
            "Favourites": "Everything you care about", "Refresh": "Guide refresh",
        }
        tk.Label(self.body, text=titles[page], bg=INK, fg=CREAM, font=("Segoe UI", 25, "bold"), anchor="w").pack(fill="x", padx=32, pady=(28, 15))
        hero = tk.Frame(self.body, bg=MINT)
        hero.pack(fill="x", padx=32)
        tk.Label(hero, text="SAFE DEMO\nFind something worth watching.", bg=MINT, fg=INK, font=("Georgia", 19, "italic"), justify="left").pack(anchor="w", padx=24, pady=20)
        tk.Label(self.body, text="GUIDE HEALTH   Healthy / fictional demonstration data", bg=NAVY, fg=MINT, padx=16, pady=12, anchor="w").pack(fill="x", padx=32, pady=15)
        area = tk.Frame(self.body, bg=INK)
        area.pack(fill="both", expand=True, padx=25)
        samples = (
            ("DEMO SPORT HD", "Weekend Football Preview"), ("DEMO CINEMA", "Sample Feature Presentation"),
            ("DEMO NATURE", "Wildlife After Dark"), ("DEMO SERIES", "The Sample Detective"),
        )
        for index, (channel, title) in enumerate(samples):
            card = tk.Frame(area, bg=CARD, highlightbackground="#294b68", highlightthickness=1)
            card.grid(row=index // 2, column=index % 2, sticky="nsew", padx=7, pady=7)
            tk.Label(card, text=channel, bg=CARD, fg=SKY).pack(anchor="w", padx=16, pady=(15, 3))
            tk.Label(card, text=title, bg=CARD, fg=CREAM, font=("Georgia", 15, "bold")).pack(anchor="w", padx=16, pady=(0, 15))
        area.grid_columnconfigure((0, 1), weight=1)
        area.grid_rowconfigure((0, 1), weight=1)


if __name__ == "__main__":
    window = tk.Tk()
    Demo(window)
    window.mainloop()
