# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from mydesign import Ui_Dialog


class Example(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


app = QApplication(sys.argv)
w = Example()
w.show()
sys.exit(app.exec_())