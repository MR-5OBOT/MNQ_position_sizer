import tkinter as tk
from tkinter import ttk, messagebox


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
                "Warning", "You are risking more than 5% of your account."
            )

        contracts = risk_amount / (stop_loss * point_value)
        result_var.set(f"{contracts:.2f} MNQ Contracts")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid positive numbers.")


# GUI setup
root = tk.Tk()
root.title("MNQ Position Size Calculator")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Theme & style
style = ttk.Style(root)
style.theme_use("clam")
style.configure(
    "TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 10)
)
style.configure("TEntry", fieldbackground="#2b2b2b", foreground="white")
style.configure(
    "TButton",
    background="#1a1a1a",
    foreground="white",
    font=("Segoe UI", 10, "bold"),
    borderwidth=1,
)

style.map(
    "TButton",
    background=[("active", "#000000"), ("pressed", "#1a1a1a")],
    foreground=[("active", "white"), ("pressed", "white")],
)

# Title Label
ttk.Label(
    root,
    text="📈 MNQ POSITION SIZER",
    font=("Segoe UI", 14, "bold"),
    anchor="center",
    justify="center",
).grid(column=0, row=0, columnspan=2, pady=(15, 10))

# Labels and entries
ttk.Label(root, text="Stop Loss (points):").grid(
    column=0, row=1, padx=10, pady=8, sticky="w"
)
entry_sl = ttk.Entry(root, width=20)
entry_sl.grid(column=1, row=1, padx=10)

ttk.Label(root, text="Risk ($):").grid(column=0, row=2, padx=10, pady=8, sticky="w")
entry_risk = ttk.Entry(root, width=20)
entry_risk.insert(0, "500")  # Default MNQ point value
entry_risk.grid(column=1, row=2, padx=10)

ttk.Label(root, text="Account Balance ($):").grid(
    column=0, row=3, padx=10, pady=8, sticky="w"
)
entry_balance = ttk.Entry(root, width=20)
entry_balance.insert(0, "100000")  # Default MNQ point value
entry_balance.grid(column=1, row=3, padx=10)

ttk.Label(root, text="Point Value ($):").grid(
    column=0, row=4, padx=10, pady=8, sticky="w"
)
entry_point_value = ttk.Entry(root, width=20)
entry_point_value.insert(0, "2.00")  # Default MNQ point value
entry_point_value.grid(column=1, row=4, padx=10)

# Calculate Button
ttk.Button(root, text="Calculate", command=calculate_position_size).grid(
    column=0, row=5, columnspan=2, pady=15
)

# Result label
result_var = tk.StringVar()
ttk.Label(root, textvariable=result_var, font=("Segoe UI", 11, "bold")).grid(
    column=0, row=6, columnspan=2, pady=10
)

# Run App
root.mainloop()
