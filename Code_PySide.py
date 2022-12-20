from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import Qt, QObject, QThread, Signal, QUrl
from PySide6.QtWidgets import (
                             QApplication, QLabel,
                             QMainWindow, QPushButton,
                             QVBoxLayout, QFileDialog,
                             QTableWidget, QWidget,
                             QTableWidgetItem, QProgressBar
                             )

from Ui_PySide import Ui_Asterisk_Extractor  # импорт нашего сгенерированного файла
import sys, configparser, pymysql, time, pathlib
import paramiko
from pathlib import Path


class CFunc:
    #функция перевода секунды в дату формата %H:%M:%S
    @staticmethod
    def sec2time(sec):
        print (sec)
        try:
            sec = int(sec)
            if int(sec) > 86400:
                m, sec = divmod(sec, 60)
                h, m = divmod(m, 60)
                return ('{}:{:0>2}:{:0>2}'.format(h, m, sec))
            else: 
                ty_res = time.gmtime(int(sec))
                res = time.strftime("%H:%M:%S",ty_res)
                return res
        except:
            return ('00:00:00')

    #функция документированияданных в файл
    @staticmethod
    def write2list(w_file):
        # открываем файл в режиме записи utf-8
        with open("some.txt", 'a', encoding='utf-8') as my_w_file:
            # записываем все строки
            my_w_file.write(w_file)
            my_w_file.close()

    #функция подключения и выполнения команд по SSH
    @staticmethod
    def paramiko_conn(paramiko_cammand):
        # Объединяем полученную строку с недостающими частями пути
        path_config = Path(pathlib.Path.cwd(), 'config.ini')
        print (path_config)
        config = configparser.ConfigParser()
        config.read(path_config, encoding='utf-8-sig')
        # Создать объект SSH
        ssh = paramiko.SSHClient()
        # Разрешить соединения с хостами, которых нет в файле know_hosts
        
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # подключиться к серверу
        ssh.connect(
            hostname=config.get('paramiko', 'machine'),
            port=22, username=config.get('paramiko', 'username'),
            password=config.get('paramiko', 'password')
            )
        # Исключая заказ
        stdin, stdout, stderr = ssh.exec_command(paramiko_cammand)
        # Получить результат команды
        res,err = stdout.read(),stderr.read()
        result = res if res else err
        
        print(result.decode())
        
        # Закрыть соединение
        ssh.close()

        #возвращаем результат выполнения
        return (result.decode())

