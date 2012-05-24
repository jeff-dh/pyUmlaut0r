#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import QApplication, QClipboard, QSystemTrayIcon, QMenu, QAction, QIcon
import sys

import ctypes
#register the process id as 'pyUmlaut0r'
libc = ctypes.cdll.LoadLibrary('libc.so.6')
libc.prctl(15, 'pyUmlaut0r', 0, 0, 0)

def toClipboard(s):
  QApplication.clipboard().setText(s)
  QApplication.clipboard().setText(s, QClipboard.Selection)

def createMenu():
  def createAction(s):
    action = QAction(s, trayMenu)
    action.triggered.connect(lambda: toClipboard(s))
    return action

  trayMenu = QMenu()
  umlaute = [u"ä", u"ö", u"ü", u"Ä", u"Ö", u"Ü", u"ß"]

  for u in umlaute:
    trayMenu.addAction(createAction(u))

  return trayMenu

app = QApplication(sys.argv)

trayIcon = QSystemTrayIcon()
trayIcon.setIcon(QIcon("umlautIcon.png"))
trayIcon.setContextMenu(createMenu())
trayIcon.show()

app.exec_()
