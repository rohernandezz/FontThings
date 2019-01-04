#Replaces current Glyph with a /? wildcard in the current space center
from mojo.UI import *

exceptions = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
g =  CurrentGlyph()
g = str(g.name)
if g in exceptions:
    g = exceptions[g]

sc = CurrentSpaceCenter()
text = sc.getRaw()
new_text = text.replace(g, "/?")
sc.setRaw(new_text)



