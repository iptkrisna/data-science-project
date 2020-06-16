import os
import requests
import json

def download():
    url = 'https://data.covid19.go.id/public/api/update.json?_=1592281989293'
    filename = os.path.abspath(os.getcwd()) + '/data/covid_id.csv'
    print(filename)
    with open(filename, 'w') as fp:
        response = requests.get(url)
        data = response.json()
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

if __name__ == '__main__':
    download()
