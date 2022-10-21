from tkinter import Tk

from services.ui_logic import UILogic
from ui.ui import UI


def main():
    window = Tk()
    window.title("Reitinhaku")

    ui_logic = UILogic()
    ui = UI(window, ui_logic)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
