# Fisrts import urlib
import urllib.request
import zipfile
import os
#workindir
working_d="../data/movies"
#destino del archiivo
file_name=working_d +"movies.zip"
#url public data
url = "https://grouplens.org/datasets/movielens/ml-lastets-small.zip"
file_name = "../data/moveies.zip"

# Download the file from `url` and save it locally under `file_name`:
#urllib.request.urlretrieve(url, file_name)
# Descomprimr archivo
if os.path.isfile(file_name):
	print("Archivo descrgad")
else:
	print("Descargado")
	urllib.request.urlretrieve(url,file_name)
#We already know the expect files so
expected_files = ['links.csv','movies.csv','rating.csv','README.txt','tgs.csv']
#THERES AN EXTRAXT DIR LEVEL IN THE EXTRAXTE FILE
inner_dir= "ml-lastest-samall"
file_names= os.listdir(working_d + inner_dir)
if files_names == expected_files:
	print("Already have that  files, check it")
else:
	path_to_zip_file = "../data/movies.zip"
	directory_to_extract_to = "../data"
	zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
	zip_ref.extractall(working_d)
#close
	zip_ref.close()

#THERES AN EXTRAXT DIR LEVEL IN THE EXTRAXTE FILE
#inner_dir= "ml-lastest-samall"
#file_names= os.listdir(working_d + inner_dir)
print(file_names)
#eer archivo
movies = pd.read_csv(
	working_d +
	inner_d + 
	expected_files [1],
	 sep= ',')
ratings =  pd.read_csv(
	working_d +
	inner_d + 
	expected_files [2], 
	sep= ',')
#imprimir
movies.head()
ratings.head()
# import pandas as pd
#movie =pd.read_csv(
