import pytest

import os
import sys

import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from poedevtools.trade import PoeTrade
from google.protobuf.json_format import MessageToJson, MessageToDict
import numpy


def test_imports():
    assert True


def test_blank_proto():
    trade_obj = PoeTrade.PoeTrade()

    assert trade_obj.print_query() == None


def test_malformed_search():
    trade_obj = PoeTrade.PoeTrade()

    request = trade_obj.get_query()
    request.query.status.option = "Definitely not online ;)"

    # Expected error
    unknown_status_error = {"error": {"code": 2, "message": "Unknown status type"}}

    assert trade_obj.search(PoeTradeRequest=request) == unknown_status_error


def test_empty_search():
    trade_obj = PoeTrade.PoeTrade()
    trade_obj.reset_query()

    # Expected error
    query_missing_error = {"error": {"code": 2, "message": "Query missing."}}

    assert trade_obj.search(PoeTradeRequest=None) == query_missing_error
    assert trade_obj.search() == query_missing_error


def test_query_datatypes():
    trade_obj = PoeTrade.PoeTrade()

    proto_request = trade_obj.get_query()

    proto_request.query.status.option = "online"
    proto_request.query.sort.price = "asc"
    
    dict_request = {"query":{"sort"{"price":"asc"}, "status": {"option":"online"}}}
    json_request = '{"query":{"status":{"option":"online"}}}'

    proto_response = trade_obj.search(proto_request, num_get=1)
    dict_response = trade_obj.search(dict_request, num_get=1)
    json_response = trade_obj.search(json_request, num_get=1)

    assert (proto_response == dict_response) & (dict_request == json_response) & (json_response == proto_response)
    
dict_request = {"query":{"status":{"option":"online"}}}
print(trade_obj.search(dict_request, num_get=1))
trade_obj = PoeTrade.PoeTrade()

proto_request = trade_obj.get_query()

proto_request.query.status.option = "online"



print(proto_request)