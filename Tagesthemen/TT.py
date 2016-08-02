#!/usr/bin/python3.5
import codecs
import re
import subprocess
import urllib.request
#import os
#import platform

VLC_WIN_PATH = "C:\\Program Files (x86)\\VideoLAN\\VLC\\"
VLC_WIN_CMD = 'vlc.exe %s'
BASE_URL = "http://www.tagesschau.de/sendung/tagesthemen/index.html"
SEARCH_PATTERN = '<a\shref=\"(.*)\">HD.\(h264'
DESC = "Tagesthemen"

def readHtmlFile():
    filename = "snippet.txt"
    file_stream = codecs.open(filename, "r", "utf-8")
    #lines = file_stream.read().replace('\n', '')
    lines = file_stream.read()
    file_stream.close()
    return lines

def writeM3U(name, url):
    print("test_ " + name)
    print("test_ " + url)
    filename = name + ".m3u"
    file = codecs.open(filename, "w", "utf-8")
    file.write("#EXTM3U\n")
    line = "#EXTINF:-1,DE: " + name + "\n"
    file.write(line)
    file.write(url)
    file.close()

def getHtml(url):
    html = urllib.request.urlopen(url).read().decode("utf-8")
    return html

def findString(lines, pattern):
    p = re.compile(pattern)
    m = p.search(lines)
    if m:
        return m.group(1)
    else:
        print('No match')

def windowsStartVlc(videoUrl):
    print ("VideoLink: " + videoUrl)
    buildCmd = VLC_WIN_PATH + VLC_WIN_CMD%(videoUrl)
    print ("cmd: " + buildCmd)
    subprocess.call(buildCmd)
    
    
#html = readHtmlFile()
html = getHtml(BASE_URL)       
videoUrl = findString(html, SEARCH_PATTERN)
#windowsStartVlc(videoUrl)
writeM3U (DESC, videoUrl)
