try:
    from idlelib.tooltip import Hovertip
except ModuleNotFoundError:
    import tkinter as tk

    class Hovertip:
        def __init__(self, anchor_widget, text, hover_delay=1000):
            self.anchor_widget = anchor_widget
            self.text = text
            self.hover_delay = hover_delay
            self._after_id = None
            self._tipwindow = None

            anchor_widget.bind("<Enter>", self._schedule)
            anchor_widget.bind("<Leave>", self._hide)
            anchor_widget.bind("<ButtonPress>", self._hide)

        def _schedule(self, event=None):
            self._cancel()
            self._after_id = self.anchor_widget.after(
                self.hover_delay, self._show
            )

        def _cancel(self):
            if self._after_id:
                self.anchor_widget.after_cancel(self._after_id)
                self._after_id = None

        def _show(self):
            if self._tipwindow or not self.text:
                return

            x = self.anchor_widget.winfo_rootx() + 20
            y = self.anchor_widget.winfo_rooty() + self.anchor_widget.winfo_height() + 5

            self._tipwindow = tw = tk.Toplevel(self.anchor_widget)
            tw.wm_overrideredirect(True)
            tw.wm_geometry(f"+{x}+{y}")

            label = tk.Label(
                tw,
                text=self.text,
                justify=tk.LEFT,
                background="#ffffe0",
                relief=tk.SOLID,
                borderwidth=1,
                padx=4,
                pady=2,
            )
            label.pack()

        def _hide(self, event=None):
            self._cancel()
            if self._tipwindow:
                self._tipwindow.destroy()
                self._tipwindow = None