# Step 1: Create a worker class
class Worker(QObject):
    def __init__(self, valisChecked, lines_number, cdb, cde):
        super().__init__()
        self._valisChecked = valisChecked
        self._lines_number = lines_number
        self._cdb = cdb
        self._cde = cde
        # Объединяем полученную строку с недостающими частями пути
        path_config = Path(pathlib.Path.cwd(), 'config.ini')
        print (path_config)
        config = configparser.ConfigParser()
        config.read(path_config, encoding='utf-8-sig')
        self.connection = pymysql.connect(host=config.get('mysql', 'host'),
                            user=config.get('mysql', 'user'),
                            passwd=config.get('mysql', 'password'),
                            database=config.get('mysql', 'database'),
                            charset="utf8mb4")

    finished = Signal()
    progress_pb = Signal(int)
    progressWidg = Signal(int, str, str)
    progresstextBrowser2 = Signal(list)

    def run(self):
        with self.connection.cursor() as cursor:
            self.count_lines_number = 0
            self.total_time = 0
            self.total_count = 0
            self.local_count_end = 0
            self.local_time_end = 0
            for number in self._lines_number:
                if number == 'end':
                    print('input error end')
                    time.sleep(0.22)
                    self.count_lines_number += 1
                    self.progress_pb.emit(self.count_lines_number)
                    self.progressWidg.emit(int(1), str(self.local_count_end), str(self.local_time_end))
                    self.local_count_end = 0
                    self.local_time_end = 0
                    continue
                try:
                    int(number)
                except ValueError:
                    print('input error number')
                    time.sleep(0.11)
                    self.count_lines_number += 1
                    self.progress_pb.emit(self.count_lines_number)
                    continue
                if len(number) not in  [4,6,11]:
                    time.sleep(0.11)
                    self.count_lines_number += 1
                    self.progress_pb.emit(self.count_lines_number)
                    continue
                if (len(number) == 11 and self._valisChecked == 'dst'):
                    self._valisChecked = 'did'
                    number = number[5:]

                sql = "SELECT COUNT(`clid`), SUM(`billsec`) FROM `cdr` WHERE `{0}` = '{1}' AND `disposition` = 'ANSWERED' AND `calldate` >= '{2} 00:00:00' AND `calldate` < '{3} 23:59:59'".format(self._valisChecked, number, self._cdb, self._cde)
                time.sleep(0.11)
                self.count_lines_number += 1
                self.progress_pb.emit(self.count_lines_number)
                print (sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:
                    #lines_data= ("Номер: {0}, количество звонков: {1}, общая длительность: {2} секунды или ,{3}".format(number, row[0], row[1], self.sec2time(row[1])))
                    lines_data= ("{0}, {1}, {2}, {3}".format(number, row[0], row[1], CFunc.sec2time(row[1])))
                    CFunc.write2list(lines_data)
                    print("{0} {1} {2}".format(number, row[0], row[1]))
                    if len(number) == 11:
                        number = number[5:]
                    self.progressWidg.emit(int(number), str(row[0]), str(row[1]))
                    try:
                        int(row[1])
                        self.total_time += int(row[1])
                        self.total_count += int(row[0])

                        self.local_time_end += int(row[1])
                        self.local_count_end += int(row[0])
                    except:
                        print('total_time error time')
                        continue

                print("The query affected {} rows".format(cursor.rowcount))
            self.progressWidg.emit(int(9), str(self.total_count), str(self.total_time))
            self.finished.emit()

class FunctionScanChannel(QtCore.QThread):
    dataChangedSC = QtCore.Signal(str)
    finishedSC = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        self.working = True

    def run(self):
        self.dataChangedSC.emit("Start Function1")
        nSC = 0
        while self.working:
            nSC +=1
            print(nSC)
            resultdataSC = CFunc.paramiko_conn(f"asterisk -rx \"pjsip show channels concise\"")
            self.dataChangedSC.emit(f"Data  FunctionSC {nSC}: {resultdataSC}")
            self.sleep(10)

            if not self.stoped():
                nSC = 0
                break
        self.finishedSC.emit(f"finished FunctionSC: -------")

    def stoped(self): 
        return self.working

class mywindow(QMainWindow, Ui_Asterisk_Extractor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        # adding functions to buttons from here
    #tab1 
        self.Button_test.clicked.connect(self._clicked_push_button_test)
        self.Button_execute.clicked.connect(self._select_data_mysql)
        self.actionOpen.triggered.connect(self._clicked_push_button_open_number)
        self.actionSaveToFile.triggered.connect(self._clicked_file_save)
        self.actionAbout.triggered.connect(self._show_modal_window_about)
    #####################################################################
    #tab2
        self.Button_2_SearchIp.clicked.connect(self._clicked_push_button_SearchIp)
        self.pushButton_2_test.clicked.connect(self._clicked_push_button_2_Test)
        self.pushButton_2_ModelPhone.clicked.connect(self._clicked_push_button_2_ModelPhone)
        self.pushButton_2_BanIp.clicked.connect(self._clicked_pushButton_2_BanIp)
   #####################################################################
    #tab3
        self.Button_3_ChanAct.clicked.connect(self._clicked_Button_3_ChanAct)
        self.functionscanchannel = FunctionScanChannel()
        self.functionscanchannel.dataChangedSC.connect(self.dataThreadsSC)
        self.functionscanchannel.finishedSC.connect(self.finishThreadsSC) 
        self.Button_CS_down.clicked.connect(self._clicked_Button_CS_down)

    #обработчик нажатия клавиш
    def keyPressEvent(self, event):
        if event.key() ==QtCore.Qt.Key_F1:
            self._show_modal_window_about()
        if event.key() == QtCore.Qt.Key_F2:
            self._clicked_push_button_open_number()
        if event.key() == QtCore.Qt.Key_F3:
            self._select_data_mysql()
        event.accept()

    #получение данных из сигнала в GUI
    def reportProgress(self, n):
        self.progressBar.setValue(n)
        self.label_3.setText(f"Long-Running Step: {n}")

    #получение данных из сигнала в GUI
    def reportProgressWidg(self,num, n0, n1):
        self.tableWidgetResult.resizeColumnsToContents()
        rowPosition = self.tableWidgetResult.rowCount()
        self.tableWidgetResult.insertRow(rowPosition)
        self.tableWidgetResult.setItem(rowPosition , 0, QTableWidgetItem(str(num))) #Номер:
        self.tableWidgetResult.setItem(rowPosition , 1, QTableWidgetItem(str(n0))) #количество звонков:
        self.tableWidgetResult.setItem(rowPosition , 2, QTableWidgetItem(str(n1)))#общая длительность:
        self.tableWidgetResult.setItem(rowPosition , 3, QTableWidgetItem(str(CFunc.sec2time(n1)))) #HH:MM:SS:
        lines_data= ("Номер: {0}, количество звонков: {1}, общая длительность: {2} секунды или ,{3}".format(num, n0, n1, str(CFunc.sec2time(n1))))
        self.textBrowser.append(lines_data)

    def _select_data_mysql(self):
        self.thread = QThread()
        value = self.comboBox_arr.currentText()
        if value == 'входящие':
            valisChecked = "dst"#######
        if value == 'исходящие':
            valisChecked = "src"#######
        lines_number = self.input_number2list(self.textEditNumber.toPlainText())#######
        cdb = self.dt2query(self.calendar_db)
        cde = self.dt2query(self.calendar_de)
        print(f"phone number: {lines_number} \n")
        self.textBrowser.append(valisChecked)
        self.textBrowser.append("Номер:, количество звонков:, общая длительность(секунды):, HH:MM:SS")
        len_n_lines_number = len(lines_number)
        self.progressBar.setValue(0)
        self.progressBar.setRange(0, len_n_lines_number);
        count_lines_number = 0
        self.tableWidgetResult.setRowCount(0)
        self.tableWidgetResult.setColumnCount(4)
                # Устанавливаем заголовки таблицы
        self.tableWidgetResult.setHorizontalHeaderLabels(["Номер:", "количество звонков:", "общая длительность(секунды):", "HH:MM:SS:"])
        self.tableWidgetResult.resizeColumnsToContents()
        rowPosition = self.tableWidgetResult.rowCount()
        self.tableWidgetResult.insertRow(rowPosition)
        self.tableWidgetResult.setItem(rowPosition , 0, QTableWidgetItem('Номер:'))
        self.tableWidgetResult.setItem(rowPosition , 1, QTableWidgetItem('количество звонков:'))
        self.tableWidgetResult.setItem(rowPosition , 2, QTableWidgetItem('общая длительность(секунды):'))
        self.tableWidgetResult.setItem(rowPosition , 3, QTableWidgetItem('HH:MM:SS'))

        # Step 3: Create a worker object
        self.worker = Worker(valisChecked, lines_number, cdb, cde)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress_pb.connect(self.reportProgress)

        self.worker.progressWidg.connect(self.reportProgressWidg)
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        self.Button_execute.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.Button_execute.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: self.label_3.setText("Long-Running Step: 0")
        )

    def _clicked_push_button_test(self):
    # when button is pressed this method is being called
        print(self.horizontalSlider_CS.value() * 1000)
        pass

    # функция импорта номеров
    def _clicked_push_button_open_number(self):
        file_name_r, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if file_name_r != "":
            with open(file_name_r, 'r') as fr:
                data_r_n = fr.read()
                my_text = self.textEditNumber.setText(data_r_n)

    # функция сохранения в файл
    def _clicked_file_save(self):
        files_types = "All Files (*);;Text Files (*.txt);;CSV (*.csv)"
        options = QFileDialog.Options()
        file_name_w, _ = QFileDialog.getSaveFileName(self, 'Save as... File', self.dt2query(self.calendar_db)+'.csv', filter=files_types,options=options)
        if not file_name_w: return

        self.files_types = files_types
        with open(file_name_w, 'w') as f:
            for row in range(self.tableWidgetResult.rowCount()):
                tmp = []
                for col in range(self.tableWidgetResult.columnCount()):
                    try: tmp.append(self.tableWidgetResult.item(row,col).text())
                    except: tmp.append('')
                f.write(';'.join(tmp) + '\n')

    def read2list(self, r_file):
        # открываем файл в режиме чтения utf-8
        with open(r_file, 'r', encoding='utf-8') as r_content:
            # читаем все строки и удаляем переводы строк
            lines = r_content.readlines()
            lines = [line.rstrip('\n') for line in lines]
            return lines

    # читает файл в список
    def input_number2list(self, lines_number):
        input_number = lines_number
        item_input_number = list(input_number.split("\n"))
        return item_input_number

    #date in calendar
    def dt2query(self, calendar):
        qdate = calendar.selectedDate()
        pydate = str(qdate.toPython())
        return pydate

    #функция вывода модального окна
    def _show_modal_window_about(self):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("Ver.2022031")
        button = dlg.exec()
        if button == QtWidgets.QMessageBox.Ok:
            print("OK!")
    #####################################################################


    ###tab2

    def link(self, linkStr):
        QDesktopServices.openUrl(QUrl(linkStr))

    #функция вывода модального окна
    def _clicked_push_button_SearchIp(self):
        resultdata = CFunc.paramiko_conn("asterisk -rx 'pjsip show aor "+self.lineEdit_2_SNember.text()+"' | awk '$1 == \"contact\" {print $3}'")
        # if none result
        if len(resultdata) < 3:
            print ('result Active None, enable search log')
            result2data = CFunc.paramiko_conn("cat /var/log/asterisk/full.0 | grep "+self.lineEdit_2_SNember.text()+"@192.168. | awk 'BEGIN { FS = \" \" } {print $1\"\", $2\"\", $6;exit}'")
            if len(result2data) <3:
                self.textEdit_2_PhoneInfo.setText("NO DATA FILE")
                return
            resultdata = result2data.split(" ")[2] + result2data.split(" ")[0] + " " + result2data.split(" ")[1]
            print (result2data)
    
        # result ok =)
        # if none result
        if len(resultdata) > 3:
        #activate Link
            self.label_2_openLink.setEnabled(True)
            self.label_2_openLink.linkActivated.connect(self.link)
            self.label_2_openLink.setText('<a href="'+ (resultdata.split(":")[1].split("@")[1]) +'">OpenLink/</a>')

        textEdit_2_PhoneInfo_txt = (f'Last IP:\n' + resultdata)
        self.textEdit_2_PhoneInfo.setText(textEdit_2_PhoneInfo_txt)

    ##
    def _clicked_push_button_2_Test(self):
        resultdata = CFunc.paramiko_conn("cat /var/log/asterisk/full.0 | grep "+self.lineEdit_2_SNember.text()+"@192.168. | awk '{print $8;exit}'")
        print (resultdata)
    
    def _clicked_push_button_2_ModelPhone(self):
        modphoncomm = CFunc.paramiko_conn("asterisk -rx 'database show registrar' | cut -d, -f1,7,12 | awk 'BEGIN { FS = \": {\" } {print $2}' | grep "+self.lineEdit_2_SNember.text()+"")
        if (len(self.lineEdit_2_SNember.text()) == 4 and self.lineEdit_2_SNember.text().isnumeric()):
                
            modphoncomm2 = dict(subString.split(":") for subString in modphoncomm.replace("\"", "").split(","))
            self.textEdit_2_PhoneInfo.setText(
                f"""Ip_addr: {modphoncomm2.get('via_addr')}
End point: {modphoncomm2.get('endpoint')}
Model_phone: {modphoncomm2.get('user_agent')}
""")
        else:
            
            print (len(modphoncomm.splitlines()))

            array = modphoncomm.split('\n')
            self.textBrowser_Tool_Alert.clear()
            for line in array:
                self.textBrowser_Tool_Alert.append("LINE: " + line)
            self.textBrowser_Tool_Alert.append("LINES: %s" % len(array))

    #ban funct
    def _clicked_pushButton_2_BanIp(self):
        self.textBrowser_Tool_Alert.clear()
        if not self.lineEdit_2_SNember.text():
            resultdata = CFunc.paramiko_conn(f"fail2ban-client status asterisk-iptables")
            if not resultdata:
                self.textBrowser_Tool_Alert.append("Not banned ip:ERROR")
            else:
                self.textBrowser_Tool_Alert.append(resultdata)
        else:
            resultdata = CFunc.paramiko_conn(f"fail2ban-client set asterisk-iptables unbanip {self.lineEdit_2_SNember.text()}")
            self.textBrowser_Tool_Alert.append(resultdata)

    #tab3
    def _clicked_Button_3_ChanAct(self):
        if self.Button_3_ChanAct.text() == 'Scan Channels':
            self.Button_3_ChanAct.setText('Scan Stop')
            self.label_3_CS_down.setText("")
            self.functionscanchannel.working = True
            self.functionscanchannel.start()
        else:
            self.Button_3_ChanAct.setText('Scan Channels')
            self.functionscanchannel.working = False

    def dataThreadsSC(self, text):
        self.textBrowser_3_ChannelBrowser.clear()
        self.textBrowser_3_ChannelBrowser.insertPlainText(text.replace("\n      Exten:", "  Exten:")+'\n')

    def finishThreadsSC(self, text):
        self.label_3_CS_down.setText(f"{text}")

        #label_3_CS_down
    def _clicked_Button_CS_down(self):
        print (self.lineEdit_3_CS_down.text())
        RequestedDown = CFunc.paramiko_conn("asterisk -rx 'channel request hangup "+self.lineEdit_3_CS_down.text()+"'")
        self.label_3_CS_down.setText(f"{RequestedDown}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = mywindow()
    application.show()
    sys.exit(app.exec())
