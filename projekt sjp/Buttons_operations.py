import db
import Functions

def add_database(database, is_database):
    Functions.add_to_hosts(database, is_database)
    db.add_entry(database, is_database)

def add_website(website, is_database):
    Functions.add_to_hosts(website, is_database)
    db.add_entry(website, is_database)

def remove_database(database, is_database):
    Functions.remove_from_hosts(database, is_database)
    db.remove_entry(database)

def remove_website(website, is_database):
    Functions.remove_from_hosts(website, is_database)
    db.remove_entry(website)