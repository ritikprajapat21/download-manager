#! /usr/bin/python3
import os
import shutil

path = '/home/ritik/Downloads'

audio_format = ['.mp3', '.m4a', '.wac', '.aac', '.wma']
text_format = ['.txt', '.doc', '.docx', '.pdf', '.md', '.json', '.csv', '.xls', '.xlsx', '.pptx']
image_format = ['.jpeg', '.jpg', '.png', '.wpeg', '.gif', '.tiff', '.bmp', '.svg']
compressed_format = ['.zip', '.7z', '.tar', '.gzip', '.rar', '.apk', '.deb', '.appimage']
video_format = ['.mp4', '.mkv', '.mov', '.avi']

def fileExist(file_path):
    return os.path.exists(file_path)

def renameFile(file):
    arr = file.split('.')
    arr[0] += 'new'
    new_name = '.'.join(arr)
    return new_name

for file in os.listdir(path):
    if (os.path.isfile(os.path.join(path, file))):
        destination = './'
        ext = os.path.splitext(file)[1]
        if (ext in audio_format):
            destination = 'audio'
        elif ext in text_format:
            destination = 'text'
        elif ext in image_format:
            destination = 'image'
        elif ext in compressed_format:
            destination = 'compressed'
        elif ext in video_format:
            destination = 'video'
        else:
            destination = 'other'

        destination_path = os.path.join(path, destination)
        source_file_path = os.path.join(path, file)
        destination_file_path = os.path.join(destination_path, file)

        if (fileExist(destination_file_path)):
            file = renameFile(file)
            destination_file_path = os.path.join(destination_path, file)

        if not os.path.exists(destination_path):
            os.mkdir(destination_path)

        shutil.move(source_file_path, destination_file_path)
