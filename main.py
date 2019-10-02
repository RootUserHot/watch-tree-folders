import os
from PIL import Image, ImageDraw, ImageFont
import argparse

parser = argparse.ArgumentParser(description='desc')
parser.add_argument('path', help='Write path to files - myfiles/folder1/...')
parser.add_argument('nesting', help='Nesting folder, max 10')
args = parser.parse_args()

def createTree(path, nesting):
    nameFile = 'result.png'
    img = Image.new('RGB', (300, 500), color=(73, 109, 137))
    font = ImageFont.truetype("Lato-Black.ttf", 13)
    d = ImageDraw.Draw(img)
    strFile = path + ' - root directory'
    bigData = '\n Very big data... '
    count = 0
    for root, dirs, files in os.walk(path):
        if count >= 25:
            d.text((1, 1), strFile + bigData, font=font, fill=(255, 255, 0))
            img.save(nameFile)
            imgOpen = Image.open(nameFile)
            return exit(imgOpen.show())
        path = root.split(os.sep)
        if len(path) >= int(nesting) and int(nesting) <= 10:
            continue
        s = (len(path) - 1) * '***', os.path.basename(root)
        strFile = strFile + '\n' + str(s)
        count = count + 1
    d.text((1, 1), strFile, font=font, fill=(255, 255, 0))
    img.save(nameFile)
    imgOpen = Image.open(nameFile)
    return exit(imgOpen.show())

if __name__ == '__main__':
    input(createTree(args.path, args.nesting))