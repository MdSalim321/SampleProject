fileName = "DataSet/InputFile.txt"
with open(fileName) as fileObject:
    lines = fileObject.readline()

for line in lines:
    print(line)