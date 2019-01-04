"""Will pop up a dialog to select a glyph and add it 
as a component to the background layer of the current glyph"""

from mojo.UI import SelectGlyph
font = CurrentFont()
glyph = SelectGlyph(font)
print(glyph)