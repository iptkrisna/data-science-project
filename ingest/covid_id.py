import os
import requests
import json
import csv

def download():
    url = 'https://data.covid19.go.id/public/api/update.json?_=1592281989293'
    covid_path = os.path.abspath(os.getcwd()) + '/data/covid_id.csv'
    with open(covid_path, 'w') as fp:
        response = requests.get(url)
        writer = csv.writer(fp)
        data = response.json()
#         writer.writerow('tanggal,key,jumlah_item,jumlah_meninggal,jumlah_sembuh,jumlah_positif,jumlah_dirawat,jumlah_positif_kum,jumlah_sembuh_kum,jumlah_meninggal_kum,jumlah_dirawat_kum')
        fp.write('tanggal,key,jumlah_item,jumlah_meninggal,jumlah_sembuh,jumlah_positif,jumlah_dirawat,jumlah_positif_kum,jumlah_sembuh_kum,jumlah_meninggal_kum,jumlah_dirawat_kum\n')
        for ln in data['update']['harian']:
            item = ''
            line = ln.values()
            line_iterator = iter(line)
            tanggal = str(next(line_iterator))
            key = str(next(line_iterator))
            jumlah_item = str(next(line_iterator))
            jumlah_meninggal = str(next(line_iterator)['value'])
            jumlah_sembuh = str(next(line_iterator)['value'])
            jumlah_positif = str(next(line_iterator)['value'])
            jumlah_dirawat = str(next(line_iterator)['value'])
            jumlah_positif_kum = str(next(line_iterator)['value'])
            jumlah_sembuh_kum = str(next(line_iterator)['value'])
            jumlah_meninggal_kum = str(next(line_iterator)['value'])
            jumlah_dirawat_kum = str(next(line_iterator)['value'])
            item = tanggal + ',' + key + ',' + jumlah_item + ',' + jumlah_meninggal + ',' + jumlah_sembuh + ',' + jumlah_positif + ',' + jumlah_dirawat + ',' + jumlah_positif_kum + ',' + jumlah_sembuh_kum + ',' + jumlah_meninggal_kum + ',' + jumlah_dirawat_kum + '\n'
            fp.write(item)

def combine():
    covid_path = os.path.abspath(os.getcwd()) + '/data/covid_id.csv'
    ihsg_path = os.path.abspath(os.getcwd()) + '/data/ihsg.csv'
    combine_path = os.path.abspath(os.getcwd()) + '/data/combine.csv'
    with open(covid_path, 'r') as fp, open(ihsg_path, 'r') as fq, open(combine_path, 'w') as fr:
        covid = reader(fp)
        ihsg = reader(fq)
        covid_iterator = iter(covid)
        ihsg_iterator = iter(ihsg)
        next(ihsg_iterator)
        counter = 0
        for row in covid:
            print(next(covid_iterator))
if __name__ == '__main__':
    combine()
