import tkinter as tk
from book_loans import checkout as checkout_book   # corrected import


class CheckoutScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")

        # ------- CARD CONTAINER -------
        card = tk.Frame(
            self,
            bg="#f2f2f2",          # light gray card (visible but clean)
            bd=1,
            relief="solid",
            padx=40,
            pady=35
        )
        card.place(relx=0.5, rely=0.5, anchor="center")

        # ------- TITLE -------
        tk.Label(
            card,
            text="Checkout Book",
            font=("Arial", 22, "bold"),
            bg="#f2f2f2",
            fg="black"
        ).grid(row=0, column=0, columnspan=2, pady=(0, 15))

        # ------- BULLET INSTRUCTIONS -------
        bullet_texts = [
            "Enter an ISBN and Borrower ID to check out a book.",
            "Borrowers may check out up to 3 books.",
            "Books already checked out cannot be checked out again.",
            "Borrowers with unpaid fines cannot check out books."
        ]

        bullet_frame = tk.Frame(card, bg="#f2f2f2")
        bullet_frame.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 20))

        for text in bullet_texts:
            tk.Label(
                bullet_frame,
                text="• " + text,
                font=("Arial", 12),
                bg="#f2f2f2",
                fg="black",
                anchor="w",
                justify="left"
            ).pack(anchor="w", pady=3)

        # ------- ISBN ROW -------
        tk.Label(
            card,
            text="ISBN:",
            font=("Arial", 13),
            bg="#f2f2f2",
            fg="black"
        ).grid(row=2, column=0, sticky="e", padx=(0, 10), pady=10)

        self.isbn_entry = tk.Entry(
            card,
            font=("Arial", 13),
            width=28,
            bg="white",
            fg="black",
            relief="solid",
            bd=1,
            insertbackground="black"
        )
        self.isbn_entry.grid(row=2, column=1, sticky="w", pady=10)

        # ------- BORROWER ID ROW -------
        tk.Label(
            card,
            text="Borrower ID:",
            font=("Arial", 13),
            bg="#f2f2f2",
            fg="black"
        ).grid(row=3, column=0, sticky="e", padx=(0, 10), pady=10)

        self.card_entry = tk.Entry(
            card,
            font=("Arial", 13),
            width=28,
            bg="white",
            fg="black",
            relief="solid",
            bd=1,
            insertbackground="black"
        )
        self.card_entry.grid(row=3, column=1, sticky="w", pady=10)

        # ------- CHECKOUT BUTTON -------
        self.checkout_btn = tk.Button(
            card,
            text="Checkout Book",
            font=("Arial", 13, "bold"),
            bg="white",
            fg="black",
            bd=2,
            relief="raised",
            padx=20,
            pady=8,
            activebackground="#e6e6e6",
            activeforeground="black",
            command=self.checkout_action
        )
        self.checkout_btn.grid(row=4, column=0, columnspan=2, pady=20)

        # Hover effect (subtle professional)
        self.checkout_btn.bind("<Enter>", lambda e: self.checkout_btn.config(bg="#f0f0f0"))
        self.checkout_btn.bind("<Leave>", lambda e: self.checkout_btn.config(bg="white"))

        # ------- STATUS LABEL -------
        self.status_label = tk.Label(
            card,
            text="",
            font=("Arial", 12),
            bg="#f2f2f2",
            fg="black",
            wraplength=400,
            justify="center"
        )
        self.status_label.grid(row=5, column=0, columnspan=2, pady=(10, 0))

    # ------- CHECKOUT ACTION -------
    def checkout_action(self):
        isbn = self.isbn_entry.get().strip()
        card_id = self.card_entry.get().strip()

        if not isbn or not card_id:
            self.status_label.config(text="ERROR: ISBN and Borrower ID required.", fg="red")
            return

        result = checkout_book(isbn, card_id)

        if result.startswith("SUCCESS"):
            self.status_label.config(text=result, fg="green")
        else:
            self.status_label.config(text=result, fg="red")


# ------- RUN WINDOW -------
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library System - Checkout")
    root.geometry("900x600")
    root.configure(bg="white")

    CheckoutScreen(root).pack(fill="both", expand=True)

    root.mainloop()
