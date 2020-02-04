'''AutoMagicProoferThing'''

from datetime import datetime

#---------
#Settings
#---------

pageSize = 'LetterLandscape'
size(pageSize)
margin = 40

#Page1
pointSize = 50
leading = .3

#Page2
pointSize_2 = 160
tracking_2 = 15
#Page3
gutter = 15

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#-------------
#Calculations
#-------------

f = CurrentFont()
f.testInstall(showProgress=False)
fname = (f.info.familyName + '-' + f.info.styleName).replace(' ', '')
font(fname)
fallbackFont('LastResort')
pageDimentions =  (width(), height())
x, y, w, h = margin, margin+25 , pageDimentions[0] - 2*margin, pageDimentions[1] - 2*margin-25
# #Debug rect------
# fill(.9,.9,.9)
# rect(x, y, w, h)
# fill(0)
# #----------------

def letterChecker(group):
    availableGlyphs = []
    for g in f:
        if g.name in group:
            availableGlyphs += g.name
    availableGlyphs.sort()
    return availableGlyphs

availableLowercase = letterChecker(lowercase)
availableUppercase = letterChecker(uppercase)

#-------
#Footer
#-------

def drawFooter(pageNumber,totalPages):
    x, y, w, h = margin, margin-10, pageDimentions[0]-2*margin, 30
    # #Debug rect------
    # fill(1,.9,.9)
    # rect(x, y, w, h)
    # fill(0)
    # #-----------------
    txt = FormattedString()
    txt.append(fname + '\n', font='InputMono-Bold')
    txt.append(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")+ ' ', font='InputMono-Regular')
    txt.append('p. ' + str(pageNumber) + '/' + str(totalPages), font='InputMono-Regular')
    textBox(txt, (x, y, w, h))

#------------
#Draw Page 1
#------------

drawFooter(1,2)

#----Page 1 Settings----

x1, y1, w1, h1 = x, y, w, h
letters = availableLowercase

def setLine(letters, bread, pointSize,leading, box):
    fontSize(pointSize)
    scale = pointSize / f.info.unitsPerEm 
    breadWidth = f[bread].width * scale
    x, y, w, h = box
    
    #Calculate what fits in box
    while letters:
        lineText = bread
        lineLength = breadWidth
        for letter in letters:
            lineLength += (f[letter].width * scale) + breadWidth
            if lineLength <= w:
                lineText += (f[letter].name + bread)
                letters = letters[1:]
                
        #Draw line
        textBox(lineText, (x, y, w, h))    
        
        #Substract 1 line height from original box
        h = h - 1000 * scale * (1+leading)
    return h
        #Debug Rect------
        # fill(0,0,0,.1)
        # rect(x, y, w, h)
        # fill(0)
        #----------------

#Check if control characters are present. If so, create sandwich string.
if "n" in f.keys():
    h1 = setLine(letters, "n", pointSize, leading, (x1, y1, w1, h1))
else: print("Control character 'n' not available")

if "o" in f.keys():
    h1 = setLine(letters, "o", pointSize, leading, (x1, y1, w1, h1))
else: print("Control character 'o' not available")

if "H" in f.keys():
    h1 = setLine(letters, "H", pointSize, leading, (x1, y1, w1, h1))
else: print("Control character 'H' not available")

if "O" in f.keys():
    h1 = setLine(letters, "O", pointSize, leading, (x1, y1, w1, h1))
else: print("Control character 'O' not available")    

#********************PAGE 2**************************

newPage(*pageDimentions)
drawFooter(2,2)
font(fname)
tracking(tracking_2)
fontSize(pointSize_2)
if availableLowercase or availableUppercase:
    az = ''
    textBox(az.join(availableUppercase + availableLowercase), (x, y, w, h)) 
#**availableUppercase ****availableUppercase **************PAGE 3**************************

# newPage(*pageDimentions)
# drawFooter(2,2)

# x2, y2, w2, h2 = x, y, w, h

# words = 800
# txt = ""
# def random_word(a,b):
#     key = ''
#     length = choice(range(a,b))
#     for i in range(length):
#         key += choice(letters)
#     key += ' '
#     return key
        

# for n in range(words):
#     txt += random_word(4,10)

# hyphenation(False)
# font(fname)
# fontSize(12)
# lineHeight(15)
# columnwidth = (w-2 * gutter) / 3

# textBox(txt, (x, y, columnwidth, h2))
# fontSize(9)
# lineHeight(11)

# textBox(txt, ((margin + columnwidth + gutter), margin, columnwidth, (height()-2*margin)))
# fontSize(6)
# lineHeight(9)

# textBox(txt, ((margin + 2*columnwidth + 2*gutter), margin, columnwidth, (height()-2*margin)))


#********************PAGE 2**************************

# newPage("A4Landscape")
# font(fname)
# fontSize(100)
# upperText = ''.join(upper)[:6]
# w, _ = textSize(upperText)
# text(upperText,(margin, height()*.7))
# text("Hello",(margin + w, height()*.7))

# text(''.join(lower),(margin, height()*.5))

#----Save PFD----
date = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
saveImage('~/Desktop/RFProof_' + date + '.pdf')
