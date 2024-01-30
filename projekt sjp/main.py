from customtkinter import *
import Functions
from Buttons_operations import *
import db
import datetime

class DataFrame(CTkFrame):

    def update_listbox(self):
        self.listbox.configure(state="normal")
        self.listbox.delete("1.0", END)
        entries = db.get_entries()
        for entry in entries:
            self.listbox.insert("end", f"{entry['website']} - {entry['date']}\n")
        self.listbox.configure(state="disabled")

    def __init__(self, master):
        super().__init__(master)

        self.website_frame = CTkFrame(self)
        self.website_frame.grid(row=0, column=0, padx=10, pady=0, sticky="news")
        self.website_frame.configure(fg_color="transparent")
        self.label1 = CTkLabel(self.website_frame, text="Wprowadź adres strony:")
        self.label1.pack(side="top")
        self.website_entry = CTkEntry(self.website_frame, placeholder_text="np. google.com")
        self.website_entry.pack(side="bottom")
        self.website_entry.configure(width=450, height=30)
        
        self.button_frame1 = CTkFrame(self)
        self.button_frame1.grid(row=1, column=0, padx=250, pady=0, sticky="w")
        self.button_addwebsite = CTkButton(self.button_frame1, text="Dodaj stronę", command=lambda: add_website(self.website_entry.get(), False), border_width=1, fg_color="green")
        self.button_addwebsite.pack(side="left")
        self.button_removewebsite = CTkButton(self.button_frame1, text="Usuń stronę", command=lambda: remove_website(self.website_entry.get(), False), border_width=1, fg_color="red")
        self.button_removewebsite.pack(side="left")


        self.database_frame = CTkFrame(self)
        self.database_frame.grid(row=2, column=0, padx=10, pady=0, sticky="news")
        self.database_frame.configure(fg_color="transparent")
        self.label2 = CTkLabel(self.database_frame, text="Wprowadź adres bazy stron:")
        self.label2.pack(side="top")
        self.database_entry = CTkEntry(self.database_frame, placeholder_text="https://hole.cert.pl/domains/v2/domains_hosts.txt")
        self.database_entry.pack(side="bottom")
        self.database_entry.configure(width=450, height=30)
        
        self.button_frame2 = CTkFrame(self)
        self.button_frame2.grid(row=3, column=0, padx=250, pady=0, sticky="w")
        self.button_add_database = CTkButton(self.button_frame2, text="Dodaj stronę", command=lambda: add_database(self.database_entry.get(), True), border_width=1, fg_color="green")
        self.button_add_database.pack(side="left")
        self.button_remove_database = CTkButton(self.button_frame2, text="Usuń stronę", command= lambda: remove_database(self.database_entry.get(), True), border_width=1, fg_color="red")
        self.button_remove_database.pack(side="left")

        self.label3 = CTkLabel(self, text="Lista baz oraz wykluczonych stron:")
        self.label3.grid(row=6, column=0, padx=10, pady=0, sticky="news")
        self.label3.configure(justify="center", anchor="center")
        self.listbox = CTkTextbox(self)
        self.listbox.grid(row=7, column=0, padx=10, pady=0, sticky="nesw")
        self.button = CTkButton(self, text="Update", command=self.update_listbox)
        self.button.grid(row=8, column=0, padx=10, pady=0, sticky="nesw")

        self.grid_columnconfigure(0, minsize=200)  # Set the minimum width of column 0 to 200 pixels
        self.grid_rowconfigure(7, minsize=450)  # Set the minimum height of row 4 to 350 pixels

        items = db.get_entries()
        items = [str({x["website"]: x["date"].strftime('%Y-%m-%d %H:%M:%S')}) for x in items]
        for item in items:
            self.listbox.insert(END, item[1:-1])
            self.listbox.insert(END, "\n")
        
        self.listbox.configure(state="disabled")



class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.data_frame = DataFrame(self)
        self.data_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="news")
        
        self.grid_columnconfigure(0, minsize=400)  # Set the minimum width of column 0 to 400 pixels
        self.grid_rowconfigure(0, minsize=680)



if __name__ == "__main__":
    app = App()
    Functions.update_database()
    DataFrame.update_listbox(app.data_frame)
    app.mainloop()