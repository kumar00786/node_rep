# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 22:51:59 2023

@author: Kumar.Gautam
"""
from PyQt5.QtWidgets import *

class NodeEditorWnd(QWidget):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        
        
        self.initUI()
        
    
    def initUI(self):
        
        self.setGeometry(200,200,800,600)
        
        self.setWindowTitle("Node Editor")
        self.show()