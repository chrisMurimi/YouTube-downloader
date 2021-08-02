from pytube import YouTube
import tkinter as tk 

WINDOW_WIDTH = 200
WINDOW_HEIGHT = 150
WINDOW_TITLE = " Chris YouTube Downloader"


class YoutubeDownloader:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry(f"{WINDOW_WIDTH} x{WINDOW_HEIGHT}")
        self.window.configure(bg="#3300ee")
        self.window.title(WINDOW_TITLE)
        
        #Names of the entries
        self.link_label =tk.Label(self.window, text = " DownLoad Link")
        self.link_label.grid( column = 0, row = 0)
        self.link_label =tk.Label(self.window, text = " Save File as")
        self.link_label.grid( column = 0, row = 1)
        self.link_label =tk.Label(self.window, text = " Save File path")
        self.link_label.grid( column = 0, row = 2)
        self.link_label =tk.Label(self.window, text = " File extension")
        self.link_label.grid( column = 0, row = 3)
        
        
       #entries
        self.link_entry = tk.Entry(master= self.window, width = 40)
        self.link_entry.grid(column = 1, row = 0 ) 
        self.link_entry = tk.Entry(master= self.window, width = 40)
        self.link_entry.grid(column = 1, row = 1 ) 
        self.link_entry = tk.Entry(master= self.window, width = 40)
        self.link_entry.grid(column = 1, row = 2 ) 
        self.link_entry = tk.Entry(master= self.window, width = 40)
        self.link_entry.grid(column = 1, row = 3 ) 
       
        self.download_button = tk.Button(self.window, text = "download", comand = self.__get_link)
        self.download_button.grid( column = 1, row =  4)
        return
   
    
    def __downloader(self, link, save_path = "", save_name ="", extension = "mp4"):
        yt = YouTube(link)
        yt_stream = yt.streams.filter(progressive =True, file_extension = extension).order_by("resolution").desc().first()
        yt_stream.download(out_put = save_path, filename = save_name)
        
        return
   
    def __get_link(self):
        link = self.link_entry.get()
        path = self.path_entry.get()
        name = self.name_entry.get()
        ext = self.ext_entry.get()
        
        self.__downloader(link, path, name, ext)
        
        return 
        
    
    
       
        
    def run_app(self):
        self.window.mainloop()
        return
    

if __name__=="__main__":
    app = YoutubeDownloader()
    app.run_app()
