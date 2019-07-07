from suds import Client

from .details import wsdl_url, service_url


def get_board(crs, token):
    """
        Get a live departure board from the LDBWS service.
        The data shows the next 20 trains currently scheduled
        to leave from that station. The data should match
        that shown on the real-life departure boards in the station
        and in mapping apps, etc.

         - crs: a three-letter token identifying a UK station.
                You can find out the CRS of a station at
                http://www.nationalrail.co.uk/stations_destinations/48541.aspx
         - token: An API access token.
    """
    client = Client(wsdl_url, location=service_url)

    access_token = client.factory.create("ns2:AccessToken")
    access_token.TokenValue = token
    client.set_options(soapheaders=access_token)

    service = client.service
    result = service.GetDepartureBoard(20, crs)
    return result
