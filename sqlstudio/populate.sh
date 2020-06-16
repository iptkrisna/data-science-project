#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: ./populate_table.sh  bucket-name"
    exit
fi

BUCKET=$1
echo "Populating Cloud SQL instance flights from gs://${BUCKET}/covid-ihsg/raw/..."

# To run mysqlimport and mysql, authorize CloudShell
bash authorize_cloudshell.sh

# the table name for mysqlimport comes from the filename, so rename our CSV files, changing bucket name as needed
#for FILE in $(gsutil ls gs://${BUCKET}/flights/raw/2015*.csv); do
#   gsutil cp $FILE flights.csv-${counter}
gsutil cp gs://${BUCKET}/flights/raw/combine.csv covid-ihsg.csv

# import csv files
MYSQLIP=$(gcloud sql instances describe covid-ihsg --format="value(ipAddresses.ipAddress)")
mysqlimport --local --host=$MYSQLIP --user=root --ignore-lines=1 --fields-terminated-by=',' --password bts covid-ihsg.csv
rm covid-ihsg.csv
