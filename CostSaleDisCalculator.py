import tkinter as tk
from tkinter import messagebox

def calculate_profit():
    try:
        cost = float(cost_price_entry.get())
        sale = float(sale_price_entry.get())

        profit = sale - cost
        margin = (profit / cost) * 100 if cost else 0

        profit_var.set(f"{profit:.2f}")
        margin_var.set(f"{margin:.2f}%")
    except ValueError:
        messagebox.showerror("Error", "Enter valid Cost & Sale Price!")

def calculate_sale_price():
    try:
        cost = float(cost_price_entry.get())
        margin_str = margin_var.get().replace('%', '').strip()
        margin_val = float(margin_str)

        sale = cost + (cost * margin_val / 100)

        sale_price_entry.delete(0, tk.END)
        sale_price_entry.insert(0, f"{sale:.2f}")
        calculate_profit()
    except ValueError:
        messagebox.showerror("Error", "Enter valid Cost Price & Margin!")

def apply_discount():
    try:
        sale = float(sale_price_entry.get())
        discount_val = float(discount_entry.get())

        if discount_type.get() == "₹":
            final_price = sale - discount_val
            disc_percent = (discount_val / sale) * 100 if sale else 0
        else:
            disc_percent = discount_val
            discount_val = (sale * disc_percent) / 100
            final_price = sale - discount_val

        discounted_price_var.set(f"{final_price:.2f}")
        discount_amount_var.set(f"{discount_val:.2f} ({disc_percent:.2f}%)")
    except ValueError:
        messagebox.showerror("Error", "Enter valid Discount Value!")

def remove_discount():
    discounted_price_var.set("")
    discount_amount_var.set("")

def clear_all():
    cost_price_entry.delete(0, tk.END)
    sale_price_entry.delete(0, tk.END)
    profit_var.set("")
    margin_var.set("")
    discount_entry.delete(0, tk.END)
    discounted_price_var.set("")
    discount_amount_var.set("")

# Main window
root = tk.Tk()
root.title("Profit & Discount Calculator")
root.geometry("320x540")  # Fits most phone screens in portrait mode

# Font & Padding
FONT = ("Arial", 11)
PADX, PADY = 4, 4

# Variables to hold computed values
profit_var = tk.StringVar()
margin_var = tk.StringVar()
discounted_price_var = tk.StringVar()
discount_amount_var = tk.StringVar()

# Cost Price
tk.Label(root, text="Cost Price", font=FONT).grid(row=0, column=0, padx=PADX, pady=PADY, sticky="w")
cost_price_entry = tk.Entry(root, font=FONT, width=15)
cost_price_entry.grid(row=1, column=0, padx=PADX, pady=PADY)

# Sale Price
tk.Label(root, text="Sale Price", font=FONT).grid(row=2, column=0, padx=PADX, pady=PADY, sticky="w")
sale_price_entry = tk.Entry(root, font=FONT, width=15)
sale_price_entry.grid(row=3, column=0, padx=PADX, pady=PADY)

# Profit
tk.Label(root, text="Profit", font=FONT).grid(row=4, column=0, padx=PADX, pady=PADY, sticky="w")
tk.Entry(root, font=FONT, width=15, textvariable=profit_var, state="readonly").grid(row=5, column=0, padx=PADX, pady=PADY)

# Profit Margin
tk.Label(root, text="Margin %", font=FONT).grid(row=6, column=0, padx=PADX, pady=PADY, sticky="w")
tk.Entry(root, font=FONT, width=15, textvariable=margin_var).grid(row=7, column=0, padx=PADX, pady=PADY)

# Buttons for Profit Calculation
tk.Button(root, text="Calc Profit", font=FONT, command=calculate_profit).grid(row=8, column=0, padx=PADX, pady=PADY, sticky="ew")
tk.Button(root, text="Calc Sale Price", font=FONT, command=calculate_sale_price).grid(row=9, column=0, padx=PADX, pady=PADY, sticky="ew")

# Discount Value
tk.Label(root, text="Discount Value", font=FONT).grid(row=10, column=0, padx=PADX, pady=PADY, sticky="w")
discount_entry = tk.Entry(root, font=FONT, width=15)
discount_entry.grid(row=11, column=0, padx=PADX, pady=PADY)

# Discount Type Radio
discount_type = tk.StringVar(value="₹")
frame_radio = tk.Frame(root)
frame_radio.grid(row=12, column=0, pady=PADY)
tk.Radiobutton(frame_radio, text="₹", variable=discount_type, value="₹", font=FONT).pack(side="left")
tk.Radiobutton(frame_radio, text="%", variable=discount_type, value="%", font=FONT).pack(side="left")

# Buttons for Discount
tk.Button(root, text="Apply Discount", font=FONT, command=apply_discount).grid(row=13, column=0, padx=PADX, pady=PADY, sticky="ew")
tk.Button(root, text="Remove Discount", font=FONT, command=remove_discount).grid(row=14, column=0, padx=PADX, pady=PADY, sticky="ew")

# Discounted Price
tk.Label(root, text="Disc. Sale Price", font=FONT).grid(row=15, column=0, padx=PADX, pady=PADY, sticky="w")
tk.Entry(root, font=FONT, width=15, textvariable=discounted_price_var, state="readonly").grid(row=16, column=0, padx=PADX, pady=PADY)

# Discount Amount
tk.Label(root, text="Disc. Amount", font=FONT).grid(row=17, column=0, padx=PADX, pady=PADY, sticky="w")
tk.Entry(root, font=FONT, width=15, textvariable=discount_amount_var, state="readonly").grid(row=18, column=0, padx=PADX, pady=PADY)

# Clear All Button
tk.Button(root, text="Clear All", font=FONT, command=clear_all).grid(row=19, column=0, padx=PADX, pady=8, sticky="ew")

root.mainloop()