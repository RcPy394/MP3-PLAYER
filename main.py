import tkinter as tk
from tkinter import *
import random, pygame, os
pygame.init()
pygame.mixer.init()
class MP3:
    def __init__(self,window):
        self.SONG_END=pygame.USEREVENT+1
        pygame.mixer.music.set_endevent(self.SONG_END)
        self.window=window
        self.window.geometry("600x200")
        self.window.title("MP3 Player by Robert Collingwood")
        self.EXTEN = ['.mp3']
        self.MusicList = self.getfromfile('./music', self.EXTEN)
        self.i=0
        pygame.mixer.music.load(self.MusicList[self.i])
        pygame.mixer.music.play()
        self.Mlabel=Label(self.window,text='',width=100,height=1,fg='black')
        self.Mlabel['text'] = self.getSongName(self.MusicList[self.i])
        self.Mlabel.pack()
        self.rs = Button(self.window, text='Random Song', width=10, height=1 ,bg='DeepSkyBlue2',fg='black', command = self.RandSong)
        self.rs.pack(fill = BOTH)
        self.pt = Button(self.window, text='<< Prev Track', width=10, height=3, bg='DeepSkyBlue2', fg='black', command = self.PrevTrack)
        self.pt.pack(side = LEFT, expand = True, fill = BOTH)
        self.button = Button(self.window, text='PAUSE', width=10, height=3, bg='DeepSkyBlue2', fg='black',command=self.PausePlay)
        self.button.pack(side = LEFT, expand = True, fill = BOTH)
        self.nt = Button(self.window, text='Next Track >>', width=10, height=3, bg='DeepSkyBlue2', fg='black', command=self.NextTrack)
        self.nt.pack(side=LEFT, expand=True, fill=BOTH)
        self.check_music()
        self.window.mainloop()

    def getfromfile(self,rootdir,e):
        filelist=[]
        counter=1
        for root, directories, filenames in os.walk(rootdir):
            for filename in filenames:
                if any(ext in filename for ext in e):
                    filelist.append(os.path.join(root,filename))
                    counter +=1
        return filelist
    def check_music(self):
        for event in pygame.event.get():
            if event.type == self.SONG_END:
                self.NextTrack()
        self.window.after(1000, self.check_music)
    def getSongName(self,song):
        SongName=song.replace("./music\\","")
        SongName=SongName.replace(".mp3","")
        return SongName
    def NextTrack(self):
        if(self.i== len(self.MusicList)-1):
            self.i=0
            pygame.mixer.music.load(self.MusicList[self.i])
            self.Mlabel['text'] = self.getSongName(self.MusicList[self.i])
            self.button['text'] = 'PAUSE'
            pygame.mixer.music.play()
        else:
            self.i=self.i + 1
            pygame.mixer.music.load(self.MusicList[self.i])
            self.Mlabel['text'] = self.getSongName(self.MusicList[self.i])
            self.button['text'] = 'PAUSE'
            pygame.mixer.music.play()
    def PrevTrack(self):
        if(self.i==0):
            self.i = len(self.MusicList)-1
            pygame.mixer.music.load(self.MusicList[self.i])
            self.Mlabel['text'] = self.getSongName(self.MusicList[self.i])
            self.button['text'] = 'PAUSE'
            pygame.mixer.music.play()
        else:
            self.i=self.i - 1
            pygame.mixer.music.load(self.MusicList[self.i])
            self.Mlabel['text'] = self.getSongName(self.MusicList[self.i])
            self.button['text']='PAUSE'
            pygame.mixer.music.play()
    def PausePlay(self):
        if(self.button['text']=='PLAY'):
            self.button['text']='PAUSE'
            pygame.mixer.music.unpause()
        elif(self.button['text']=='PAUSE'):
            self.button['text'] = 'PLAY'
            pygame.mixer.music.pause()
    def RandSong(self):
        self.i=random.randint(0,len(self.MusicList)-1)
        self.Mlabel['text'] = self.getSongName(self.MusicList[self.i])
        pygame.mixer.music.load(self.MusicList[self.i])
        self.button['text'] = 'PAUSE'
        pygame.mixer.music.play()
window = tk.Tk()
MP3(window)
