from io import SEEK_END
import os
from datetime import date

def get_root_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'journal')

def file_exists(fname):
    return os.path.exists(fname)

def get_content(filter=None):
    filtered_journals = filter_journals()
    content = ''
    for fname in filtered_journals:
        if file_exists(fname):
            with open(fname, 'r') as f:
                content += f.read()
    return content

def write_content(data):
    current_date = date.today()
    fname = os.path.join(get_root_dir(), str(current_date))
    try:
        with open(fname, 'a') as f:
            f.write('\n')
            f.write(data)
            f.write('\n')

        return True
    
    except Exception:
        return False
    
def filter_journals():
    all_journals = os.listdir(get_root_dir())
    file_names = []
    for journal_name in all_journals:
        file_names.append(os.path.join(get_root_dir(), journal_name))

    return file_names