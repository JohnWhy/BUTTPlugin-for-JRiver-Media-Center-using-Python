import requests
import time

def UpdateArtistSong():
    r = requests.get('http://localhost:52199/MCWS/v1/Playback/Info?Zone=-1')
    #I use localhost since I'm running this on the same machine as JRiver Media Center
    #Make sure you turn on JRiver Media Center's server settings
    string = r.text                                                                 
    yStart = string.find('Item Name="Artist"')
    yEnd = string[yStart:].find("</Item>")
    Artist = string[yStart+19:yEnd+yStart]
    print(Artist)
    xStart = string.find('Item Name="Name"')
    xEnd = string[xStart:].find("</Item>")
    Song = string[xStart+17:xEnd+xStart]
    print(Song)

    with open('BUTTInfo.txt', "w") as f: #BUTTInfo.txt can be whatever you want the textfile to be named
        f.write(Song + " - " + Artist)
    f.close()

while(True): #Loops forever, I'll add a graceful exit soon
    time.sleep(5)       #Checks every 5 seconds, there's probably a better way to check if a song ended but this works.
    UpdateArtistSong()  #Runs the function to update the .txt
