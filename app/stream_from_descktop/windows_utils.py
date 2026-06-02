import win32con
import win32gui
import win32api
from dataclasses import dataclass


@dataclass
class SelectWindow:
    hwnd: int
    title: str

    @property
    def region(self):
        left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)
        return left, top, right, bottom


class WindowSelector:

    @staticmethod
    def select_window() -> SelectWindow:

        x, y = win32api.GetCursorPos()

        hwnd = win32gui.WindowFromPoint((x, y))
        hwnd = win32gui.GetAncestor(hwnd, win32con.GA_ROOT)

        title = win32gui.GetWindowText(hwnd)

        return SelectWindow(hwnd=hwnd, title=title)



