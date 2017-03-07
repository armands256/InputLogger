
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
mouse_coordinates = [0,0]

def OnKeyboardEvent(event):
    global mouse_coordinates
    logger.open()
    print 'MessageName:', event.MessageName
    print 'Key:', event.Key
    print 'Time:', event.Time
    # print 'Message:', event.Message
    #print 'Window:', event.Window
    #print 'WindowName:', event.WindowName
    #print 'Ascii:', event.Ascii, chr(event.Ascii)gffd
    #print 'KeyID:', event.KeyID
    #print 'ScanCode:', event.ScanCode
    #print 'Extended:', event.Extended
    #print 'Injected:', event.Injected
    #print 'Alt', event.Alt
    #print 'Transition', event.Transition
    print '---'
    logger.writeRow([event.Time, "'Key'", "'"+event.Key+"'", mouse_coordinates[0], mouse_coordinates[1]])
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
    logger.writeRow([event.Time, "'Mouse'", "'LDown'", event.Position[0], event.Position[1]])
    logger.release()
    return True


def OnMouseMoveEvent(event):
    print('Move')
    global mouse_coordinates
    print(event.Position)
    mouse_coordinates = list(event.Position)
    return True

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
hm.MouseAllButtonsDown = OnMouseClickEvent
hm.MouseMove = OnMouseMoveEvent
# set the hook
hm.HookMouse()
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()

#