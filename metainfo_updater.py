import re
import sys
import shutil


def metainfo2_changer(new_filename, reached_version, filename='metainfo2.txt',):
    counter = 0
    shutil.copy(filename, new_filename)
    with open(filename) as file:
        with open(new_filename, 'a') as updated_file:
            for line in file.readlines():
                _str = re.match(r"^\[.[^DUK]{0,}\\\d{2}\\.{0,}\]$", line)
                if _str:
                    _founded = _str.group(0)
                    _rv = rf'\\{reached_version}\\'
                    _new_version = re.sub(r'\\\d{2}\\', _rv, _founded)
                    new_block = f'\n\r{_founded}\nLink = "{_new_version}"'
                    updated_file.write(new_block)
                    counter+=1
            print("Blocks updated:", counter)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python metainfo_updater.py <outputfilename> <reached HW>")
        exit()

    filename = sys.argv[1]
    reached_version = sys.argv[2]
    metainfo2_changer(filename, reached_version)


