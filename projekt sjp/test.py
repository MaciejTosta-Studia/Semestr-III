import requests
import re
import Functions

hosts_path = "C://Windows//System32//drivers//etc//hosts"

Functions.add_to_hosts("https://hole.cert.pl/domains/v2/domains.txt", True)