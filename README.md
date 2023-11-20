# wallpaper_changer_the_great
## Purpose
This app is a security app which should inform You if someone tried to logg into your computer and failed in this. This programm also edits your wallpaper
## Installation and preparations
At first you should make a directory in which You will collect your wallpapers. After download You have to change path_to_dir in Wall class to path to directory which
You made being wallpapers folder. The same You should do with path_to_txt_logs_dir in Analise class.
You should also change marked places in Email class with Your personal data (as commants says).

The next step is You should make a .exe file using "one file" option in autopytoexe and add it to autostart.
### If You are not an administrator, program will not be working properly!
### This app works only on Windows!

## Usage
When You run Your computer, app should start automatically. It analyse window's security logs so after start it will ask You if it can run powershell as an administrator.
This programm automatically checks if You have internet connection so don't close it. It will close itself. If it detects failed logging attempt, email will be send
to given by You email addres.

## Lincense
It is an open source project :)
You can run it, edit and whatever You want (but please don't use it in non-ethical ways)
