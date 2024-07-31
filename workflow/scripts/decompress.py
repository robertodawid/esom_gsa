import gzip
import shutil
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with gzip.open(input_file, 'rb') as f_in:
    with open(output_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)