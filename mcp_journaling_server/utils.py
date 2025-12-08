from io import SEEK_END
import os
from datetime import date

def get_root_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'journal')

def file_exists(fname):
    return os.path.exists(fname)

def get_content(start_date=None, end_date=None):
    filtered_journals = filter_journals(start_date, end_date)
    content = ''
    for fname in filtered_journals:
        if file_exists(fname):
            with open(fname, 'r') as f:
                content += f.read()
    return content

def write_content(data, date=None):
    if not date:
        journal_date = date.today()
    else:
        journal_date = date
    fname = os.path.join(get_root_dir(), str(journal_date))
    try:
        with open(fname, 'a') as f:
            f.write('\n')
            f.write(data)
            f.write('\n')

        return True
    
    except Exception:
        return False
    
def filter_journals(start_date, end_date):
    all_journals = os.listdir(get_root_dir())
    file_names = []
    for journal_name in all_journals:
        
        file_names.append(os.path.join(get_root_dir(), journal_name))

    return file_names

"""

def get_dates_between(start_date, end_date): 
    if start_date > end_date:
        raise ValueError("start_date cannot be after end_date")

    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date)
        current_date += timedelta(days=1)
    return date_list
"""