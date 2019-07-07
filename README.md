# pyLDB - Python interface to the Live Departure Boards

[![PyPI](https://img.shields.io/pypi/v/pyldb.svg)](https://pypi.python.org/pypi/pyldb)
[![PyPI](https://img.shields.io/pypi/dm/pyldb.svg)](https://pypi.python.org/pypi/pyldb)
[![PyPI](https://img.shields.io/pypi/l/pyldb.svg)](https://pypi.python.org/pypi/pyldb)
[![Build Status](https://travis-ci.org/jwg4/pyldb.svg?branch=master)](https://travis-ci.org/jwg4/pyldb)

A simple library for getting live departure boards from the National Rail Enquiries Darwin service (via OpenLDBWS). Designed to wrap the SOAP code with a simple interface. Currently a work in progress.

To run this code you will need your own access token which you have to get from National Rail Enquiries.

If you're not in the UK or not interested in train data from the UK, this code probably won't help you.

## Technical
This library relies on two others: suds to do a SOAP call into the LDBWS service, and jinja2 for the HTML templating.

SOAP is a framework for remote APIs, typically over HTTP but other transport layers are supported, which predates REST. It uses XML, and relies on XML documents in a WSDL language to define the specifics of the API, including function signatures and all the custom types used by the API. It's usually a bit more complicated to setup a SOAP connection than to hit a REST api, but the use of strong types can make them very powerful. The code in this library provides a minimal proof of concept of how to retrieve live departure board data from the SOAP service using Python. For some peope that might be all you need.

Due to the choice of a port of suds to Python 3, this library does not currently work at all with Python 2.

Jinja2 is an awesome templating library for Python which is used in Flask and Ansible among many other projects. Its use here is straightforward, and if you look at the basic HTML template, you can probably figure out how to write a template for either a differently structured HTML document, or a different document type altogether.

National Rail Enquiries is a UK organization which provides information about train times and fares on the National Rail system. The Live Departure Board service is a web API which shows trains scheduled to depart from a given station, along with information about their expected departure times, etc. This is the same data, updated live, which is used in mapping apps - since 2015 it is also the same data shown on departure boards in train stations, since these boards also rely on the same API.

## Important
National Rail Enquiries is the data provider for the API which this code wraps. However, this library is not approved, endorsed or supported by National Rail Enquiries. Information about Darwin Data Feeds provided by NRE (of which LDBWS is one) is at [[https://www.nationalrail.co.uk/100296.aspx]].