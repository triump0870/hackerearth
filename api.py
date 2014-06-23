import urllib
import urllib2
import json

COMPILE_URL = 'http://api.hackerearth.com/code/compile/'
RUN_URL = 'http://api.hackerearth.com/code/run/'

class HackerAPI(object):
    def __init__(self, secret, src, language, pinput=None, tlimit = 5, mlimit = 262144, async = 0):
        self.client_secret = secret
        self.source = src
        self.lang = language
        self.input = pinput
        if tlimit > 5:
            tlimit = 5
        self.time_limit = tlimit
        if mlimit > 262144:
            mlimit = 262144
        self.memory_limit = mlimit
        self.async = async
        self.params = {
            'client_secret' : self.client_secret,
            'source' : self.source,
            'lang' : self.lang,
            'time_limit' : self.time_limit,
            'memory_limit' : self.memory_limit,
            'async' : self.async
            }

    def compile(self):
        data = self.__request(COMPILE_URL, self.params)
        return data

    def run(self):
        data = self.__request(RUN_URL, self.params)
        return data

    def __request(self, url, params):
        try:
            request = urllib2.Request(url, urllib.urlencode(params))
            r = urllib2.urlopen(request)
            response = self.__result(r)
        except urllib2.URLError as e:
            if hasattr(e, 'code') and hasattr(e, 'reasone'):
                response = {'error_code': e.code, 'error_reason':e.reason }
            else:
                response = {'error': e}
        return response

    def __result(self, res):
        result = json.load(res)
        return result