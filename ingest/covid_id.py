import os
import requests
import json
import csv
from google.cloud import storage
from google.cloud.storage import Blob

def download():
    url = 'https://data.covid19.go.id/public/api/update.json?_=1592281989293'
    covid_path = os.path.abspath(os.getcwd()) + '/data/covid_id.csv'
    with open(covid_path, 'w') as fp:
        response = requests.get(url)
        writer = csv.writer(fp)
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
        gcsfile = upload(fp)
        logging.info('Success download... ingested to {}'.format(gcsfile))
        combine()

def combine():
    covid_path = os.path.abspath(os.getcwd()) + '/data/covid_id.csv'
    ihsg_path = os.path.abspath(os.getcwd()) + '/data/ihsg.csv'
    combine_path = os.path.abspath(os.getcwd()) + '/data/combine.csv'
    with open(covid_path, 'r') as fp, open(ihsg_path, 'r') as fq, open(combine_path, 'w') as fr:
        covid = reader(fp)
        ihsg = reader(fq)
        ihsg_iterator = iter(ihsg)
        counter = 0
        ihsg_i = next(ihsg_iterator)
        for row in covid:
            try:
                counter += 1
                if (counter < 6):
                    print(row + ihsg_i)
                    item = row + ihsg_i[1:]
                    fr.write(','.join(item) + '\n')
                    ihsg_i = next(ihsg_iterator)
                else:
                    print(row, ihsg_i)
                    item = row + ihsg_i[1:]
                    fr.write(','.join(item) + '\n')
                if counter > 6:
                    counter = 0
            except StopIteration:
                break
        gcsfile = upload(fr)
        logging.info('Success combine... ingested to {}'.format(gcsfile))

def upload(csvfile):
    bucketname = 'dsp-covid-ihsg'
    blobname = 'covid_ihsg/raw/{}'.format(os.path.basename(csvfile))
    client = storage.Client()
    bucket = client.get_bucket(bucketname)
    blob = Blob(blobname, bucket)
    blob.upload_from_filename(csvfile)
    gcslocation = 'gs://{}/{}'.format(bucketname, blobname)
    logging.info('Uploaded {} ...'.format(gcslocation))
    return gcslocation

if __name__ == '__main__':
    download()
