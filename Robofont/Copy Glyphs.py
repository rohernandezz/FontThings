from mojo.UI import SelectFont, AskString

markColor = (1,0,0,1) #(R,G,B,A)

def getFontsNGlyphs():
    source = SelectFont("Select origin font:", "Copy glyphs")
    destination = SelectFont("Select destination font:", "Copy glyphs")

    if CurrentFont().selection:
        copySet = CurrentFont().selection
    else:
        copySet = AskString("Enter glyph names:").split()
        if not copySet:
            print("☹️ No glyphs selected!")
    return[source, destination, copySet]

def getFontName(font):
    if font.info.familyName != None:
        fn = font.info.familyName
    else:
        fn = "*No Name*"
    if font.info.styleName != None:
        fs = font.info.styleName
    else:
        fs = "*No Style*"
    return(fn+" "+fs)

def printReport(copied, notFound, source, destination):
    if copied:
        print(f"🎉 Glyphs \"{', '.join(copied)}\" copied to font \"{getFontName(destination)}\".")
    if notFound:
        print(f"😔 Glyphs \"{', '.join(notFound)}\" not found in font \"{getFontName(source)}\" so they weren't copied.")

def copyGlyphs(source, destination, copySet):
    notFound, copied = [], []
    for glyph in copySet:
        if glyph not in source.keys():
            notFound.append(glyph)
        else:
            destination.insertGlyph(source[glyph], name=glyph)
            destination[glyph].mark = markColor
            copied.append(glyph)
    printReport(copied, notFound, source, destination)

# print(*getFonts())
copyGlyphs(*getFontsNGlyphs())