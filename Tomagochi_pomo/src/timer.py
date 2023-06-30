import time


class Timer:
    def __init__(self, gui):
        self.running = False
        self.start_time = 0
        self.gui = gui

    def update_clock(self):
        elapsed_time = self.get_elapsed_time()
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        clock_text = f"{minutes:02d}:{seconds:02d}"
        self.gui.clock_label.config(text=clock_text)
        if self.running:
            self.gui.root.after(1000, self.update_clock)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.update_clock()

    def stop_timer(self):
        self.running = False

    def get_elapsed_time(self):
        if self.running:
            return time.time() - self.start_time
        return 0
