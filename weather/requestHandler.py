import endpoints
import click
import requests

headers={"Content-Type":"application/json","Accept":"application/json"}
def _get(url,param,headers=headers):
    print("url "+url)
    res=requests.get(url,params=param,headers=headers)
    print(res.url)
    if res.status_code == requests.codes.ok:
        print('status ok')
        return res

    if res.status_code == requests.codes.bad:
        raise(Exception('check params'))

    if res.status_code == requests.codes.too_many_requests:
        raise Exception('You have exceeded your allowed requests per minute/day')


def getData(countrycode,cityname,zipcode,unit):
    BASE_URL=endpoints.BASE_URL
    url=''
    if  cityname and zipcode:
        click.secho('please provide either city name and country code or zipcode and country code',
         fg="red", bold=True)
        exit(0) 

    if not countrycode :
        click.secho("please provide the country code",fg='red',bold=True)

    if zipcode:
        #url="{}/data/2.5/weather?zip={},{}".format(BASE_URL,zipcode,countrycode)
        url="{}/data/2.5/weather".format(BASE_URL)
        params={'zip':"{},{}".format(zipcode,countrycode),'APPID':endpoints.APPID}
        if unit:
            params['units']=unit
        return _get(url,params)
    if cityname:
        url="{}/data/2.5/weather".format(BASE_URL)
        params={'q':"{},{}".format(cityname,countrycode),'APPID':endpoints.APPID}
        if unit:
            params['units']=unit
        return _get(url,params)

