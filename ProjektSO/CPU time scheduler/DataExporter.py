import csv

def export_data(result, path):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(list(result[0].keys()))
        for row in result:
            writer.writerow(list(row.values()))