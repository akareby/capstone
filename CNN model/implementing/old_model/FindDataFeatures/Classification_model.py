import csv
import os
import shutil

src_files = os.listdir("movie")

matrix = []
imdbid = []
genre = []
count = []


f = open('MovieGenre.csv', 'r')
csvReader = csv.reader(f)
for row in csvReader:
    matrix.append(row)
    print(row)

for i,j in enumerate(matrix):

    if i!=0 :
        imdbid.append(matrix[i][0])
print(imdbid)
for i,j in enumerate(matrix):

    if i!=0 :
        genre.append(matrix[i][1])
print(genre)


def classification(num, path):
    for i, j in enumerate(imdbid):
        if int(genre[i]) == num:
            count.append(imdbid[i])
    name = str(path)
    for i, j in enumerate(count):
        file_name = count[i]
        full_file_name = os.path.join("movie", file_name + ".jpg")
        if (os.path.isfile(full_file_name)):
            shutil.move(full_file_name, name)

for i in range(26):
    input = i + 1
    classification(input, input)


f.close()
