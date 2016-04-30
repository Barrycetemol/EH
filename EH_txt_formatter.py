import os

FileCount = 0
    
def format(read):
    rfile = open(read, 'r')
    filename = str(read[:-4]) + "_formatted.txt"
    print filename
    wfile = open(filename, 'w')
    count = 0
    for i in rfile.read():
        if count < 0 and i == '\t':
            pass
        else:
            wfile.write(i)
            count = 0
    rfile.close()
    wfile.close()
            
for root, dirs, files in os.walk(os.path.dirname((os.path.realpath(__file__)))):
    for file in files:
        if file.lower().endswith('_formatted.txt'):
            pass
        elif file.lower().endswith('.txt'):
            format(os.path.join(root, file))
            FileCount += 1


print("Conversion completed: " + str(FileCount)+ " Readme files created.")
raw_input()