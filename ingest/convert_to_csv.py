import pandas as pd
import os

def convert():
    for root, dirs, files in os.walk('../data/index'):
        for file in files:
            if file.endswith('.TXT'):
                print(file)
                newFile = file.replace('.TXT', '')
                print(newFile)
                read_file = pd.read_csv (r'../data/'+ newFile +'.TXT')
                read_file.to_csv (r'../data/'+ newFile +'.csv', index=None)

if __name__ == '__main__':
    convert()
