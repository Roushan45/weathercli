import click
#from .requestHandler import getData
import json
import requestHandler

def m1(opt):
    print('a : '+str(opt))

def m2(opt):
    print('b : '+str(opt))

def m3(opt):
    print('c : '+str(opt))
choices=[1,5,8]
units=['metric','impulse']
@click.command()
@click.option('--countrycode','-t',help='code of the country')
@click.option('--cityname','-c',help='name of the city')
@click.option('--cityzipcode','-z',help=('zip code of the city'))
@click.option("--unit",'-u',type=click.Choice(units),
                help="by default kelvin for celcius metric and for fahrenhit use impulse")
def main(countrycode,cityname,cityzipcode,unit):
    """
    demo of click command
    """
    res=requestHandler.getData(countrycode,cityname,cityzipcode,unit).json()
    viewData(res)

def viewData(data):
    click.secho("view : " + data['weather'][0]['description'])
    click.secho("Current Temp : "+str(data['main']['temp']-273.15))
    click.secho("Max Temp : "+str(data['main']['temp_max']-273.15))
    click.secho("Min Temp : "+str(data['main']['temp_min']-273.15))
if __name__=="__main__":
    main()
        