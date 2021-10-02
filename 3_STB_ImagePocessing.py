from PIL import Image
import numpy
import pandas as pd

nome = './STB/immagine.tif'
nome_destinazione = "./STB/image.csv"

'''importa l'immagine .tif'''
im = Image.open(nome)

'''trasforma l'immagine importata in un numpy array [matrice quadrata]'''
imarray = numpy.array(im)

'''salva il file in csv'''
numpy.savetxt(nome_destinazione, imarray, fmt='%d', delimiter=",")


'''trasforma il numpy array in formato pandas quindi una vera matrice
my_df = pd.DataFrame(imarray)

#salva il formato pandas in file .csv
my_df.to_csv('./STB/foo.csv', index=False)'''



