import sys
from actions import *
from pet import Pet

def main():
    app = QApplication(sys.argv)

    window = MainWindow(Pet)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()