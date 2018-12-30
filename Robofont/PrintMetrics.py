printVerticalMetrics = False

f = CurrentFont()

fontName = str(f.info.familyName) + " " + str(f.info.styleName)

print("")
print(fontName)
print("-"*len(fontName))

if printVerticalMetrics == True:
	print("Descender:", f.info.descender)
	print("x-height:", f.info.xHeight)
	print("Ascender:", f.info.ascender)
	print("****")

print("HheaAscender:", f.info.openTypeHheaAscender)
print("HheaDescender:", f.info.openTypeHheaDescender)
print("HheaLineGap:", f.info.openTypeHheaLineGap)
print("****")
print("OS2WinAscent:", f.info.openTypeOS2WinAscent)
print("OS2WinDescent:", f.info.openTypeOS2WinDescent)
print("****")
print("OS2TypoAscender:", f.info.openTypeOS2TypoAscender)
print("OS2TypoDescender:", f.info.openTypeOS2TypoDescender)
print("OS2TypoLineGap:", f.info.openTypeOS2TypoLineGap)
