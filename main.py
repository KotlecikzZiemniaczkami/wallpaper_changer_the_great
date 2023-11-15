import time
import os
import datetime
import ctypes
import subprocess


# class which has to analyse logs
class Analise:
    def __init__(self):
        self.__path_to_txt_logs_dir = "D:\\odczytane_logi"
        self.__name_log_txt = "myLogs.txt"
        self.__command = 'Get-WinEvent -LogName Security | Select-Object -First 100 > ' + self.__path_to_txt_logs_dir + '\\' + self.__name_log_txt

    # method which will be reading security logs and rewriting first 100 to name_log_txt file using command artifact
    # located in path_to_txt_logs_dir
    def logs_reading(self):
        # powershell command: Get_WinEvent reads logs, Select-Object takes only first 100 and gives it to name_log_txt
        command = self.__command
        # running powershell as administrator and giving it order to execute command
        process = subprocess.Popen(
            ["powershell", "-Command", "Start-Process", "powershell", "-Verb", "RunAs", "-ArgumentList",
             f"'-Command {command}'"], shell=True)
        output, error = process.communicate()

# class which is made for automatic change of wallpaper
class Wall:
    def __init__(self):
        self.__path_to_dir = "D:\\tapety"
        self.__today_num = 0
        self.__file = "Python_wallpaper_officer"
        self.__files_in_folder = os.listdir(self.__path_to_dir)
        self.__next = 0
        self.__new_wallpaper = ''
        self.__continue = 1

    # method which is made read txt file with current data (or to make such file if it doesn't exist
    def __reading_the_day(self):
        try:
            file = open(self.__path_to_dir + '\\' + self.__file + '.txt', 'r')
            file_date = file.read()
            file.close()
            date = datetime.datetime.now().date()
            cur_date = str(date)
            if file_date == cur_date:
                self.__continue = 0
            else:
                self.__next = (int(date.strftime("%d")) + int(date.strftime("%m"))) % len(self.__files_in_folder)
                if self.__next >= len(self.__files_in_folder) - 1:
                    self.__next -= 1
                file = open(self.__path_to_dir + '\\' + self.__file + '.txt', 'w')
                file.write(cur_date)
                file.close()
                return 1
        except FileNotFoundError:
            cur_date = str(datetime.datetime.now().date())
            file = open(self.__path_to_dir + '\\' + self.__file + '.txt', 'w')
            file.write(cur_date)
            file.close()
            self.__continue = 0

    # method which is checking the type of given file
    # it returns the .type_name (.jpg or anything)
    def __check_the_type(self, file_name: str):
        type_name = ''
        for i in range(len(file_name) - 1, 0, -1):
            if file_name[i] == '.':
                type_name = '.' + type_name
                break
            type_name = file_name[i] + type_name
        return type_name

    # it sorts files_in_folder list
    def __sorting(self):
        types = {}
        names = []
        typo = ''
        for i in self.__files_in_folder:
            typo = self.__check_the_type(i)
            if typo == '.txt':
                continue
            i = int(i[:i.index('.')])
            types[i] = typo
            names.append(i)
        names.sort()
        for i in range(len(names)):
            names[i] = str(names[i]) + types[names[i]]
        names.append(self.__file + '.txt')
        self.__files_in_folder = names

    # method checking if names in folder are correct and correcting them if one is not
    def __correctance(self):
        guard = 0
        self.__sorting()
        for i in range(len(self.__files_in_folder)):
            if (self.__files_in_folder[i] == self.__file + '.txt') or guard == 1:
                guard = 0
                continue
            try:
                os.rename(self.__path_to_dir + '\\' + self.__files_in_folder[i],
                          self.__path_to_dir + '\\' + str(i) + self.__check_the_type(self.__files_in_folder[i]))
            except FileExistsError:
                if self.__files_in_folder[i] == self.__file + '.txt':
                    continue
                os.rename(self.__path_to_dir + '\\' + self.__files_in_folder[i+1],
                          self.__path_to_dir + '\\' + str(i) + self.__check_the_type(self.__files_in_folder[i + 1]))
                os.rename(self.__path_to_dir + '\\' + self.__files_in_folder[i],
                          self.__path_to_dir + '\\' + str(i) + self.__check_the_type(self.__files_in_folder[i + 1]))
                guard = 1

    # method which is reading files from directory and makes decision which wallpaper will be chosen today
    def __check_the_folder(self):
        self.__reading_the_day()
        if not self.__continue:
            return
        self.__correctance()
        folder_length = len(self.__files_in_folder)
        helper_paper = ''
        self.__new_wallpaper = str(self.__next)
        for i in range(folder_length):
            if self.__new_wallpaper in self.__files_in_folder[i]:
                self.__new_wallpaper = self.__new_wallpaper + self.__check_the_type(self.__files_in_folder[i])
                break

    # main method of this class
    def change_wallpaper(self):
        self.__check_the_folder()
        if not self.__continue:
            return
        self.__new_wallpaper = self.__path_to_dir + '\\' + self.__new_wallpaper
        self.__new_wallpaper = str(self.__new_wallpaper)

        # to keep wallpaper after restart last argument have to be one
        ctypes.windll.user32.SystemParametersInfoW(20, 0, self.__new_wallpaper, 0)

#oWall = Wall()
oAnalise = Analise()
while(1):
    #oWall.change_wallpaper()
    oAnalise.logs_reading()
    time.sleep(10)
