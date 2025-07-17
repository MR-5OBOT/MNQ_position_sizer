import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


def calculate_position_size():
    try:
        stop_loss = float(entry_sl.get())
        risk_amount = float(entry_risk.get())
        balance = float(entry_balance.get())
        point_value = float(entry_point_value.get())

        if stop_loss <= 0 or risk_amount <= 0 or balance <= 0 or point_value <= 0:
            raise ValueError

        if risk_amount > balance * 0.05:
            messagebox.showwarning(
                "Risk Warning", "You're risking more than 5% of your account!"
            )

        contracts = risk_amount / (stop_loss * point_value)
        result_var.set(f"{contracts:.2f} MNQ Contracts")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


# === Root Window ===
root = tk.Tk()
root.title("MNQ Position Size Calculator")
root.configure(bg="#121212")
root.geometry("330x450")
root.resizable(False, False)

# === Style ===
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#121212")
style.configure(
    "TLabel", background="#121212", foreground="white", font=("Segoe UI", 10)
)
style.configure(
    "TEntry", fieldbackground="#1e1e1e", foreground="white", insertcolor="white"
)
style.configure(
    "Calc.TButton",
    font=("Segoe UI", 10, "bold"),
    padding=5,
    background="#333333",
    foreground="white",
)
style.map(
    "Calc.TButton",
    background=[("active", "#444444"), ("pressed", "#222222")],
    foreground=[("active", "white"), ("pressed", "white")],
)

# === Frame ===
frame = ttk.Frame(root, padding=(5, 5))
frame.pack(fill="both", expand=True)

# === Logo ===
try:
    image = Image.open("/home/mr5obot/Pictures/mr5obot-logo.png")
    image = image.resize((80, 80), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    ttk.Label(frame, image=photo).pack(pady=(0, 5))
except Exception as e:
    print(f"Image error: {e}")

# === Title ===
ttk.Label(frame, text="MNQ POSITION SIZER", font=("Segoe UI", 13, "bold")).pack(
    pady=(0, 10)
)


# === Input Builder ===
def make_labeled_input(label_text, default_value):
    ttk.Label(frame, text=label_text, anchor="center", justify="center").pack(
        pady=(6, 0)
    )
    entry = ttk.Entry(frame, width=24)
    entry.insert(0, default_value)
    entry.pack()
    return entry


# === Inputs with Labels and Defaults ===
entry_sl = make_labeled_input("Stop Loss (points):", "50")
entry_risk = make_labeled_input("Risk ($):", "500")
entry_balance = make_labeled_input("Account Balance ($):", "100000")
entry_point_value = make_labeled_input("Point Value ($):", "2.00")

# === Button ===
ttk.Button(
    frame, text="Calculate", command=calculate_position_size, style="Calc.TButton"
).pack(pady=20)

# === Result ===
result_var = tk.StringVar()
ttk.Label(frame, textvariable=result_var, font=("Segoe UI", 11, "bold")).pack()


root.mainloop()
