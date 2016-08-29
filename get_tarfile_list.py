import tarfile
import time
from sys import version_info


def tarfile_list(tarfile_full_name):
    try:
        # open up the file Read only.
        tarfile_open = tarfile.open(tarfile_full_name, 'r')

        # Format output table
        file_name_width = 80
        time_width = 30
        total_width = 110
        print '=' * total_width
        header_format = '%-*s%*s'
        body_format = '%-*s%*s'
        print header_format % (file_name_width, 'File Name', time_width, 'Modified Time')
        print '-' * total_width

        for member_info in tarfile_open.getmembers():
            # Check if it's a file
            if member_info.isreg():
                print body_format % (file_name_width, member_info.name,  time_width, time.ctime(member_info.mtime))
        print '=' * total_width
    except IOError, err:
        print '%20s %s' % (tarfile_full_name, err)
    finally:
        tarfile_open.close()


if __name__ == '__main__':
    # Check python version whether 2 or 3
    python3 = version_info[0] > 2
    if python3:
        file_location = input("Tar file location: ")
        file_name = input("Tar file name: ")
        tarfile_full_name = file_location + file_name
    else:
        file_location = raw_input("Tar file location: ")
        file_name = raw_input("Tar file name: ")
        tarfile_full_name = file_location + '/' + file_name

    # Function call to open up the tar file (without extracting) and print file names and date
    try:
        if tarfile.is_tarfile(tarfile_full_name):
            tarfile_list(tarfile_full_name)
    except IOError, err:
        print '%20s %s' % (tarfile_full_name, err)