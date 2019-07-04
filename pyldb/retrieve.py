from suds import Client

from .details import wsdl_url, service_url


def get_board(crs, token):
    client = Client(wsdl_url, location=service_url)

    access_token = client.factory.create("ns2:AccessToken")
    access_token.TokenValue = token
    client.set_options(soapheaders=access_token)

    service = client.service
    result = service.GetDepartureBoard(20, crs)
    return result
