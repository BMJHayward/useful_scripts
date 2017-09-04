import datetime
import os
import shutil
import gzip

GOOGLE_DRIVE_DIRECTORY = 'C:/Users/username/Google Drive/'
MAIN_BACKUP_DIRECTORY = 'C:/Users/username/Desktop/_Backups/md_backup_{0}'
EXTERNAL_DRIVE_DIRECTORY = 'F:/My Files/_Backups/md_backup_{0}'

def compress(target):
    with open(target, 'rb') as in_file:
        with gzip.open(target + '.gz', 'wb') as out_file:
            out_file.writelines(in_file)

def get_backup_directory(base_directory):
    date = str(datetime.datetime.now())[:16]
    date = date.replace(' ', '_').replace(':', '')
    return base_directory.format(date)

def copy_files(directory):
    for file in os.listdir(GOOGLE_DRIVE_DIRECTORY):
        file_path = os.path.join(GOOGLE_DRIVE_DIRECTORY, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, directory)

def perform_backup(base_directory):
    backup_directory = get_backup_directory(base_directory)
    os.makedirs(backup_directory)
    copy_files(backup_directory)

def main():
    perform_backup(MAIN_BACKUP_DIRECTORY)
    perform_backup(EXTERNAL_DRIVE_DIRECTORY)

if __name__ == '__main__':
    main()