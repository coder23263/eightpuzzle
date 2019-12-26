import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from eightpuzzle import *
from A_algorithm import solvePuzzle_A
from Depth_first import solvePuzzle_depth
from show import *
from PyQt5.QtCore import QTimer


alllog = '           '

class MyWindow(QMainWindow,Ui_eightPuzzle):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.Run.clicked.connect(self.Algorithm_choose) #run绑定运行程序函数
        self.srcLayout = "013425786"  # 初始状态
        self.destLayout = "647850321"  # 目标状态
        self.log = 'nihao'  # 存储run的log
        self.Go.clicked.connect(self.go_specific)
        self.Restore.clicked.connect(self.restore_all)# restore_all绑定
        self.count = 0
        timer = QTimer()
        timer.timeout.connect(self.process) # 计时器挂接到槽：process
        self.Run.clicked.connect(lambda :timer.start(1000))
        self.Restore.clicked.connect(lambda :timer.stop())

    def restore_all(self):
        global alllog
        alllog = '           '

        for i in range(1, 10):
            self_show = eval('self.show' + str(i))
            self_show.setText('')
            self_show2 = eval('self.show' + str(i) + '_2')
            self_show2.setText('')
            self_init = eval('self.init' + str(i))
            self_init.setText('')
            self_final = eval('self.final{}'.format(i))
            self_final.setText('')


    def go_specific(self):# 获取到具体值的步骤
        specific = int(self.lineEdit.text())
        if specific > len(alllog):
            QMessageBox.information(self, "步骤数", "最大步骤数为{}".format(len(alllog)),
                                    QMessageBox.Yes)
        else:
            specific_value = alllog[specific-1]
            for i in range(1, 10):
                self_show = eval('self.show' + str(i) + '_2')
                self_show.setText(str(specific_value[i-1]))

    def process(self):# 设置run后程序动态展示画面  , lst_steps
        try:
            self.count = self.count + 1
            if self.count < len(alllog):  # 更新一遍八数码的值
                for i in range(1, 10):
                    self_show = eval('self.show' + str(i))
                    if str(alllog[self.count][i-1]) != '0':  # 为零的置空白
                        self_show.setText(str(alllog[self.count][i-1]))
                    else:
                        self_show.setText('')
        except:
            pass
        # for i in range(9):#找到0的位置， 把lable的属性置空白
        #     if str(alllog[self.count][0]) == '0':
        #         pass

    def show_message(self):
        get_message = QMessageBox.information(self, "格式问题", "请输入正确的0-9数字格式",
                                QMessageBox.Yes)
        if str(get_message) == '16384':
            pass
    def show_message2(self):
        get_message = QMessageBox.information(self, "数据", "目标布局不可达",
                                QMessageBox.Yes)

    def get_init(self):  # 设置初始状态的值
        count = 0
        for i in range(1, 10):
            va = eval('self.init{}'.format(i))
            if 0 < len(va.text()) < 2 and 0 <= int(va.text()) <= 10:
                count += 1
        if count == 9:
            return [self.init1.text(), self.init2.text(), self.init3.text(), self.init4.text(), \
                    self.init5.text(), self.init6.text(), self.init7.text(), self.init8.text(), \
                    self.init9.text()]
        else:
            self.show_message()

    def get_final(self):  # 设置最后目标状态的值
        count = 0
        for i in range(1, 10):
            va = eval('self.final{}'.format(i))
            if 0 < len(va.text()) < 2 and 0 <= int(va.text()) <= 10:
                count += 1
        if count == 9:
            return [self.final1.text(), self.final2.text(), self.final3.text(), self.final4.text(), \
                    self.final5.text(), self.final6.text(), self.final7.text(), self.final8.text(), \
                    self.final9.text()]
        else:
            self.show_message()


    def Algorithm_choose(self):
        try:
            global alllog
            srcLayout_list = self.get_init() # 获取八数码初始值
            srcLayout = ''
            for i in range(len(srcLayout_list)):# 转字符串
                srcLayout += srcLayout_list[i]
            destLayout_list = self.get_final() # 获取八数码目标值
            destLayout = ''
            for i in range(len(destLayout_list)):
                destLayout += destLayout_list[i]
            self.srcLayout = srcLayout #赋值给类属性
            self.destLayout = destLayout

            for i in range(len(destLayout_list)):
                destLayout += destLayout_list[i]

            if self.algorithm_comboBox.currentText() == 'A':
                retCode, lst_steps = solvePuzzle_A(self.srcLayout, self.destLayout)
                # self.process()#lst_steps
                if retCode != 0:
                    # self.log = "目标布局不可达"
                    self.show_message2()
                    alllog = None
                else:
                    alllog = lst_steps#list
            elif self.algorithm_comboBox.currentText() == '深度搜索':
                retCode, lst_steps = solvePuzzle_depth(self.srcLayout, self.destLayout)
                if retCode != 0:
                    # self.log = "目标布局不可达"
                    self.show_message2()
                    alllog = None
                else:
                    alllog = lst_steps#list
            else:
                return '宽度搜索'
        except:
            pass



class childWindow(QMainWindow, Ui_Show):
    def __init__(self):
        super(childWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('log')
        self.result.setText('请先运行程序')
        # self.setFont(18)
        # self.setFont(self, 18)

        # self.pushButton.clicked.connect(self.btnClick)#按钮事件绑定
    def set_log(self):#设置log的值
        show_text = ''
        for i in range(len(alllog)-1):
            show_text = show_text + alllog[i][0]+' '+ alllog[i][1] + ' '+alllog[i][2] + '\n' + alllog[i][3]+' '+ alllog[i][4] + ' '+alllog[i][5] + '\n' + alllog[i][6]+' '+ alllog[i][7] + ' '+alllog[i][8] + '\n' + '  |' + '\n'
        show_text = show_text + alllog[len(alllog)-1][:3] + '\n' + alllog[len(alllog)-1][3:6] + '\n' + alllog[len(alllog)-1][6:9] + '\n'
        self.result.setText(show_text)


def get_log(child):
    # child.result = alllog
    # print(type(child.result))
    child.set_log()

    #不可达实例
    # srcLayout  = "013425768"#初始状态
    # destLayout = "647850321"#目标状态
#可达实例
# 013425786
# 647850321

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    child = childWindow()

    #通过toolButton将两个窗体关联
    btn = myWin.Log
    btn.clicked.connect(lambda: get_log(child))
    btn.clicked.connect(child.show)

    myWin.show()
    sys.exit(app.exec_())
