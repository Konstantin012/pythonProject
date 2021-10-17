filename = 'folder1/folder2/file.ext'
point_pos = filename.find('.')
# Возвращаем срез начиная с позиции после точки и до конца имени файла
print(filename[point_pos + 1:])
print(filename.partition('.')[2])
print(filename.split('.')[1])