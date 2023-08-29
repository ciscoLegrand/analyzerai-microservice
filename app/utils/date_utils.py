from datetime import date

def quarter_dates(year, quarter):
    if quarter == 1:
        return date(year, 1, 1), date(year, 3, 31)
    elif quarter == 2:
        return date(year, 4, 1), date(year, 6, 30)
    elif quarter == 3:
        return date(year, 7, 1), date(year, 9, 30)
    elif quarter == 4:
        return date(year, 10, 1), date(year, 12, 31)
