import requests
import socketserver
import socket
import http
import json
import bilibili.community.service.dm.v1_pb2 as Danmaku
from http.server import BaseHTTPRequestHandler, HTTPServer
import google.protobuf.text_format as tf
import google.protobuf.json_format as jf
import urllib

DM_URL = 'https://api.bilibili.com/x/v2/dm/web/seg.so'
CID_URL = 'https://api.bilibili.com/x/web-interface/view'
SEARCH_URL = 'https://api.bilibili.com/x/web-interface/search/all/v2'

PORT_NUMBER = 80


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        response = self.request_parser()
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Type", "json")
        self.end_headers()
        self.wfile.write(response)

    def request_parser(self):
        path = self.path
        print(path)
        query = urllib.parse.urlparse(path)
        print(query)
        params = dict(urllib.parse.parse_qsl(query.query))
        if 'search' in params.keys():
            return self.search_request(params)
        elif 'bvid' in params.keys():
            return self.danmaku_request(params)
        else:
            return b''

    @staticmethod
    def search_request(params):
        response = search_keyword(params['search'])
        print(response)
        return response

    @staticmethod
    def danmaku_request(params):
        cid = fetch_cid(params['bvid'])
        danmaku_data = fetch_danmaku(cid, params['segment'])
        return jf.MessageToJson(danmaku_data).encode('utf-8')


def str_processing(danmaku_str: str):
    content = danmaku_str.split('\n')


def search_keyword(keyword):
    params = {
        'keyword': keyword
    }
    req = requests.get(SEARCH_URL, params)
    data = req.content
    return data


def fetch_cid(bvID):
    cid_params = {
        'bvid': bvID
    }
    req = requests.get(CID_URL, cid_params)
    data = json.loads(req.content)
    return data['data']['cid']


def fetch_danmaku(cid, segment_index):
    params = {
        'type': 1,
        'oid': cid,
        'segment_index': segment_index,
    }
    req = requests.get(DM_URL, params)
    data = req.content

    danmaku_segment = Danmaku.DmSegMobileReply()
    danmaku_segment.ParseFromString(data)

    # print(tf.MessageToString(danmaku_segment, as_utf8=True))
    try:
        print(tf.MessageToString(danmaku_segment.elems[0], as_utf8=True))
    except IndexError as err:
        print("Out of segment", segment_index)
    return danmaku_segment


if __name__ == "__main__":
    http_server = HTTPServer(('', PORT_NUMBER), MyHandler)
    http_server.serve_forever()

# bvid = input()
# cid = fetch_cid(bvid)
# d1 = fetch_danmaku(cid, 1)



