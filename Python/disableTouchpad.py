import pythoncom, pyHook, time

buff=1.0
lasthit=time.time()
isfirst=1

def main():
    def OnKeyboardEvent(event):
        t=time.time()
        global lasthit
        global isfirst
        lasthit=t
    
        
        isfirst=0
        return True
    
    def OnMouseEvent(event):
        #t=time.time()
        #global st
        global isfirst
        global lasthit
        global buff
        diff=time.time()-lasthit
        rc=True
        #print "ping"
        if isfirst:
            rc=True
            #print "1"
        
        if (diff<buff and not isfirst):

            rc=False
            #print "2"
        if(diff>buff and not isfirst):
            rc=True
            #print "3"
        return rc
    print "app started. close this window to stop"
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
    hm.MouseAll = OnMouseEvent
    hm.KeyDown = OnKeyboardEvent
    # set the hook
    hm.HookKeyboard()
    hm.HookMouse()
    # wait forever
    pythoncom.PumpMessages()

if __name__ == '__main__':
  main()
