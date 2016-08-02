import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="file path to .html")
arg = parser.parse_args()
orgFile = arg.file
string = "<BODY BACKGROUND=\"gifs/bg9.gif\">\n"
html = open(orgFile, 'rw')
for line in html:
    str(line)
    print line
    if string != line:
        html.write(line)
html.close()
