'''AutoMagicProoferThing'''

from datetime import datetime

#---------
#Settings
#---------

size("A4Landscape")
margin = 40
gutter = 20
fallbackFont("LastResort")

includeDiacritics = False
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#-------------
#Calculations
#-------------
 
f = CurrentFont()
f.testInstall(showProgress=False)
fname = f.info.familyName + '-' + f.info.styleName
pageSize =  (width(), height())


def letterChecker(group):
    availableGlyphs = []
    for g in f:
        if g.name in group:
            availableGlyphs += g.name
    availableGlyphs.sort()
    return availableGlyphs

def letterSandwicher(letters, bread):
    sandwich = bread
    for letter in letters:
        sandwich += letter + bread
    return sandwich


availableLowercase = letterChecker(lowercase)
availableUppercase = letterChecker(uppercase)

allSandwiches = ''
#Check if control characters are present. If so, create sandwich string.
if "n" in f.keys():
    nSandwich = (letterSandwicher(availableLowercase, "n"))
    allSandwiches += nSandwich + '\n'
else: print("Control character 'n' not available")

if "o" in f.keys():
    oSandwich = (letterSandwicher(availableLowercase, "o"))
    allSandwiches += oSandwich + '\n'
else: print("Control character 'o' not available")

if "H" in f.keys():
    Hsandwich = (letterSandwicher(availableLowercase, "o")) 
    allSandwiches += HSandwich + '\n'
else: print("Control character 'H' not available")

if "O" in f.keys():
    Osandwich = (letterSandwicher(availableLowercase, "o"))
    allSandwiches += OSandwich + '\n'
else: print("Control character 'O' not available")

#------------
#Draw Page 1
#------------

def drawFooter(pageNumber,totalPages):
    x, y, w, h = margin, margin-10, pageSize[0]-2*margin, 30
    # fill(1,.9,.9)
    # rect(x, y, w, h)
    txt = FormattedString()
    txt.append(fname + ' ', font='InputMono-Bold')
    txt.append(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+ '\n', font='InputMono-Regular')
    txt.append(str(pageNumber) + '/' + str(totalPages), font='InputMono-Regular')
    textBox(txt, (x, y, w, h))

drawFooter(1,1)
#------------
#Footer
#------------



font(fname)
fontSize(50)
textBox(allSandwiches, (margin, margin, pageSize[0] - 2*margin, pageSize[1] - 2*margin))




#********************PAGE 2**************************


# newPage("A4Landscape")
# words = 800

# txt = ""
# def random_word(a,b):
#     key = ''
#     length = choice(range(a,b))
#     for i in range(length):
#         key += choice(letters)
#     return key
        

# for n in range(words):
#     txt += random_word(5,10)

# hyphenation(False)
# font(fname)
# fontSize(12)
# lineHeight(15)
# width = width()/3 -  4 * gutter
# textBox(txt, (margin, margin, width, (height()-2*margin)))
# fontSize(9)
# lineHeight(11)
# textBox(txt, ((margin + width + gutter), margin, width, (height()-2*margin)))
# fontSize(6)
# lineHeight(9)
# textBox(txt, ((margin + 2*width + 2*gutter), margin, width, (height()-2*margin)))


#********************PAGE 2**************************

# newPage("A4Landscape")
# font(fname)
# fontSize(100)
# upperText = ''.join(upper)[:6]
# w, _ = textSize(upperText)
# text(upperText,(margin, height()*.7))
# text("Hello",(margin + w, height()*.7))

# text(''.join(lower),(margin, height()*.5))


# saveImage("~/Desktop/Test.pdf")