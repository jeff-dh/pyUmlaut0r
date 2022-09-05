#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMessageBox
from PyQt5.QtGui import QIcon, QCursor
import sys
import dbus
import dbus.service
from dbus.mainloop.pyqt5 import DBusQtMainLoop

import utils
import pyUmlaut0rRes

app = QApplication(sys.argv)

#try to connect to tray icon daemon and show menu
if not sys.argv[-1] == "-d":
  try:
    utils.setProcessName("pyUmlaut0r-client")
    #connect to daemon
    bus = dbus.SessionBus()
    server = bus.get_object('org.documentroot.umlaut0r', '/umlaut0r')

    #show menu
    menu = utils.createMenu()
    action = menu.exec_(QCursor.pos())

    #send character
    server.toClipboard(action.text(), \
                       dbus_interface = 'org.documentroot.umlaut0r')

    sys.exit(0)

  except dbus.exceptions.DBusException:
    QMessageBox.critical(None, "Can't connect",
                        """Can't connect to pyUmlaut0r daemon.\nYou should first start a daemon by calling:\n'pyUmlaut0r.py -d'.""")
    print("can't connect to daemon")
    sys.exit(1)


#set process name
utils.setProcessName("pyUmlaut0r")

#create trayIcon
trayIcon = QSystemTrayIcon()
trayIcon.setIcon(QIcon(":/pyUmlaut0rIcon.png"))
trayIcon.setContextMenu(utils.createMenu())
trayIcon.show()

#dbus "daemon"
DBusQtMainLoop(set_as_default = True)

class DBusInterface(dbus.service.Object):
  def __init__(self):
    busName = dbus.service.BusName('org.documentroot.umlaut0r', \
                                   bus = dbus.SessionBus())
    dbus.service.Object.__init__(self, busName, '/umlaut0r')

  @dbus.service.method('org.documentroot.umlaut0r', in_signature='s')
  def toClipboard(self, s):
    utils.toClipboard(s)

dbusInterface = DBusInterface()

#exec "daemon"
app.exec_()

