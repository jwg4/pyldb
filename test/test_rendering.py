from unittest import TestCase

import requests

from pyldb import render_board


class TestHTMLOutput(TestCase):
    def validate(self, html):
        self.assertIsNotNone(html)

        r = requests.post(
            'https://validator.w3.org/nu/',
            data=html,
            params={'out': 'json'},
            headers={'Content-Type': 'text/html; charset=UTF-8'}
        )
        result = r.json()
        messages = result['messages']
        errors = [ m for m in messages if m['type'] == 'error' ]
        self.assertListEqual([], errors)


class TestRender(TestHTMLOutput):
    class StationBoardStub(object):
        crs = "CLJ"
        locationName = "Clapham Junction"
        generatedAt = "2020-04-18T02:33:50.6760206+01:00"

    def test_render_board_without_trains(self):
        data = b'<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><GetDepartureBoardResponse xmlns="http://thalesgroup.com/RTTI/2017-10-01/ldb/"><GetStationBoardResult xmlns:lt="http://thalesgroup.com/RTTI/2012-01-13/ldb/types" xmlns:lt6="http://thalesgroup.com/RTTI/2017-02-02/ldb/types" xmlns:lt7="http://thalesgroup.com/RTTI/2017-10-01/ldb/types" xmlns:lt4="http://thalesgroup.com/RTTI/2015-11-27/ldb/types" xmlns:lt5="http://thalesgroup.com/RTTI/2016-02-16/ldb/types" xmlns:lt2="http://thalesgroup.com/RTTI/2014-02-20/ldb/types" xmlns:lt3="http://thalesgroup.com/RTTI/2015-05-14/ldb/types"><lt4:generatedAt>2020-04-18T02:33:50.6760206+01:00</lt4:generatedAt><lt4:locationName>Norwood Junction</lt4:locationName><lt4:crs>NWD</lt4:crs><lt4:nrccMessages><lt:message>Reduced timetable in operation. In line with government advice, you should only be travelling if you are a key worker or it is essential for you to do so. If you must travel, always practice social distancing. More details can be found &lt;A href="http://nationalrail.co.uk/service_disruptions/245388.aspx"&gt;here&lt;/A&gt;.</lt:message><lt:message>Amended trains in the Guildford area. More details can be found &lt;A href="http://nationalrail.co.uk/service_disruptions/240366.aspx"&gt;here&lt;/A&gt;.</lt:message></lt4:nrccMessages><lt4:platformAvailable>true</lt4:platformAvailable></GetStationBoardResult></GetDepartureBoardResponse></soap:Body></soap:Envelope>'
        data = TestRender.StationBoardStub()
        html = render_board(data)
        self.validate(html)
