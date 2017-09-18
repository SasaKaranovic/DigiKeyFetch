import ctypes
import ctypes.wintypes
import win32con


class GlobalHotKeys(object):
    """
    Register a key using the register() method, or using the @register decorator
    Use listen() to start the message pump
    Example:
    from globalhotkeys import GlobalHotKeys
    @GlobalHotKeys.register(GlobalHotKeys.VK_F1)
    def hello_world():
        print 'Hello World'
    GlobalHotKeys.listen()
    """

    key_mapping = []
    user32 = ctypes.windll.user32

    MOD_ALT = win32con.MOD_ALT
    MOD_CTRL = win32con.MOD_CONTROL
    MOD_CONTROL = win32con.MOD_CONTROL
    MOD_SHIFT = win32con.MOD_SHIFT
    MOD_WIN = win32con.MOD_WIN

    @classmethod
    def register(cls, vk, modifier=0, func=None):
        """
        vk is a windows virtual key code
         - can use ord('X') for A-Z, and 0-1 (note uppercase letter only)
         - or win32con.VK_* constants
         - for full list of VKs see: http://msdn.microsoft.com/en-us/library/dd375731.aspx
        modifier is a win32con.MOD_* constant
        func is the function to run.  If False then break out of the message loop
        """

        # Called as a decorator?
        if func is None:
            def register_decorator(f):
                cls.register(vk, modifier, f)
                return f
            return register_decorator
        else:
            cls.key_mapping.append((vk, modifier, func))


    @classmethod
    def listen(cls):
        """
        Start the message pump
        """

        for index, (vk, modifiers, func) in enumerate(cls.key_mapping):
            if not cls.user32.RegisterHotKey(None, index, modifiers, vk):
                raise Exception('Unable to register hot key: ' + str(vk))

        try:
            msg = ctypes.wintypes.MSG()
            while cls.user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    (vk, modifiers, func) = cls.key_mapping[msg.wParam]
                    if not func:
                        break
                    func()

                cls.user32.TranslateMessage(ctypes.byref(msg))
                cls.user32.DispatchMessageA(ctypes.byref(msg))

        finally:
            for index, (vk, modifiers, func) in enumerate(cls.key_mapping):
                cls.user32.UnregisterHotKey(None, index)


    @classmethod
    def _include_defined_vks(cls):
        for item in win32con.__dict__:
            item = str(item)
            if item[:3] == 'VK_':
                setattr(cls, item, win32con.__dict__[item])


    @classmethod
    def _include_alpha_numeric_vks(cls):
        for key_code in (range(ord('A'), ord('Z')) + range(ord('0'), ord('9'))):
            setattr(cls, 'VK_' + chr(key_code), key_code)


# Not sure if this is really a good idea or not?
#
# It makes decorators look a little nicer, and the user doesn't have to explicitly use win32con (and we add missing VKs
# for A-Z, 0-9
#
# But there no auto-complete (as it's done at run time), and lint'ers hate it
GlobalHotKeys._include_defined_vks()
GlobalHotKeys._include_alpha_numeric_vks()