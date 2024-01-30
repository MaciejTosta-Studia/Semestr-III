import requests
from datetime import datetime
import re
import os
from customtkinter import *
import db

hosts_path = "C://Windows//System32//drivers//etc//hosts"

def window_message(title, message):
    smth = CTk()
    message_window = CTkToplevel(smth)
    message_window.title(title)
    message_window.geometry("300x100")
    message_window.configure(bg_color="red")
    message_window.resizable(False, False)
    message_window.grid_columnconfigure(0, weight=1)
    message_window.grid_rowconfigure(0, weight=1)
    error_label = CTkLabel(message_window, text=message)

def is_website(website):
    domain_pattern = re.compile(r'^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$')
    web_pattern = re.compile(r'https?://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-]+/[a-zA-Z0-9-]+/[a-zA-Z0-9-]+/')
    if domain_pattern.match(website) or web_pattern.match(website):
        return True
    return False

def database_contents(database):
    try:
        database = (requests.get(database).text).split("\n")
        database = [w for w in database if is_website(w)]
        return database
    except Exception as e:
        window_message("error", f"Błąd {e}")

def hosts_contents():
    with open(hosts_path, "r") as hosts:
        lines = hosts.read()
        lines = [x for x in lines.split("\n") if x != ""]
    return lines

def save_to_hosts(lines):
    try:
        with open(hosts_path, "w") as hosts:
            hosts.write("\n".join(lines))
    except Exception as e:
        window_message("error", f"Błąd {e}")
    
def add_to_hosts(website, is_database):
    try:
        lines = hosts_contents()

        if is_database:
            websites = database_contents(website)
            for website in websites:
                lines.append(f"195.187.6.34 {website}")

        else:
            lines.append(f"195.187.6.34 {website}")

        save_to_hosts(set(lines))
        window_message("info", "Dodano do hosts")
    except Exception as e:
        window_message("error", f"Błąd {e}")

def remove_from_hosts(website, is_database):
    try:
        lines = hosts_contents()

        if is_database:
            websites = database_contents(website)
            lines = [x for x in lines if x.split()[-1] not in websites]

        else:
            lines = [x for x in lines if x.split()[-1] != website]

        save_to_hosts(set(lines))
        window_message("info", "Usunięto z hosts")
    except Exception as e:
        window_message("error", f"Błąd {e}")

def update_database():
    try:

        entries = db.get_entries()
        databases = [x for x in entries if x["is_database"] == True]
        if len(databases) == 0:
            return
        for database in databases:
            response = requests.get(database["website"])
            update_date = None
            if 'Last-Modified' in response.headers:
                update_date = datetime.strptime(response.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z')
            if update_date is not None and database["date"] < update_date:
                remove_from_hosts(database["website"], True)
                add_to_hosts(database["website"], True)
                db.update_entry(database["website"])
        window_message("info", "Baza danych zaktualizowana")
    except Exception as e:
        window_message("error", f"Błąd {e}")