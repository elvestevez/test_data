import pandas as pd
from datetime import datetime, timedelta

def to_csv(center, start, end):
    diff_days = (end - start).days
    list_obj = []
    for hour in range(0, 24 * diff_days):
        dict_obj = {}
        end = start + timedelta(hours=1)
        dict_obj['center'] = center
        dict_obj['start'] = start.isoformat(timespec='milliseconds') + 'Z'
        dict_obj['end'] = end.isoformat(timespec='milliseconds') + 'Z'
        dict_obj['blank'] = None
        start = end 

        list_obj.append(dict_obj)

    df = pd.DataFrame(list_obj)
    
    file = './data_test.csv'
    df.to_csv(file, index=False, header=False)
    
    return file

def main():
    center_str = input('Enter a center: ')
    start_date_str = input('Enter a start date (yyyy-mm-dd): ')
    end_date_str = input('Enter a end date (yyyy-mm-dd): ')

    try:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    except:
        print('error start date')
    else:
        try:
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except:
            print('error end date')
        else:
            file = to_csv(center_str, start_date, end_date)
            print(f'{file} is saved')


if __name__ == '__main__':
    main()
