import datetime
import requests
now = datetime.datetime.now()

class mtdapi:
    
    # setup (https://developer.cumtd.com/)

    def __init__(self, api, version='2.2', form='json'):
        self.api = str(api)
        self.version = '2.2'
        self.form = 'json'
        self.main = "https://developer.cumtd.com/api/v" + self.version + '/' + self.form + '/'
        self.date = now.strftime("%Y-%m-%d")
    
    

    # request info

    def request_info(self, url, changeset_id):
        if changeset_id is not None:
            url = url + "&changeset_id=" + str(changeset_id)
        info = requests.get(url).json()
        status = info['status']
        if (status['code'] == 200) & (changeset_id is None):
            return info
        else:
            return status['msg']



    # validate date format
    def validate_date_format(self, date):
        try:
            datetime.datetime.strptime(str(date), '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    


    # Get Calendar date by date
    # https://developer.cumtd.com/documentation/v2.2/method/getcalendardatesbydate/

    def get_calendar_dates_by_date(self, date=now.strftime("%Y-%m-%d")
, changeset_id=None):
        self.validate_date_format(date) 
        url = self.main + 'getcalendardatesbydate?key=' + self.api + '&date=' + str(date) 
        dat = self.request_info(url, changeset_id)
        return dat
    


    # Get Calendar Dates By Service
    # https://developer.cumtd.com/documentation/v2.2/method/getcalendardatesbyservice/
    def get_calendar_dates_by_service(self, service_id="I1%20MF", changeset_id=None):
        if "%20" not in service_id:
            raise ValueError("Remember to replace space with '%20' e.g. trip id 'I1 MF' should be 'I1%20MF'")
        url = self.main + 'getcalendardatesbyservice?key=' + self.api + '&service_id=' + service_id
        dat = self.request_info(url, changeset_id)
        return dat
    
    
    
    # Get departure by stop










api = 
mtd = mtdapi(api)
a = mtd.get_calendar_dates_by_service()
print(a)
##########################
#          test          #
##########################


        
