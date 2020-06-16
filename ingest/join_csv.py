import os
import glob
import pandas as pd

def join():
    os.chdir("../data/index")
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv( "combined_index.csv", index=False, encoding='utf-8-sig')

if __name__ == '__main__':
    join()
