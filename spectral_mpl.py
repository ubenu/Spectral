# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:43:23 2016

@author: Maria Schilstra
"""
#from PyQt5 import QtGui as gui
from PyQt5 import QtCore as qt
from PyQt5 import QtWidgets as widgets


from matplotlib.figure import Figure
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,
                                                NavigationToolbar2QT)


class MplCanvas(FigureCanvas):
    """ 
    Class representing the FigureCanvas widget to be embedded in the GUI
    For simplicity, MplCanvas objects are driven via the UI
    """

    def __init__(self, parent):
        self.fig = Figure()
        
        self.gs = gridspec.GridSpec(10, 1) 
        self.gs.update(left=0.1, right=0.95, top=0.95, bottom=0.1, hspace=1.5)
        self.main_plot = self.fig.add_subplot(self.gs[:,:])
                
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, 
                widgets.QSizePolicy.Expanding, widgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self) 
        self.curves = {}
       
        
class NavigationToolbar(NavigationToolbar2QT):
                        
    def __init__(self, canvas_, parent_):
#        self.toolitems = (
#            ('Home', 'Reset original view', 'mjs-home', 'home'),
#            (None, None, None, None), # this is a separator
#            ('Zoom', 'Zoom in to rectangle', 'mjs-zoom-to-rect', 'zoom'),
#            ('Pan', 'Pan axes with left mouse, zoom with rigvoltage', 'mjs-pan', 'pan'),
#            (None, None, None, None),
#            ('Save', 'Save plot (graphics format)', 'mjs-save', 'save_figure'),
#            )
        self.toolitems = tuple([t for t in NavigationToolbar2QT.toolitems if
                 t[0] in ('Home', 'Back', 'Forward', 'Pan', 'Zoom', 'Save')])
        NavigationToolbar2QT.__init__(self,canvas_,parent_)  
        
#    def _init_toolbar(self):
#        # Reimplemented to 1) get rid of edit_curves, and 
#        # 2) get better control over icons
#    
#        self.basedir = ".\\Resources\\"
#                        
#        for text, tooltip_text, image_file, callback in self.toolitems:
#            if text is None:
#                self.addSeparator()
#            else:
#                a = self.addAction(self._icon(image_file + '.png'),
#                                         text, getattr(self, callback))
#                self._actions[callback] = a
#                if callback in ['zoom', 'pan']:
#                    a.setCheckable(True)
#                if tooltip_text is not None:
#                    a.setToolTip(tooltip_text)
#                    
#        figureoptions = None # Added to get rid of curve editor
#        if figureoptions is not None:
#            a = self.addAction(self._icon("qt4_editor_options.png"),
#                               'Customize', self.edit_parameters)
#            a.setToolTip('Edit curves line and axes parameters')
#
#        self.buttons = {}
#
#        # Add the x,y location widget at the right side of the toolbar
#        # The stretch factor is 1 which means any resizing of the toolbar
#        # will resize this label instead of the buttons.
#        if self.coordinates:
#            self.locLabel = widgets.QLabel("", self)
#            self.locLabel.setAlignment(
#                    qt.Qt.AlignRight | qt.Qt.AlignTop)
#            self.locLabel.setSizePolicy(
#                widgets.QSizePolicy(widgets.QSizePolicy.Expanding,
#                                  widgets.QSizePolicy.Ignored))
#            labelAction = self.addWidget(self.locLabel)
#            labelAction.setVisible(True)

        # reference holder for subplots_adjust window
#        self.adj_window = None
        
    def switch_off_pan_zoom(self):
        if self._active == "PAN":
            self.pan()
        elif self._active == "ZOOM":
            self.zoom()
