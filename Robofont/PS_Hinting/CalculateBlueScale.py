f = CurrentFont()

blueValues = f.info.postscriptBlueValues
otherBlues = f.info.postscriptOtherBlues

allBlues = otherBlues + blueValues

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

fontName = getFontName(f)

if not allBlues:
    print(f"There's no blue Values set in font '{fontName}' ☹️")
else:
    diffs = []
    for i in range(int(len(allBlues)/2)):
        diff = int(allBlues[i*2+1]) - int(allBlues[i*2])
        diffs.append(diff)

    print(f"{fontName}")
    print(f"{'-' * len(fontName)}")
    print(f"Diffs: {diffs}")
    maxZone = max(diffs)
    print(f"Max: {maxZone}")
    blueScale = 3 / (4 * maxZone)

    print(f"BlueScale: {blueScale}")