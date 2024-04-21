import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1000x200")
        mixer.init()
        self.track = StringVar()
        self.status = StringVar()

        trackframe = LabelFrame(self.root, text="Song Track", font=("arial", 15, "bold"), bg="#8F00FF", fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=("arial", 24, "bold"), bg="#8F00FF", fg="#B0FC38").grid(row=0, column=0, padx=10, pady=5)
        trackstatus = Label(trackframe, textvariable=self.status, font=("arial", 24, "bold"), bg="#8F00FF", fg="#B0FC38").grid(row=0, column=1, padx=10, pady=5)

        buttonframe = LabelFrame(self.root, text="Control Panel", font=("arial", 15, "bold"), bg="#8F00FF", fg="white", bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=100, width=600, height=100)
        playbtn = Button(buttonframe, text="PLAY", command=self.playsong, width=6, height=2, font=("arial", 12, "bold"), bg="#B0FC38", fg="#8F00FF").grid(row=0, column=0, padx=10, pady=5)
        pausebtn = Button(buttonframe, text="PAUSE", command=self.pausesong, width=6, height=2, font=("arial", 12, "bold"), bg="#B0FC38", fg="#8F00FF").grid(row=0, column=1, padx=10, pady=5)
        unpausebtn = Button(buttonframe, text="UNPAUSE", command=self.unpausesong, width=6, height=2, font=("arial", 12, "bold"), bg="#B0FC38", fg="#8F00FF").grid(row=0, column=2, padx=10, pady=5)
        stopbtn = Button(buttonframe, text="STOP", command=self.stopsong, width=6, height=2, font=("arial", 12, "bold"), bg="#B0FC38", fg="#8F00FF").grid(row=0, column=3, padx=10, pady=5)

        songsframe = LabelFrame(self.root, text="Song Playlist", font=("arial", 15, "bold"), bg="#8F00FF", fg="white", bd=5, relief=GROOVE)
        songsframe.place(x=600, y=0, width=400, height=200)
        scroll_y = Scrollbar(songsframe, orient=VERTICAL)
        self.playlist = Listbox(songsframe, yscrollcommand=scroll_y.set, selectbackground="lightblue", selectmode=SINGLE, font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        os.chdir("Path_to_your_songs_folder")
        songtracks = os.listdir()
        for track in songtracks:
            self.playlist.insert(END, track)

    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        mixer.music.load(self.playlist.get(ACTIVE))
        mixer.music.play()

    def stopsong(self):
        self.status.set("-Stopped")
        mixer.music.stop()

    def pausesong(self):
        self.status.set("-Paused")
        mixer.music.pause()

    def unpausesong(self):
        self.status.set("-Playing")
        mixer.music.unpause()

root = Tk()
MusicPlayer(root)
root.mainloop()