import csv

def result_exporter(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["page_faults", "frames"])
        for row in data:
            writer.writerow(row)

def input_exporter(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["dataset"])
        for row in data:
            writer.writerow([row])
        
