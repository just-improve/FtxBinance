import csv
import sys
import time


from ftx_methods import FtxClient
from ftx_wj_methods import FtxClientWJ

class FundingRateChange:
    def get_oi_list(lastopenIterests=float or int, list_of_oi=list, number_elements_in_lists=int):
        # list_of_oi= list_of_oi
        list_of_oi.insert(0, lastopenIterests)
        if len(list_of_oi) > number_elements_in_lists:
            list_of_oi.pop()

    #def mainMethod ():
    year_in_seconds = 31556926
    fifteen_days_in_seconds = 1296000
    ten_days_in_seconds = 864000
    one_day_in_seconds = 86400
    one_hour_in_seconds = 3600
    ten_minutes_in_seconds = 600
    RESOLUTION = {"1m": 60, "5m": 300, "1h": 3600, "1d": 86400, "10d": 864000, "15d": 1296000}
    list_of_oi = []
    list_of_fr = []


