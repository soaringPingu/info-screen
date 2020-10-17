import sys# Use PySide2 to allow direct use of Qt UI filesfrom PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit# import the GUIfrom ui_rwr import Ui_MainWindowclass MainWindow(QMainWindow):    def __init__(self):        super(MainWindow, self).__init__()        self.ui = Ui_MainWindow()        self.ui.setupUi(self)        # Link to best information so far for connecting widgets to code:        # https://ethicalhackingguru.com/getting-started-building-a-python-gui-using-pyqt5/        # Set up actions on events below this line        self.ui.minutes_per_km_cbox.currentIndexChanged.connect(self.update_data)        self.ui.rwr_distance_dspin.textChanged.connect(self.update_data)        self.ui.minute_per_km_spin.textChanged.connect(self.update_data)        self.ui.seconds_per_km_spin.textChanged.connect(self.update_data)        # Update the screen information once regardless of events        self.update_data()    def update_data(self):        # self.output_text.text = "Button is pressed!"        run_seconds = 0        walk_seconds = 0        expected_minutes_per_km = 0        expected_seconds_per_km = 0        km_per_interval = 0        interval_count = 0        result_text = ""        selected_text = self.ui.minutes_per_km_cbox.currentText()        # Get the run / walk ratio, which is fixed depending on the contents of the combobox        if selected_text == " 4:30 min/km":            run_seconds = 5 * 60            walk_seconds = 30        elif selected_text == " 5:00 min/km":            run_seconds = 4 * 60            walk_seconds = 30        elif selected_text == " 5:30 min/km":            run_seconds = 2 * 60            walk_seconds = 30        elif selected_text == " 6:00 min/km":            run_seconds = 90            walk_seconds = 30        elif selected_text == " 6:30 min/km":            run_seconds = 75            walk_seconds = 30        elif selected_text == " 7:00 min/km":            run_seconds = 60            walk_seconds = 30        elif selected_text == " 8:00 min/km":            run_seconds = 30            walk_seconds = 30        elif selected_text == " 9:00 min/km":            run_seconds = 20            walk_seconds = 30        elif selected_text == "10:00 min/km":            run_seconds = 15            walk_seconds = 30        elif selected_text == "11:00 min/km":            run_seconds = 10            walk_seconds = 30        # Get the expected time per km for this run        expected_seconds_per_km = self.ui.minute_per_km_spin.value() * 60 + self.ui.seconds_per_km_spin.value()        km_per_interval = (run_seconds + walk_seconds) / expected_seconds_per_km        interval_count = int(self.ui.rwr_distance_dspin.value() / km_per_interval)  # Interval count without decimals        # Check if the total distance by the truncated intervals is less than the desired distance, if so, add 1        if (interval_count * km_per_interval) < self.ui.rwr_distance_dspin.value():            interval_count += 1        result_text = str(interval_count) + " x [" + str(run_seconds) + " - " + str(walk_seconds) + \            "] --> Σ " + str(round(interval_count * km_per_interval, 1)) + " km"        self.ui.interval_summary_text.setText(result_text)if __name__ == "__main__":    app = QApplication(sys.argv)    window = MainWindow()    window.show()    sys.exit(app.exec_())