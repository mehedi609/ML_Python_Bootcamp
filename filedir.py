import os
from pathlib import Path

rootDir = "E:\\Machine Learning n Data Science\\.Jose Portilla\\Python for Data Science and Machine Learning Bootcamp"

for dirName, subdirList, fileList in os.walk(rootDir):
    # print('Found directory: %s' % dirName)
    directory_path = Path(dirName)
    # print(d)
    for each_file_path in directory_path.glob('*.vtt'):
        # print(f'removing {each_file_path}')
        each_file_path.unlink()

    for each_file_path in directory_path.glob('*.srt'):
        # print(f'removing {each_file_path}')
        each_file_path.unlink()
print("=="*30)
print('Done!!!')
