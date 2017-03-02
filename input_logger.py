
import pythoncom
import pyHook
import os
import sendatalogging as log

# create logging file
if not os.path.exists("data"):
    os.makedirs("data")
logger = log.Logger("data\\")
logger.writeRow(['Timestamp, ms', 'Event', 'Key value', 'Cursor X, px', 'Cursor Y, px'])
logger.release()

def OnKeyboardEvent(event):
    logger.open()
    print 'MessageName:', event.MessageName
    print 'Message:', event.Message
    print 'Time:', event.Time
    print 'Window:', event.Window
    print 'WindowName:', event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    print 'Extended:', event.Extended
    print 'Injected:', event.Injected
    print 'Alt', event.Alt
    print 'Transition', event.Transition
    print '---'
    logger.writeRow([event.Time, 'Key', event.Key])
    logger.release()
    # return True to pass the event to other handlers
    return True
    # Define event callbacks

def OnMouseClickEvent(event):
    logger.open()
    # called when mouse events are received
    print 'MessageName:', event.MessageName
    print 'Time:', event.Time
    print 'Position:', event.Position
    print '---'
    logger.writeRow([event.Time, 'Mouse', 'LDown', event.Position[0], event.Position[1]])
    logger.release()
    return True

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
hm.MouseAllButtonsDown = OnMouseClickEvent
# set the hook
hm.HookMouse()
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()