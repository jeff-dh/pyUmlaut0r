# -*- coding: utf-8 -*-
from PyQt4.QtGui import QMenu, QAction, QClipboard, QApplication

def createMenu():
  def createAction(s):
    action = QAction(s, trayMenu)
    action.triggered.connect(lambda: toClipboard(s))
    return action

  trayMenu = QMenu()
  umlaute = [u"ä", u"ö", u"ü", u"ß", u"Ä", u"Ö", u"Ü"]

  for u in umlaute:
    trayMenu.addAction(createAction(u))

  return trayMenu

def toClipboard(s):
  QApplication.clipboard().setText(s)
  QApplication.clipboard().setText(s, QClipboard.Selection)

def setProcessName(name):
  import ctypes
  libc = ctypes.cdll.LoadLibrary('libc.so.6')
  libc.prctl(15, name, 0, 0, 0)

