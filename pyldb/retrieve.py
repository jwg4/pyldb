from zeep import Client

from credentials import token


def get_board(crs, token):
    client = Client("https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2017-10-01")
    result = client.service.GetDepartureBoard(
        20, crs,
        _soapheaders=token
    )
    print(result)