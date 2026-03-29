import tkinter as tk
from tkinter import ttk
import random

CHOICES = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

def decide_winner(player, computer):
    if player == computer:
        return "Tie"
    if (player == "Rock" and computer == "Scissors") or \
       (player == "Paper" and computer == "Rock") or \
       (player == "Scissors" and computer == "Paper"):
        return "You Win"
    return "You Lose"

class RPSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock • Paper • Scissors")
        self.root.geometry("920x560")
        self.root.minsize(820, 520)

        self.player_score = 0
        self.computer_score = 0
        self.ties = 0

        self.player_choice = tk.StringVar(value="—")
        self.computer_choice = tk.StringVar(value="—")
        self.result_text = tk.StringVar(value="Make your move!")

        self.build_theme()
        self.build_layout()

    def build_theme(self):
        self.root.configure(bg="#0B1220") 

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Title.TLabel",
                        font=("Segoe UI", 28, "bold"),
                        foreground="#EAF2FF",
                        background="#0B1220")

        style.configure("Sub.TLabel",
                        font=("Segoe UI", 12),
                        foreground="#A9B7D0",
                        background="#0B1220")

        style.configure("Card.TFrame",
                        background="#111B2E",
                        relief="flat")

        style.configure("CardTitle.TLabel",
                        font=("Segoe UI", 12, "bold"),
                        foreground="#DDE7FF",
                        background="#111B2E")

        style.configure("BigEmoji.TLabel",
                        font=("Segoe UI Emoji", 54),
                        foreground="#EAF2FF",
                        background="#111B2E")

        style.configure("ChoiceText.TLabel",
                        font=("Segoe UI", 14, "bold"),
                        foreground="#EAF2FF",
                        background="#111B2E")

        style.configure("Result.TLabel",
                        font=("Segoe UI", 18, "bold"),
                        foreground="#FFFFFF",
                        background="#111B2E")

        style.configure("Score.TLabel",
                        font=("Segoe UI", 12, "bold"),
                        foreground="#EAF2FF",
                        background="#111B2E")

    def build_layout(self):
    
        top = tk.Frame(self.root, bg="#0B1220")
        top.pack(fill="x", padx=24, pady=(18, 8))

        title = ttk.Label(top, text="Rock • Paper • Scissors", style="Title.TLabel")
        title.pack(anchor="w")

        subtitle = ttk.Label(top, text="Choose your move.",
                             style="Sub.TLabel")
        subtitle.pack(anchor="w", pady=(6, 0))
        main = tk.Frame(self.root, bg="#0B1220")
        main.pack(fill="both", expand=True, padx=24, pady=16)

        left = tk.Frame(main, bg="#0B1220")
        left.pack(side="left", fill="both", expand=True)
        right = tk.Frame(main, bg="#0B1220")
        right.pack(side="right", fill="both", expand=True, padx=(18, 0))

        controls_card = ttk.Frame(left, style="Card.TFrame", padding=18)
        controls_card.pack(fill="both", expand=True)

        ttk.Label(controls_card, text="Your Move", style="CardTitle.TLabel").pack(anchor="w")

        btn_row = tk.Frame(controls_card, bg="#111B2E")
        btn_row.pack(fill="x", pady=(14, 10))

        self.make_choice_button(btn_row, "Rock", "#1F6FEB").pack(side="left", expand=True, fill="x", padx=(0, 10))
        self.make_choice_button(btn_row, "Paper", "#2EA043").pack(side="left", expand=True, fill="x", padx=10)
        self.make_choice_button(btn_row, "Scissors", "#D29922").pack(side="left", expand=True, fill="x", padx=(10, 0))

        hint = tk.Label(controls_card,
                        text="Tip: Rock beats Scissors • Scissors beats Paper • Paper beats Rock",
                        bg="#111B2E",
                        fg="#A9B7D0",
                        font=("Segoe UI", 10))
        hint.pack(anchor="w", pady=(6, 14))

        score_card = ttk.Frame(controls_card, style="Card.TFrame", padding=16)
        score_card.pack(fill="x", pady=(4, 8))

        ttk.Label(score_card, text="Scoreboard", style="CardTitle.TLabel").grid(row=0, column=0, sticky="w")

        self.score_label = tk.Label(score_card,
                                    text=self.score_text(),
                                    bg="#111B2E",
                                    fg="#EAF2FF",
                                    font=("Segoe UI", 12, "bold"))
        self.score_label.grid(row=1, column=0, sticky="w", pady=(8, 0))

        action_row = tk.Frame(score_card, bg="#111B2E")
        action_row.grid(row=2, column=0, sticky="ew", pady=(12, 0))
        action_row.grid_columnconfigure(0, weight=1)
        action_row.grid_columnconfigure(1, weight=1)

        reset_btn = self.make_action_button(action_row, "Reset", self.reset_game, "#8B949E")
        reset_btn.grid(row=0, column=0, sticky="ew", padx=(0, 8))

        quit_btn = self.make_action_button(action_row, "Quit", self.root.destroy, "#F85149")
        quit_btn.grid(row=0, column=1, sticky="ew", padx=(8, 0))

        results_card = ttk.Frame(right, style="Card.TFrame", padding=18)
        results_card.pack(fill="both", expand=True)

        ttk.Label(results_card, text="Result", style="CardTitle.TLabel").pack(anchor="w")
        compare = tk.Frame(results_card, bg="#111B2E")
        compare.pack(fill="both", expand=True, pady=(14, 14))

        you_box = self.make_side_box(compare, "You", self.player_choice)
        you_box.pack(side="left", fill="both", expand=True, padx=(0, 10))

        cpu_box = self.make_side_box(compare, "Computer", self.computer_choice)
        cpu_box.pack(side="right", fill="both", expand=True, padx=(10, 0))

        self.result_badge = tk.Label(results_card,
                                     textvariable=self.result_text,
                                     bg="#0E7A5F",  # default green-ish
                                     fg="white",
                                     font=("Segoe UI", 14, "bold"),
                                     padx=14, pady=10)
        self.result_badge.pack(fill="x")

        footer = tk.Label(results_card,
                          text="Made with Tkinter • Emoji icons are used for compatibility",
                          bg="#111B2E",
                          fg="#A9B7D0",
                          font=("Segoe UI", 10))
        footer.pack(anchor="w", pady=(10, 0))

    def make_side_box(self, parent, title, choice_var):
        box = tk.Frame(parent, bg="#0E1526", padx=14, pady=14)
        tk.Label(box, text=title, bg="#0E1526", fg="#DDE7FF",
                 font=("Segoe UI", 12, "bold")).pack(anchor="w")

        emoji_lbl = tk.Label(box, text="—", bg="#0E1526", fg="#EAF2FF",
                             font=("Segoe UI Emoji", 56))
        emoji_lbl.pack(pady=(12, 10))

        text_lbl = tk.Label(box, text="—", bg="#0E1526", fg="#EAF2FF",
                            font=("Segoe UI", 14, "bold"))
        text_lbl.pack()
        def update_labels(*_):
            val = choice_var.get()
            if val in CHOICES:
                emoji_lbl.config(text=CHOICES[val])
                text_lbl.config(text=val)
            else:
                emoji_lbl.config(text="—")
                text_lbl.config(text="—")

        choice_var.trace_add("write", update_labels)
        update_labels()

        return box

    def make_choice_button(self, parent, choice, color):
        btn = tk.Button(parent,
                        text=f"{CHOICES[choice]}  {choice}",
                        font=("Segoe UI", 12, "bold"),
                        bg=color,
                        fg="white",
                        activebackground=color,
                        activeforeground="white",
                        bd=0,
                        relief="flat",
                        cursor="hand2",
                        padx=14, pady=12,
                        command=lambda: self.play(choice))
        def on_enter(_):
            btn.config(bg=self.darken(color))
        def on_leave(_):
            btn.config(bg=color)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn

    def make_action_button(self, parent, text, cmd, color):
        btn = tk.Button(parent,
                        text=text,
                        font=("Segoe UI", 11, "bold"),
                        bg=color,
                        fg="#0B1220",
                        activebackground=color,
                        activeforeground="#0B1220",
                        bd=0,
                        relief="flat",
                        cursor="hand2",
                        padx=14, pady=10,
                        command=cmd)

        def on_enter(_):
            btn.config(bg=self.darken(color))
        def on_leave(_):
            btn.config(bg=color)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn

    def darken(self, hex_color):
        hex_color = hex_color.lstrip("#")
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        r = max(0, int(r * 0.85))
        g = max(0, int(g * 0.85))
        b = max(0, int(b * 0.85))
        return f"#{r:02x}{g:02x}{b:02x}"

    def score_text(self):
        return f"You: {self.player_score}   Computer: {self.computer_score}   Ties: {self.ties}"

    def play(self, player):
        computer = random.choice(list(CHOICES.keys()))
        result = decide_winner(player, computer)

        self.player_choice.set(player)
        self.computer_choice.set(computer)

        if result == "You Win":
            self.player_score += 1
            self.result_text.set("✅ You Win!")
            self.result_badge.config(bg="#2EA043") # green
        elif result == "You Lose":
            self.computer_score += 1
            self.result_text.set("❌ You Lose!")
            self.result_badge.config(bg="#F85149") # red
        else:
            self.ties += 1
            self.result_text.set("🤝 It's a Tie!")
            self.result_badge.config(bg="#D29922") # amber

        self.score_label.config(text=self.score_text())

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.player_choice.set("—")
        self.computer_choice.set("—")
        self.result_text.set("Make your move!")
        self.result_badge.config(bg="#0E7A5F")
        self.score_label.config(text=self.score_text())

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSApp(root)
    root.mainloop()
