from mojo.events import addObserver, removeObserver
from vanilla import *

class RhinoFont(object):
 
    def __init__(self):
        
        #----WINDOW SHIT----------------------------------------------------------
        self.w = FloatingWindow((123, 70), "RhinoFont")
        # Layout Variables
        x, y = 10, 10
        padding = 10
        height = 20

        self.w.closeButton = Button(
            (x, y, - padding, height), "close", callback=self.closeCallback)
            
        y += height + padding

        self.w.testText =TextBox((x, y, -padding, height), "Dummy text")
        
        self.w.open()
        #----WINDOW SHIT----------------------------------------------------------
 
        self.glyph = CurrentGlyph()
        self.glyph.addObserver(self, "selectionCallback", "Glyph.SelectionChanged")
        print("Added Observer")    
        
        
    def closeCallback(self, sender):
        self.glyph.removeObserver(self, "selectionCallback")
        print("Removed Observer") 
        self.w.close()
    
    def getImplicitSelectedPoints(self):
        pts = []
        for contour in self.glyph.contours:
            for i, segment in enumerate(contour.segments):
                for pt in segment:
                    if not pt.selected:
                        continue
                    pts.append(pt)
                    # implicit == include BCPs in selection
                    if pt.type != 'offcurve':
                        # bcpIn
                        if len(segment) == 3:
                            bcpIn = segment[-2]
                            pts.append(bcpIn)
                        # bcpOut
                        try:
                            nextSegment = contour[i + 1]
                        except IndexError:
                            nextSegment = contour[0]
                        if len(nextSegment) == 3:
                            bcpOut = nextSegment[0]
                            pts.append(bcpOut)
        return pts #List of Rpoints

    def selectionCallback(self, notification):
        self.selectedPoints = self.getImplicitSelectedPoints()
        print(self.selectedPoints)
        
RhinoFont()


