from threading import Thread
from shutil import move
import gzip


FILE = 'path/to/files/'
WEB = 'path/to/webfiles'
DATA = 'path/to/data'

BACKUP_LOCATIONS = {'files': 'backup/filebackup',
'web': 'backup/webbackup',
'data': 'backup/databackup'
}

def compress(target):
    with open(target, 'rb') as in_file:
        with gzip.open(target + '.gz', 'wb') as out_file:
            out_file.writelines(in_file) 

def do_backup(target, backup_location):
    compress(target)
    backup_file = target + '.gz'
    move(backup_file, backup_location)


if __name__ == '__main__':
    Thread(target = do_backup, args = (FILE, BACKUP_LOCATIONS['files'])).start()
    Thread(target = do_backup, args = (WEB, BACKUP_LOCATIONS['web'])).start()
    Thread(target = do_backup, args = (DATA, BACKUP_LOCATIONS['data'])).start()

