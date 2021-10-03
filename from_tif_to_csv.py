from PIL import Image
import numpy
# import pandas as pd
import os

## CONSTANTS
# Region from which the data is taken (50°N, 125°W to 40°N, 115°W)
MIN_LAT = 40
MAX_LAT = 50
MIN_LONG = -125
MAX_LONG = -115
# Ratio of resizing
SIZE_RATIO = 4
REQUESTED_FILE_SIZE = int(3600/SIZE_RATIO)    # Uguale altezza e larghezza
# Number of maps for each row & column
IMAGES_PER_ROW = MAX_LONG - MIN_LONG
IMAGES_PER_COLUMN = MAX_LAT - MIN_LAT

# Useful locations
DATA_DIRECTORY = './data/'
final_path = f"./new_data/N50W125-N40W115fct{SIZE_RATIO}.csv"

# pre-allocating for matrix hosting all the values
final_matrix = numpy.zeros((IMAGES_PER_ROW * REQUESTED_FILE_SIZE, IMAGES_PER_COLUMN * REQUESTED_FILE_SIZE))

# Runs through the whole set of files in the directory given
# The next operations work only if the file has a specific name structure
# ex. ALPSMLC30_N040W116_DSM.tif    (Important factors are the coordinates format and position)
total_file_number = len(os.listdir(DATA_DIRECTORY))
count = 0
for file in os.listdir(DATA_DIRECTORY):
    count += 1
    # Extract coordinates from the file name
    file_name = os.path.basename(file)
    print('Loading files from', file_name, f'{count}/{total_file_number}')
    file_name = os.path.splitext(file_name)[0]

    coordinates = file_name.split('_')[1]
    coordinates_n = coordinates[1:4]
    coordinates_w = coordinates[-3:]
    # indexes to concatenate images (specific to North-West coordinates for simplicity)
    x = int((MAX_LAT - int(coordinates_n) - 1))     # North
    y = int((-int(coordinates_w) - MIN_LONG))   # West

    # Opens the image from the file and resizes it
    im = Image.open(DATA_DIRECTORY + file)
    im = im.resize((REQUESTED_FILE_SIZE, REQUESTED_FILE_SIZE), resample=Image.BILINEAR)
    im_array = numpy.array(im)
    # Saves the array in the correct position based on the coordinates
    init_pos = (REQUESTED_FILE_SIZE*x, REQUESTED_FILE_SIZE*y)
    end_pos = (REQUESTED_FILE_SIZE*(x+1), REQUESTED_FILE_SIZE*(y+1))
    final_matrix[init_pos[0]:end_pos[0], init_pos[1]:end_pos[1]] = im_array
    # print(im_array.shape)

# Saves the image as a single ".csv" file
print('Saving files to', final_path)
numpy.savetxt(final_path, final_matrix, fmt='%d', delimiter=",")

'''trasforma il numpy array in formato pandas quindi una vera matrice
my_df = pd.DataFrame(imarray)
#salva il formato pandas in file .csv
my_df.to_csv('./STB/foo.csv', index=False)'''