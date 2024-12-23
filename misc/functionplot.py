"""functionplot.py

I wrote this disgusting code quite some time ago. It implements an
interactice function plotter that redraws the functions on any view
range. It most likely has a lot of bad and inefficient programming
habits (plus not a lot of comments), but i'll keep it here as
reference just in case.

cenfra
"""


import wx
import numpy as np
from random import randint
import ast


def dip1(size):
    return wx.ScreenDC().FromDIP( wx.Size( size, size ) )[0]
def dip2(width_dip, height_dip):
    return wx.Size( wx.ScreenDC().FromDIP( wx.Size( width_dip, height_dip ) ) )

def getTextCoordsCenter(dc, text, x, y):
    # x and y are the coordinates where the text will be centered
    # the dc is necessary to check the dimensions of the text using current font
    textWidth, textHeight = dc.GetTextExtent(text)
    textCoordX = x - textWidth // 2
    textCoordY = y - textHeight // 2
    return textCoordX, textCoordY


def safe_eval(expr, allowed_names):

    tree = ast.parse(expr, mode='eval')

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.For, ast.While, ast.If, ast.FunctionDef, ast.ClassDef, ast.Lambda)):
            raise ValueError("only mathematical expressions are allowed")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id not in allowed_names:
            raise ValueError(f"\"{node.func.id}\" is not allowed.")
    return eval(expr, {"__builtins__": {}}, allowed_names)


