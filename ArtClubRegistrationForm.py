import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ArtClubRegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Art Club Registration Form")

        # Set background image
        try:
            self.background_image = tk.PhotoImage(file='c:\\Users\\End User\\Desktop\\PYTHON\\vangogh.png')
            background_label = tk.Label(self.root, image=self.background_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except tk.TclError:
            # Handle the case where the image file is not found
            messagebox.showerror("Image Error", "Background image not found.")

        # Registration Fields
        self.fields = ["Name", "Age", "Contact Number", "Email", "Art Style"]

        # Create a dictionary to store data
        self.data = {}

        # Create Treeview for displaying registered data
        self.tree = ttk.Treeview(self.root, columns=self.fields, show="headings", selectmode="browse")
        for field in self.fields:
            self.tree.heading(field, text=field)
            self.tree.column(field, anchor="center")
        self.tree.pack(pady=20)

        # Registration Form
        self.create_registration_form()

        # Buttons
        self.register_button = tk.Button(self.root, text="Register", command=self.register_data)
        self.register_button.pack(side=tk.LEFT, padx=10)

        self.update_button = tk.Button(self.root, text="Update", command=self.update_data)
        self.update_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_data)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        self.view_all_button = tk.Button(self.root, text="View All", command=self.view_all_data)
        self.view_all_button.pack(side=tk.LEFT, padx=10)

    def create_registration_form(self):
        self.entries = {}
        for field in self.fields[:-1]:  # Exclude "Art Style" for dropdown
            label = tk.Label(self.root, text=field + ":")
            label.pack()

            entry = tk.Entry(self.root)
            entry.pack()
            self.entries[field] = entry

        # Art Style Dropdown
        label = tk.Label(self.root, text="Art Style:")
        label.pack()

        art_styles = ["Painting", "Sculpture", "Photography", "Digital Art", "Batik"]
        self.art_style_var = tk.StringVar()
        art_style_dropdown = ttk.Combobox(self.root, textvariable=self.art_style_var, values=art_styles)
        art_style_dropdown.pack()

    def register_data(self):
        data_entry = [entry.get() for entry in self.entries.values()]
        art_style = self.art_style_var.get()

        if all(data_entry) and art_style:
            self.data[data_entry[0]] = data_entry[1:] + [art_style]
            self.update_treeview()
            self.clear_entries()
        else:
            messagebox.showwarning("Incomplete Data", "Please fill out all fields.")

    def update_data(self):
        selected_item = self.tree.selection()
        if selected_item:
            data_entry = [entry.get() for entry in self.entries.values()]
            art_style = self.art_style_var.get()

            if all(data_entry) and art_style:
                selected_name = self.tree.item(selected_item, "values")[0]
                self.data[selected_name] = data_entry[1:] + [art_style]
                self.update_treeview()
                self.clear_entries()
            else:
                messagebox.showwarning("Incomplete Data", "Please fill out all fields.")
        else:
            messagebox.showwarning("No Selection", "Please select a record to update.")

    def delete_data(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_name = self.tree.item(selected_item, "values")[0]
            del self.data[selected_name]
            self.update_treeview()
            self.clear_entries()
        else:
            messagebox.showwarning("No Selection", "Please select a record to delete.")

    def view_all_data(self):
        self.tree.delete(*self.tree.get_children())
        for name, details in self.data.items():
            self.tree.insert("", "end", values=[name] + details)

    def update_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for name, details in self.data.items():
            self.tree.insert("", "end", values=[name] + details)

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.art_style_var.set("")  # Clear the art style dropdown selection

if __name__ == "__main__":
    root = tk.Tk()
    app = ArtClubRegistrationForm(root)
    root.mainloop()