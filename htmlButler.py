import time

print('Text to HTML Using Python!')

filename = input('File name (exclude .html) >>> ')

document = open(str(filename)+'.html', 'w+')

def htmlStart():
    document.write('<!DOCTYPE html>\n')
    document.write('<html>\n')

def htmlFinish():
    document.write("\n\n</html>")

def htmlP(text):
    document.write('\n<p>' + str(text) + '</p>')

# Main Program

htmlStart()

for i in range(int(input('Number of lines >>> '))):
    if i == 0:
        print('Type your text')

    print('')
    print('Line number', i+1)
    htmlP(input())

htmlFinish()

print('Bravo. File made as', str(filename) + '.html in this directory.')