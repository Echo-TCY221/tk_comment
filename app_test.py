import time

from pywinauto.application import Application

from pywinauto import Desktop

# 启动应用程序
app = Application(backend="uia").start(r'D:\app5\tk\douyin\douyin_launcher.exe')
time.sleep(5)

# 获取当前系统中所有已打开的窗口
windows = Desktop(backend="uia").windows()

# 打印所有窗口的名称
for window in windows:
    print(window.window_text())

# 查找包含“抖音”的窗口
dlg = None
for window in windows:
    if "抖音" in window.window_text():
        dlg = window
        break

if dlg is None:
    print("没有找到包含‘抖音’的窗口")
    exit()

# 定位菜单项
file_menu = dlg.MenuItem('首页')
file_menu.Click()
time.sleep(3)

# 定位文本编辑框
text_editor = dlg.child_window(title="Edit", control_type="Edit")
text_editor.type_keys('Hello, pywinauto!', with_spaces=True)


# 点击搜搜按钮
# 定位“保存”按钮
save_button = dlg.child_window(title="搜索", control_type="Button")

# 点击按钮
save_button.click()


# 清空文本框
text_editor.set_edit_text('')




