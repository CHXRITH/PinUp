import customtkinter as tk
from CTkListbox import *
import win32gui
import win32con
import webbrowser

class PinUpApp:  
    def __init__(self, master):

        self.master = master
        master.title("PinUp")

        self.pinnedWin = []

        # mainFrame
        self.mainFrame = tk.CTkFrame(master)
        self.mainFrame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # detailsPanel
        self.detailsPanel = tk.CTkFrame(self.mainFrame)
        self.detailsPanel.grid(row=0, column=0, padx=5, pady=5, sticky="nsw")

        # Title
        self.PinUp = tk.CTkLabel(self.detailsPanel, text="PinUp", fg_color=("#fff", "#000"), corner_radius=8)
        self.PinUp.pack(side="top", padx=5, pady=5)

        # rightFrame
        self.rightFrame = tk.CTkFrame(self.mainFrame)
        self.rightFrame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        # Theme Change 
        self.appearance_mode_var = tk.Variable()
        self.appearance_mode_var.set("System")

        self.systemButton = tk.CTkRadioButton(
            self.detailsPanel,
            text="System",
            variable=self.appearance_mode_var,
            value="System",
            command=self.themeChange,
            fg_color=("#000", "#000"),
            corner_radius=6
        )
        self.systemButton.pack(padx=5, pady=5)

        self.darkButton = tk.CTkRadioButton(
            self.detailsPanel,
            text="Dark",
            variable=self.appearance_mode_var,
            value="Dark",
            command=self.themeChange,
            fg_color=("#000", "#000"),
            corner_radius=6
        )
        self.darkButton.pack(padx=5, pady=5)

        self.lightButton = tk.CTkRadioButton(
            self.detailsPanel,
            text="Light",
            variable=self.appearance_mode_var,
            value="Light",
            command=self.themeChange,
            fg_color=("#000", "#000"),
            corner_radius=6
        )
        self.lightButton.pack(padx=5, pady=5)

        # Space
        self.space = tk.CTkLabel(self.detailsPanel, text="")
        self.space.pack(side="top", padx=20, pady=5)

        # About
        self.aboutTitle = tk.CTkLabel(self.detailsPanel, text="About", fg_color=("#fff", "#000"), corner_radius=8)
        self.aboutTitle.pack(side="top", padx=5, pady=5)
        self.about = tk.CTkLabel(self.detailsPanel, text="PinUp is a window pinning application that allows you to keep important windows always on top of others. It helps you stay organized and focused.\n\n", wraplength=200)
        self.about.pack(side="top", padx=5, pady=5)
        
        # Version
        self.versionTitle = tk.CTkLabel(self.detailsPanel, text="Version", fg_color=("#fff", "#000"), corner_radius=8)
        self.versionTitle.pack(side="top", padx=20, pady=5)
        self.version = tk.CTkLabel(self.detailsPanel, text="Version 1.0.0")
        self.version.pack(side="top", padx=20, pady=5)
        
        # GitHub
        self.githubbtn = tk.CTkButton(
            self.detailsPanel,
            text="GitHub",
            fg_color=("#fff", "#000"),
            hover_color=("#fff", "#000"),
            corner_radius=6,
            command=self.github
        )
        self.githubbtn.pack(side="top", padx=20, pady=5)
        
        # Issues
        self.issuesbtn = tk.CTkButton(
            self.detailsPanel,
            text="Report Issues",
            fg_color=("#fff", "#000"),
            hover_color=("#fff", "#000"),
            corner_radius=6,
            command=self.reportIssues
        )
        self.issuesbtn.pack(side="top", padx=20, pady=5)

        # CHXRITH
        self.CHXRITH = tk.CTkLabel(self.detailsPanel, text="\nMade with 💜 by CHXRITH in Sri Lanka\n")
        self.CHXRITH.pack(side="top", padx=20, pady=5)

        # Pin
        self.availableFrame = tk.CTkFrame(self.rightFrame, width=400, height=800)
        self.availableFrame.pack(side="left", padx=5, pady=5, fill="both", expand=True)

        self.pinnedFrame = tk.CTkFrame(self.rightFrame, width=400, height=800)
        self.pinnedFrame.pack(side="left", padx=5, pady=5, fill="both", expand=True)

        self.availableTitle = tk.CTkLabel(self.availableFrame, text="Available Windows")
        self.availableTitle.grid(row=0, column=0, padx=5, pady=5)

        self.availableList = CTkListbox(self.availableFrame, width=400, height=300)
        self.availableList.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.refreshbtn = tk.CTkButton(self.availableFrame, text="Refresh Windows", command=self.refreshWindows, hover_color=("#fff", "#000"), fg_color=("#fff", "#000"), corner_radius=6)
        self.refreshbtn.grid(row=2, column=0, padx=5, pady=5)

        self.pinbtn = tk.CTkButton(self.availableFrame, text="Pin Selected Window", command=self.pinWindow, hover_color=("#fff", "#000"), fg_color=("#fff", "#000"), corner_radius=6)
        self.pinbtn.grid(row=3, column=0, padx=5, pady=5)

        self.pinnedTitle = tk.CTkLabel(self.pinnedFrame, text="Pinned Windows")
        self.pinnedTitle.grid(row=0, column=0, padx=5, pady=5)

        self.pinnedList = CTkListbox(self.pinnedFrame, width=400, height=300)
        self.pinnedList.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.unpinbtn = tk.CTkButton(self.pinnedFrame, text="Unpin Selected Window", command=self.unpinWindow, hover_color=("#fff", "#000"), fg_color=("#fff", "#000"), corner_radius=6)
        self.unpinbtn.grid(row=2, column=0, padx=5, pady=5)

        self.unpinAllbtn = tk.CTkButton(self.pinnedFrame, text="Unpin All Windows", command=self.unpinAll, hover_color=("#fff", "#000"), fg_color=("#fff", "#000"), corner_radius=6)
        self.unpinAllbtn.grid(row=3, column=0, padx=5, pady=5)

        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        
        # Unpin all
        self.unpinAll()
        
        # Load in Start
        self.refreshWindows()

    def github(self):
        webbrowser.open("https://github.com/CHXRITH")

    def reportIssues(self):
        webbrowser.open("https://github.com/CHXRITH/PinUp/issues/new")  

    def themeChange(self):
        new_appearance_mode = self.appearance_mode_var.get()
        tk.set_appearance_mode(new_appearance_mode)

        if new_appearance_mode == "Light":
            self.refreshbtn.configure(hover_color=("#000", "#fff"), fg_color=("#000", "#fff"))
            self.issuesbtn.configure(hover_color=("#000", "#fff"), fg_color=("#000", "#fff"))
            self.githubbtn.configure(hover_color=("#000", "#fff"), fg_color=("#000", "#fff"))
            self.pinbtn.configure(hover_color=("#000", "#fff"), fg_color=("#000", "#fff"))
            self.unpinbtn.configure(hover_color=("#000", "#fff"), fg_color=("#000", "#fff"))
            self.unpinAllbtn.configure(hover_color=("#000", "#fff"), fg_color=("#000", "#fff"))
        elif new_appearance_mode == "Dark":
            self.refreshbtn.configure(hover_color=("#fff", "#000"), fg_color=("#fff", "#000"))
            self.issuesbtn.configure(hover_color=("#fff", "#000"), fg_color=("#fff", "#000"))
            self.githubbtn.configure(hover_color=("#fff", "#000"), fg_color=("#fff", "#000"))
            self.pinbtn.configure(hover_color=("#fff", "#000"), fg_color=("#fff", "#000"))
            self.unpinbtn.configure(hover_color=("#fff", "#000"), fg_color=("#fff", "#000"))
            self.unpinAllbtn.configure(hover_color=("#fff", "#000"), fg_color=("#fff", "#000"))

    def refreshWindows(self):
        self.availableList.delete(0, tk.END)
        self.available_windows = []
        self.pinnedWin = []

        win32gui.EnumWindows(self._enum_windows_callback, None)
        for window_handle, window_title in self.available_windows:
            self.availableList.insert(tk.END, window_title)

        # Unpin previous
        self.unpinAll()

    def _enum_windows_callback(self, hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            window_class = win32gui.GetClassName(hwnd)
            if window_title and window_title != "Program Manager" and window_title != "Shell_TrayWnd" \
            and window_class not in ["SysListView32", "Button", "Static"]:
                self.available_windows.append((hwnd, window_title))

            # Check if the window is already pinned
            if (hwnd, window_title) in self.pinnedWin:
                self.winTop(hwnd)

    def pinWindow(self):
        selection_index = self.availableList.curselection()
        if selection_index is not None and selection_index < len(self.available_windows):
            window_handle, window_title = self.available_windows[selection_index]
            self.winTop(window_handle)
            self.pinnedWin.append((window_handle, window_title))
            self.updatePinned()

    def unpinWindow(self):
        selection_index = self.pinnedList.curselection()
        if selection_index is not None and selection_index < len(self.pinnedWin):
            window_handle, _ = self.pinnedWin[selection_index]
            win32gui.SetWindowPos(window_handle, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                                  win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            del self.pinnedWin[selection_index]
            self.updatePinned()

    def unpinAll(self):
        for window_handle, _ in self.pinnedWin:
            win32gui.SetWindowPos(window_handle, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                                  win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        self.pinnedWin = []
        self.updatePinned()

    def winTop(self, window_handle):
        win32gui.SetWindowPos(window_handle, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    def updatePinned(self):
        self.pinnedList.delete(0, tk.END)
        for _, window_title in self.pinnedWin:
            self.pinnedList.insert(tk.END, window_title)

def main():
    root = tk.CTk()
    root.iconbitmap("icon.ico")
    app = PinUpApp(root)
    root.resizable(width=False, height=False)
    root.mainloop()

if __name__ == "__main__":
    main()