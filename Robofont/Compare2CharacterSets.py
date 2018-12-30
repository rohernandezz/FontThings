#RoboFont script to compare character sets of one UFO to another “master” UFO
#Updated for Py 3 from Nina Stoessinger's original @ https://gist.github.com/ninastoessinger/c8eb9d0938584a277f90

from mojo.UI import SelectFont

markCounterpartsOfMissing = (1, 0, 0, 1)
# mark color for glyphs missing in the other font
# set to None for none, otherwise (r, g, b, a) tuple

f1 = SelectFont("Select 'Master' font:")
f2 = SelectFont("Select font to compare:")

if f1 is not None and f2 is not None:
    missing = []
    for glyph in f1:
        try:
            otherGlyph = f2[glyph.name]
        except:
            missing.append(glyph.name)
        
    print("{} misses the following glyphs compared to {}:".format(f2, f1))
    missing = sorted(missing)
    for m in missing:
        print(m)
        if markCounterpartsOfMissing is not None:
            f1[m].mark = markCounterpartsOfMissing
    
else:
    print("aborted")