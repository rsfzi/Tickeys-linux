# coding: utf-8
import subprocess

from logger import logger
from threading import Thread
import os


terminal_id = os.environ["HOME"] + "/.tickeys/tickeys_terminal_window_id"
gui_id = os.environ["HOME"] + "/.tickeys/tickeys_GUI_window_id"


def save_terminal_window_id():
    try:
        stat, terminalId = subprocess.check_output('xdotool getactivewindow')
        with open(terminal_id, "w+") as f:
            if stat == 0:
                f.write(terminalId)
            else:
                f.write(0)
    except Exception as e:
        logger.error("Save terminal window id fail:" + str(e))


def read_terminal_window_id():
    with open(terminal_id, "r") as f:
        return f.read()


def hide_terminal():
    try:
        terminalId = read_terminal_window_id()
        if not terminalId:
            return
        subprocess.check_output(
            "xdotool windowactivate --sync %s" % terminalId)
        subprocess.check_output(
            "xdotool getactivewindow windowunmap")
    except Exception as e:
        logger.error(str(e))


def save_GUI_window_id():
    try:
        stat, GUIID = subprocess.check_output('xdotool getactivewindow')
        with open(gui_id, "w+") as f:
            if stat == 0:
                f.write(GUIID)
            else:
                f.write(0)
    except Exception as e:
        logger.error("Save GUI window id fail:" + str(e))


def read_GUI_window_id():
    with open(gui_id, "r") as f:
        return f.read()


def hide_GUI():
    try:
        GUIID = read_GUI_window_id()
        subprocess.check_output('xdotool windowunmap --sync %s' % GUIID)
    except Exception as e:
        logger.error(str(e))


def show_GUI():
    def show_notify():
        try:
            import notify2
            notify2.init('Tickeys')
            title = 'Tickeys'
            body = '程序“xdotool”尚未安装, 无法隐藏窗口。'
            iconfile = os.getcwd() + '/tickeys.png'
            notify = notify2.Notification(title, body, iconfile)
            notify.show()
        except Exception:
            return
    try:
        GUIID = read_GUI_window_id()
        if not GUIID or GUIID == "0":
            Thread(target=show_notify).start()
            return
        else:
            # read window ids
            command = "xdotool windowmap --sync %s && xdotool windowactivate --sync %s" % (GUIID, GUIID)
            stat, output = subprocess.check_output(command)
            return str(stat)
    except Exception as e:
        logger.error(str(e))
        return '256'


def check_tickeys_running_status():
    save_terminal_window_id()
    stat = show_GUI()
    if stat != "0":
        return False
    else:
        print("Tickeys is already running, show it")
        return True