class pyGraph2D(wx.Panel):

    def __init__(self, 
        axesType="centered", # centered or rectangular
        yFunctions:list=[],  # list of strings. only variable is x
        displayXRange=None,  # tuple of range
        displayYRange=None,  # tuple of range
        graphTitle:str="",
        graphLabelX:str="",
        graphLabelY:str="",
        graphPlotColors:list=[],       # (R, G, B)
        graphPlotLineStyles:list=[],   # "solid", "dashed", "dotted", "dotdashed"
        graphPlotLineWidth:list=[],    # list of integers
        graphLegend:list=[],           # list of strings
        equalAxes:bool=False,     # makes y axis range the same as x's
        axesSquare:bool=False,    # makes the axes the same size regardless of their range
        showGrid:bool=False,
        showTicks:bool=True,
        showNumbers:bool=True,
        showLegend:bool=False,
        outerColor:tuple=(220, 220, 220),   # RGB color for outer rectangles
        innerColor:tuple=(220, 220, 220),   # RGB color for plotting area
        windowSize=None,                    # panel will lock to size if one is specified
        *args, **kwargs):
    
        super().__init__(*args, **kwargs)

        # graph attributes
        
        self.axesType = axesType

        self.graphTitle = graphTitle
        self.displayXRange = displayXRange
        self.displayYRange = displayYRange
        self.graphLabelX = graphLabelX
        self.graphLabelY = graphLabelY
        
        self.yFunctions = yFunctions
        
        # unused for now
        self.xValues = [  ]
        self.yValues = [  ]
        
        self.graphPlotColors = graphPlotColors
        self.graphPlotLineStyles = graphPlotLineStyles
        self.graphPlotLineWidth = graphPlotLineWidth
        self.graphLegend = graphLegend
        
        self.equalAxes = equalAxes
        self.axesSquare = axesSquare
        
        self.showGrid = showGrid
        self.showTicks = showTicks
        self.showNumbers = showNumbers
        self.showLegend = showLegend
        
        self.outerColor = outerColor
        self.innerColor = innerColor
        
        self.windowSize = windowSize
        
        
        # static styles
        self.titleFont = wx.Font(17, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.labelFont = wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.numbersFont = wx.Font(8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.penLegend = wx.Pen(wx.BLACK, 2, wx.PENSTYLE_SOLID)
        self.brushLegend = wx.Brush(wx.WHITE, wx.BRUSHSTYLE_SOLID)
        self.tickSize = 7
        self.plotLineStyles = {"solid": wx.PENSTYLE_SOLID,
                               "dashed": wx.PENSTYLE_LONG_DASH,
                               "dotted": wx.PENSTYLE_DOT,
                               "dotdash": wx.PENSTYLE_DOT_DASH}
       
        # if there are less values than functions defined
        self.handleMissingValues()

        # set up plot range if displayXRange and displayYRange are not set
        if (self.displayXRange is None) or (self.displayYRange is None):
            self.updateDisplayRangeAutomatic()
            
        # update attributes and paint
        self.UpdateAttributes()
        self.init_ui()
        

    def init_ui(self):
        
        # set panel size
        #self.SetMinClientSize(self.panelSize)
        #self.SetMaxClientSize(self.panelSize)

        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)
        
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
        

        self.movingGraph = False
        self.zoomingGraph = False
        self.isDragging = False


    def handleMissingValues(self):
        
        # fill missing values if there are less than function amount
        
        functionsLength = len(self.yFunctions)
        
        if (len(self.graphPlotColors) < functionsLength):
            amountOfMissingValues = functionsLength - len(self.graphPlotColors)
            for i in range(amountOfMissingValues):
                self.graphPlotColors.append( ( randint(60, 200) , randint(60, 200) , randint(60, 200) ) )
        
        if (len(self.graphPlotLineStyles) < functionsLength): 
            amountOfMissingValues = functionsLength - len(self.graphPlotLineStyles)
            for i in range(amountOfMissingValues):
                self.graphPlotLineStyles.append("solid")
            
        if (len(self.graphPlotLineWidth) < functionsLength):
            amountOfMissingValues = functionsLength - len(self.graphPlotLineWidth)
            for i in range(amountOfMissingValues):
                self.graphPlotLineWidth.append(2)
            
        if (len(self.graphLegend) < functionsLength):
            amountOfMissingValues = functionsLength - len(self.graphLegend)
            initialLegendAmount = len(self.graphLegend)
            for i in range(amountOfMissingValues):
                self.graphLegend.append(self.yFunctions[i+initialLegendAmount]) # add offset if items were already defined


    def OnLeftDown(self, event):
        self.movingGraph = True
        self.startingPos = event.GetPosition()
        self.CaptureMouse()
        

    def OnLeftUp(self, event):
        self.movingGraph = False
        if self.HasCapture():
            self.ReleaseMouse()


    def OnRightDown(self, event):
        self.zoomingGraph = True
        self.startingPos = event.GetPosition()
        self.CaptureMouse()
        
        
    def OnRightUp(self, event):
        self.zoomingGraph = False
        if self.HasCapture():
            self.ReleaseMouse()

            
    def OnMouseMove(self, event):
        
        # left click
        if self.movingGraph and event.Dragging() and event.LeftIsDown():
            currentPos = event.GetPosition()
            
            # calculate the scaled shift based on the current range
            xScale = (self.displayXRange[1] - self.displayXRange[0]) * 0.0015
            yScale = (self.displayYRange[1] - self.displayYRange[0]) * 0.0015
            
            xDiff = self.startingPos[0] - currentPos[0]
            yDiff = self.startingPos[1] - currentPos[1]

            # apply the shift using the scaled values
            self.displayXRange = (
                self.displayXRange[0] + xScale * xDiff,
                self.displayXRange[1] + xScale * xDiff,
            )
            self.displayYRange = (
                self.displayYRange[0] + yScale * -yDiff,
                self.displayYRange[1] + yScale * -yDiff,
            )

            self.xAxisCoords1[1] += int(yScale * -yDiff)
            self.xAxisCoords2[1] += int(yScale * -yDiff)

            self.startingPos = currentPos
            self.Refresh()

        # right click
        if self.zoomingGraph and event.Dragging() and event.RightIsDown():
            
            currentPos = event.GetPosition()

            xDiff = self.startingPos[0] - currentPos[0]
            yDiff = self.startingPos[1] - currentPos[1]


            #n = 0.03
            #scaleIn = 1 - n
            #scaleOut = 1 + n

            n = 0.005
            scaleIn = 1 - (yDiff * n)
            scaleOut = 1 - (yDiff * n)
            

            # calculate center of the view
            xCenter = (self.displayXRange[0] + self.displayXRange[1]) / 2
            yCenter = (self.displayYRange[0] + self.displayYRange[1]) / 2
          

            if yDiff > 0:
                self.displayXRange = (
                    xCenter + (self.displayXRange[0] - xCenter) * scaleIn,
                    xCenter + (self.displayXRange[1] - xCenter) * scaleIn,
                )
                self.displayYRange = (
                    yCenter + (self.displayYRange[0] - yCenter) * scaleIn,
                    yCenter + (self.displayYRange[1] - yCenter) * scaleIn,
                )
            elif yDiff < 0:
                self.displayXRange = (
                    xCenter + (self.displayXRange[0] - xCenter) * scaleOut,
                    xCenter + (self.displayXRange[1] - xCenter) * scaleOut,
                )
                self.displayYRange = (
                    yCenter + (self.displayYRange[0] - yCenter) * scaleOut,
                    yCenter + (self.displayYRange[1] - yCenter) * scaleOut,
                )

            self.startingPos = currentPos
            self.Refresh()
            
 
    def updateDisplayRangeAutomatic(self):
        
        # default range
        self.defaultRangeX = (-10, 10)
        self.defaultRangeY = (-10, 10)
        
        # find min and max in all x sets
        currentMinX = 0
        currentMaxX = 0
        for xSet in self.xValues:
            setMin = min(xSet)
            setMax = max(xSet)
            if (setMin < currentMinX):
                currentMinX = setMin
            if (setMax > currentMaxX):
                currentMaxX = setMax
        currentMinX = currentMinX if (currentMinX != 0) else self.defaultRangeX[0]
        currentMaxX = currentMaxX if (currentMaxX != 0) else self.defaultRangeX[1]
        self.displayXRange = (currentMinX, currentMaxX)

        # find min and max in all y sets
        currentMinY = 0
        currentMaxY = 0
        for ySet in self.yValues:
            setMin = min(ySet)
            setMax = max(ySet)
            if (setMin < currentMinY):
                currentMinY = setMin
            if (setMax > currentMaxY):
                currentMaxY = setMax
        currentMinY = currentMinY if (currentMinY != 0) else self.defaultRangeY[0]
        currentMaxY = currentMaxY if (currentMaxY != 0) else self.defaultRangeY[1]
        self.displayYRange = (currentMinY, currentMaxY)
        
        
        if (self.axesType == "centered"):
            # find max of x axis and max of y axis. then, use this value to make the 0 stay at the center of the graph
            maxX = max(abs(self.displayXRange[0]), abs(self.displayXRange[1]))
            maxY = max(abs(self.displayYRange[0]), abs(self.displayYRange[1]))
            self.displayXRange = (-maxX, maxX)
            self.displayYRange = (-maxY, maxY)
            
        if self.equalAxes:
            self.displayYRange = self.displayXRange


    def paintDrawPlot(self, dc):
        
        # draw initial rectangle (might be able to fix by setting background color to inner color)
        dc.SetPen(self.penInnerColor)
        dc.SetBrush(self.brushInnerColor)
        dc.DrawRectangle(0, 0, self.panelWidth, self.panelHeight)
        
        # scale and shift, equivalent to mat transf. applied to all points (even axes!)
        scaleX = self.workingAreaWidth / (self.displayXRange[1] - self.displayXRange[0])
        scaleY = -self.workingAreaHeight / (self.displayYRange[1] - self.displayYRange[0]) # minus because mirrored
        shiftX = self.waLeft - (self.displayXRange[0] * scaleX)
        shiftY = self.waTop - (self.displayYRange[1] * scaleY)  
        
        # --------------------- plot sets of points
        
        for i in range(len(self.xValues)): # for each set of points
            
            # set pen with plot color properties
            plotColorPen = wx.Pen(colour=wx.Colour(*self.graphPlotColors[i]),
                                  width=self.graphPlotLineWidth[i],
                                  style=self.plotLineStyles[self.graphPlotLineStyles[i]])
            dc.SetPen(plotColorPen)

            # for each pair of points
            for j in range(len(self.xValues[i])):

                # get transformed point
                x = (scaleX * self.xValues[i][j]) + shiftX
                y = (scaleY * self.yValues[i][j]) + shiftY

                # check if there is a next point
                if (j == len(self.xValues[i])-1):
                    break
            
                # get next transformed point
                xp1 = (self.xValues[i][j+1] * scaleX) + shiftX
                yp1 = (self.yValues[i][j+1] * scaleY) + shiftY
                
                # join points
                dc.DrawLine(int(x), int(y), int(xp1), int(yp1))
                
        # --------------------- plot functions
        
        # create x linspace
        step = int((self.displayXRange[1] - self.displayXRange[0]) / 0.5)
        # lock step range
        if (step < 30):
            step = 30
        elif (step > 600):
            step = 600
        x = np.linspace(self.displayXRange[0], self.displayXRange[1], step)
        
        allowed_names = {
            'cos': np.cos,
            'sin': np.sin,
            'sqrt': np.sqrt,
            'log10': np.log10,
            'x': x
        }
        
        for i in range(len(self.yFunctions)):
            
            # set pen with plot color properties
            plotColorPen = wx.Pen(colour=wx.Colour(*self.graphPlotColors[i]),
                                  width=self.graphPlotLineWidth[i],
                                  style=self.plotLineStyles[self.graphPlotLineStyles[i]])
            dc.SetPen(plotColorPen)
            
            
            # calculate y values
            try:
                yValues = safe_eval(self.yFunctions[i], allowed_names)
            except ValueError as e:
                print(f"Error: {e}")
                continue
            
            for j in range(len(x)):
                
                # get transformed point
                xVal = (scaleX * x[j]) + shiftX
                yVal = (scaleY * yValues[j]) + shiftY

                # check if there is a next point
                if (j == len(x)-1):
                    break
            
                # get next transformed point
                xp1 = (x[j+1] * scaleX) + shiftX
                yp1 = (yValues[j+1] * scaleY) + shiftY
                
                # join points
                dc.DrawLine(int(xVal), int(yVal), int(xp1), int(yp1))
            


        # calculations for ticks and grid
        xAxisP1 = [self.displayXRange[0], 0]
        xAxisP2 = [self.displayXRange[1], 0]
        yAxisP1 = [0, self.displayYRange[1]]
        yAxisP2 = [0, self.displayYRange[0]]
        zeroPoint = [int(shiftX), int(shiftY)]
        # convert x axis coords
        Xx1 = (xAxisP1[0] * scaleX) + shiftX
        Xy1 = (xAxisP1[1] * scaleY) + shiftY
        Xx2 = (xAxisP2[0] * scaleX) + shiftX
        Xy2 = (xAxisP2[1] * scaleY) + shiftY
        # convert y axis coords
        Yx1 = (yAxisP1[0] * scaleX) + shiftX
        Yy1 = (yAxisP1[1] * scaleY) + shiftY
        Yx2 = (yAxisP2[0] * scaleX) + shiftX
        Yy2 = (yAxisP2[1] * scaleY) + shiftY
        
 
        # draw axes
        
        if (self.axesType == "centered"):
            # set styles
            dc.SetPen(self.penAxis)
            dc.SetBrush(wx.TRANSPARENT_BRUSH)
            # draw axes
            dc.DrawLine(int(Xx1), int(Xy1), int(Xx2), int(Xy2)) # x axis
            dc.DrawLine(int(Yx1), int(Yy1), int(Yx2), int(Yy2)) # y axis
            # draw axis labels
            dc.SetFont(self.labelFont)
            dc.DrawText(self.graphLabelX, int(Xx1+10), int(Xy1)) # x axis
            dc.DrawRotatedText(self.graphLabelY, int(Yx1), int(Yy2-10), 90) # y axis
        elif (self.axesType == "rectangular"):
            # set styles
            dc.SetPen(self.penAxis)
            dc.SetBrush(wx.TRANSPARENT_BRUSH)
            # draw axes rectangle
            dc.DrawRectangle(self.waLeft, self.waTop, self.workingAreaWidth, self.workingAreaHeight)
            
            
        # draw ticks or grid
        
        if (self.showTicks or self.showGrid):
            
            gridLinesFactor = 5 # ?????
            
            # for x range
            gridRangeX = self.displayXRange[1] - self.displayXRange[0]
            gridRangeX = gridRangeX * gridLinesFactor
            # for y range
            gridRangeY = self.displayYRange[1] - self.displayYRange[0]
            gridRangeY = gridRangeY * gridLinesFactor
            
            
            # functions
            
            def calculate_step_size(gridRange):
                base_step = 1
                exponent = int(np.log10(gridRange)) - 1
                step_size = base_step * (10 ** exponent) 
                return step_size
                
            def roundToClosestStep(n):
                return round( round(n / stepInside) * stepInside , 2)


            # ----------------------- x axis elements
            
            stepInside = calculate_step_size(gridRangeX)

            # set initial value
            gridTickX = roundToClosestStep(self.displayXRange[0])
            
            while (gridTickX <= self.displayXRange[1]):

                # draw or not the 0
                if (gridTickX == 0) and (self.axesType == "centered"):
                    gridTickX += stepInside
                    continue
                    
                # calculations

                if (self.axesType == "centered"):
                    x = (gridTickX * scaleX) + shiftX
                    y = shiftY
                elif (self.axesType == "rectangular"):
                    x = (gridTickX * scaleX) + shiftX
                    y = self.waBottom
                    
                # draw corresponding elements
                
                if self.showGrid:
                    dc.SetPen(wx.Pen(wx.Colour(170, 170, 170), 1, wx.PENSTYLE_LONG_DASH))
                    dc.SetBrush(wx.TRANSPARENT_BRUSH)
                    dc.DrawLine(int(x), int(Yy1), int(x), int(Yy2))
                    
                if self.showTicks:
                    dc.SetPen(wx.Pen(wx.BLACK, 2, wx.PENSTYLE_SOLID))
                    dc.SetBrush(wx.Brush(wx.BLACK, wx.BRUSHSTYLE_SOLID))
                    dc.DrawLine(int(x), int(y-self.tickSize), int(x), int(y+self.tickSize))
                
                if self.showNumbers:
                    text = str(round(gridTickX, 2))
                    if (self.axesType == "centered"):
                        numberX, numberY = getTextCoordsCenter(dc, text, int(x), int(Xy1+self.tickSize+14))
                    elif (self.axesType == "rectangular"):
                        numberX, numberY = getTextCoordsCenter(dc, text, int(x), int(y-self.tickSize-14))
                    dc.SetFont(self.numbersFont)
                    dc.DrawText(text, numberX, numberY)

                gridTickX += stepInside


            # ----------------------- y axis elements
            
            stepInside = calculate_step_size(gridRangeY)

            # set initial value
            gridTickY = roundToClosestStep(self.displayYRange[0])
            
            while (gridTickY <= self.displayYRange[1]):

                # draw or not the 0
                if (gridTickY == 0) and (self.axesType == "centered"):
                    gridTickY += stepInside
                    continue
                    
                # calculations

                if (self.axesType == "centered"):
                    x = shiftX
                    y = gridTickY * scaleY + shiftY
                elif (self.axesType == "rectangular"):
                    x = self.waLeft
                    y = gridTickY * scaleY + shiftY

                # draw corresponding elements 
                
                if self.showGrid:
                    dc.SetPen(wx.Pen(wx.Colour(170, 170, 170), 1, wx.PENSTYLE_LONG_DASH))
                    dc.SetBrush(wx.TRANSPARENT_BRUSH)
                    dc.DrawLine(int(Xx1), int(y), int(Xx2), int(y))
                
                if self.showTicks:
                    dc.SetPen(wx.Pen(wx.BLACK, 2, wx.PENSTYLE_SOLID))
                    dc.SetBrush(wx.Brush(wx.BLACK, wx.BRUSHSTYLE_SOLID))
                    dc.DrawLine(int(x-self.tickSize), int(y), int(x+self.tickSize), int(y))
                
                if self.showNumbers:
                    text = str(round(gridTickY, 2))       
                    textWidth, textHeight = dc.GetTextExtent(text)
                    if (self.axesType == "centered"):
                        numberX = int(x-self.tickSize-textWidth-3)
                        numberY = int(y-(textHeight//2))
                    elif (self.axesType == "rectangular"):                    
                        numberX = int(x+self.tickSize+3)
                        numberY = int(y-(textHeight//2))
                    dc.SetFont(self.numbersFont)
                    dc.DrawText(text, numberX, numberY)

                gridTickY += stepInside
                
                    
        # draw rectangles to give illusion of clipping
        dc.SetPen(self.penOuterColor)
        dc.SetBrush(self.brushOuterColor)
        dc.DrawRectangle(0, 0, self.panelWidth, self.waTop)                   # top side
        dc.DrawRectangle(0, 0, self.waLeft, self.panelHeight)                 # left side
        dc.DrawRectangle(0, self.waBottom, self.panelWidth, self.panelHeight) # bottom side
        dc.DrawRectangle(self.waRight, 0, self.panelWidth, self.panelHeight)  # right side
        
        # add rectangular labels
        if (self.axesType == "rectangular") and (self.graphLabelX != "" or self.graphLabelY != ""):
            
            # set label font
            dc.SetFont(self.labelFont)
            # draw x label
            textTitleCoordCenterX = self.panelWidth // 2
            textTitleCoordCenterY = self.panelHeight - self.marginBottom // 2
            textTitleX, textTitleY = getTextCoordsCenter(dc, self.graphLabelX, textTitleCoordCenterX, textTitleCoordCenterY)
            dc.DrawText(self.graphLabelX, textTitleX, textTitleY)
            # draw y label
            textCenterX = self.waLeft // 2
            textCenterY = self.panelHeight // 2
            textWidth, textHeight = dc.GetTextExtent(self.graphLabelY)
            textX = textCenterX - textHeight // 2
            textY = textCenterY + textWidth // 2
            dc.DrawRotatedText(self.graphLabelY, textX, textY, 90)
     
    
    def paintDrawLegend(self, dc):
        
        # draw legend
        dc.SetPen(self.penLegend)
        dc.SetBrush(self.brushLegend)
        dc.SetFont(self.labelFont)
        
        lineStyleWidth = 30
        
        # get max text width and their height with current font
        maxWidth = 0
        textHeight = 0
        for text in self.graphLegend:
            textWidth, textHeight = dc.GetTextExtent(text)
            if textWidth > maxWidth:
                maxWidth = textWidth
                
        # set legend box dimensions
        heightOffset = 10
        legendRectWidth = maxWidth + lineStyleWidth + 30
        legendRectHeight = textHeight * len(self.graphLegend) + heightOffset
        
        legendRectX = self.waRight - legendRectWidth - 10
        legendRectY = self.waBottom - legendRectHeight - 10
        
        # draw legend box
        dc.DrawRectangle(legendRectX, legendRectY, legendRectWidth, legendRectHeight)
        
        # draw legends
        currentHeight = legendRectY + (textHeight // 2) # add offset of half of the height 
        
        for i in range(len(self.graphLegend)):
            
            # set pen with plot color properties
            plotColorPen = wx.Pen(colour=wx.Colour(*self.graphPlotColors[i]),
                                  width=2,
                                  style=self.plotLineStyles[self.graphPlotLineStyles[i]])
            dc.SetPen(plotColorPen)
            
            currHeightOffset = currentHeight+heightOffset//2
            
            # draw plot style
            dc.DrawLine(legendRectX+5, currHeightOffset, legendRectX+lineStyleWidth, currHeightOffset)
            
            # draw legend
            dc.DrawText(self.graphLegend[i], legendRectX+lineStyleWidth+7, (currHeightOffset-textHeight//2))
            
            currentHeight += textHeight
     
     
    def UpdateAttributes(self):
        
        """ Graph attributes """
        
        if (self.windowSize is not None):
            self.panelWidth, self.panelHeight = dip2(self.windowSize[0], self.windowSize[1])
        else: # if size was not specified, use parent size
            try:
                self.panelWidth, self.panelHeight = self.GetParent().Size
            except:
                self.panelWidth, self.panelHeight = dip2(500, 500)

        self.panelSize = (self.panelWidth, self.panelHeight)


        # margins (percentages)
        self.marginTop = int(0.02 * self.panelHeight) if (self.graphTitle == "") else int(0.09 * self.panelHeight)
        self.marginLeft = int(0.1 * self.panelWidth) if (self.graphLabelY == "") else int(0.06 * self.panelWidth)
        self.marginRight = self.marginLeft
        self.marginBottom = int(0.08 * self.panelHeight) if (self.graphLabelX == "") else int(0.08 * self.panelHeight)

        # if centered
        if (self.axesType == "centered"):
            self.marginLeft = int(0.005 * self.panelWidth)
            self.marginRight = self.marginLeft
            self.marginBottom = self.marginLeft

        self.workingAreaHeight = self.panelHeight - self.marginTop - self.marginBottom
        
        if self.axesSquare:
            self.workingAreaWidth = self.workingAreaHeight
            self.waLeft = (self.panelWidth - self.workingAreaWidth) // 2
            self.waRight = self.panelWidth - self.waLeft
        else:
            self.workingAreaWidth = self.panelWidth - self.marginLeft - self.marginRight
            self.waLeft = self.marginLeft
            self.waRight = self.panelWidth - self.marginRight
        

        # working area coords
        self.waTop = self.marginTop
        self.waBottom = self.panelHeight - self.marginBottom



        # initial coordinates for axis

        self.xAxisCoords1 = [self.waLeft, self.panelHeight//2]
        self.xAxisCoords2 = [self.waRight, self.panelHeight//2]
        self.yAxisCoords1 = [self.panelWidth//2, self.waTop]
        self.yAxisCoords2 = [self.panelWidth//2, self.waBottom]
            


        # dynamic styles 
        
        # pens
        self.penInnerColor = wx.Pen(self.innerColor, 2, wx.PENSTYLE_SOLID)
        self.penOuterColor = wx.Pen(self.outerColor, 2, wx.PENSTYLE_SOLID)
        self.penAxis = wx.Pen(wx.BLACK, 2, wx.PENSTYLE_SOLID)
        
        # brushes
        self.brushInnerColor = wx.Brush(wx.Colour(*self.innerColor), wx.BRUSHSTYLE_SOLID)
        self.brushOuterColor = wx.Brush(wx.Colour(*self.outerColor), wx.BRUSHSTYLE_SOLID)
        

    def Update(self, event=None):
        self.OnPaint(None)
     
     
    def OnPaint(self, event):

        # update attributes
        self.UpdateAttributes()

        # create paint area
        #dc = wx.AutoBufferedPaintDC(self)
        dc = wx.BufferedPaintDC(self)
        #dc.Clear()
        dc = wx.GCDC(dc)
        dc.Clear()

        # draw plot
        self.paintDrawPlot(dc)
    
        # draw title
        if (self.graphTitle != ""):
            
            """ Draw title """
            dc.SetFont(self.titleFont)
            # title center coordinates
            textTitleCoordCenterX = self.panelWidth // 2
            textTitleCoordCenterY = self.marginTop // 2
            textTitleX, textTitleY = getTextCoordsCenter(dc, self.graphTitle, textTitleCoordCenterX, textTitleCoordCenterY)
            dc.DrawText(self.graphTitle, textTitleX, textTitleY)
            
        # draw legend
        if self.showLegend:
            self.paintDrawLegend(dc)




class FrameExample(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #self.SetMinClientSize(dip2(700, 500))
        
        self.mainPanel = wx.Panel(self)
        self.mainPanel.SetBackgroundColour(wx.BLUE)
        self.mainPanel.sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        
        self.panel = pyGraph2D(parent=self.mainPanel, yFunctions=["10*x", "sin(x)"],
                               showLegend=True, showGrid=True,
                               graphTitle="graphs",
                               graphLabelX="x label", graphLabelY="y label",
                               axesType="rectangular")
        
        
        self.mainPanel.sizer.Add(window=self.panel, proportion=1, flag=wx.EXPAND, border=0)
        

        self.mainPanel.SetSizer(self.mainPanel.sizer)
        
        
if __name__ == "__main__":
    app = wx.App()
    f = FrameExample(parent=None)
    f.Show()
    app.MainLoop()
