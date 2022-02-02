import win32gui
# from ctypes import wintypes, windll, pointer

# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-enumwindows
# https://stackoverflow.com/questions/7142342/get-window-position-size-with-python
# https://stackoverflow.com/questions/40084734/attributeerror-module-ctypes-wintypes-has-no-attribute-create-unicode-buffer

# def callback(hwnd, extra):
#     rect = win32gui.GetWindowRect(hwnd)
#     x = rect[0]
#     y = rect[1]
#     w = rect[2] - x
#     h = rect[3] - y
#     print("Window %s:" % win32gui.GetWindowText(hwnd))
#     print("\tLocation: (%d, %d)" % (x, y))
#     print("\t    Size: (%d, %d)" % (w, h))

# def main():
# win32gui.EnumWindows(callback, None)
# "Bombcrypto" - Google Chrome
# windows = win32gui.FindWindow(None, "Bombcrypto - Google Chrome")
# print(windows)

# def GetWindowRectFromName(name:str)-> tuple:
# hwnd = windll.user32.FindWindowW(0, name)
# rect = wintypes.RECT()
# windll.user32.GetWindowRect(hwnd, pointer(rect))
# # print(hwnd)
# # print(rect)
# return (rect.left, rect.top, rect.right, rect.bottom)

def bombCallback(hwnd, bombs):
    hwndName = win32gui.GetWindowText(hwnd)
    if hwndName.startswith("Bombcrypto - "):
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        bomb = {
            "appID": hwnd,
            "position": (x, y),
            "size": (w, h),
        }
        bombs.append(bomb)

def findAllBombWindows():
    bombs = []
    win32gui.EnumWindows(bombCallback, bombs)
    return bombs


if __name__ == '__main__':
    print(findAllBombWindows())
