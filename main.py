# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 22:39:12 2023

@author: Kumar.Gautam
"""

from PyQt5.QtWidgets import *
import sys

from node_editor_wnd import NodeEditorWnd

if __name__=="__main__":
    app = QApplication(sys.argv)
    
    wnd = NodeEditorWnd()
    
    
    
    
    
    
    
    
    sys.exit(app.exec_())
    
    
"""
Useful command
!pip freeze > requirements.txt
conda list --export > requirements_conda.txt
"""    