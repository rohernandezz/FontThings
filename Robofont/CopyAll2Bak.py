### Copies the foreground in all glyphs to the background layer

font = CurrentFont()

for glyph in font:
    glyph.copyToLayer("background")
    print(str(glyph) + " contours were copied to background layer")


###RESTORE SIDEBEARINGS        
# front = font.getLayer("foreground")
# bak = font.getLayer("background")

# for g in bak:
#     if g.contours:
#         g.leftMargin = front[g.name].leftMargin
#         g.rightMargin = front[g.name].rightMargin
#         print(f"Changed {g}")