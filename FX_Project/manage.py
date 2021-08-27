#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import pandas as pd
import sqlite3

def get_data():
    usecols = ['forex_id','date','rate']
    forex_quotes = pd.read_csv("../output.csv")

    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    final_list = list(set(usecols) & set(forex_quotes.columns))
    forex_quotes = forex_quotes[final_list]
    # print(type(forex_quotes))
    # forex_quotes.to_sql('api_forex_quotes', conn, if_exists='append', index = False)
    
    conn.commit()
    conn.close()
     


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FX_Project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # get_data()
    main()
