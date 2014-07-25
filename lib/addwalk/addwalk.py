# -*- coding: utf-8 -*-
import base64
import urllib, urllib2
import json

class Addwalk(object):
  api_host_url = None
  api_key = None
  api_secret = None
  access_token = None


  def __init__(self, api_host_url = None, api_key = None, api_secret = None):
  
    super(Addwalk, self).__init__()
    self.api_host_url = api_host_url
    self.api_key = api_key
    self.api_secret = api_secret
    try:
      token_credential = urllib.quote(api_key) + ':' + urllib.quote(api_secret)
      credential = 'Basic ' + base64.b64encode(token_credential)

      value = {'grant_type': 'client_credentials'}
      data = urllib.urlencode(value)
      
      auth_url = '%s/oauth/token'%self.api_host_url
      req = urllib2.Request(auth_url)
      req.add_header('Authorization', credential)
      req.add_header('Content-Type', 'application/x-www-form-urlencoded;charset=UTF-8')

      response = urllib2.urlopen(req, data)
      json_response = json.loads(response.read())
      self.access_token = json_response['access_token']
    except Exception, e:
      raise e


  def sendRequest(self, url, http_method='GET', params=None, headers=None):
    data = None
    if params:
      data = urllib.urlencode(params)
    if http_method == 'POST':
      req = urllib2.Request(url, data)
    else: 
      req = urllib2.Request(url+'?'+data)

    req.add_header('Authorization', 'Bearer ' + self.access_token)
    if headers:
      for (k,v) in headers.items():
        req.add_header(k,v)

    response = urllib2.urlopen(req)
    json_response = json.loads(response.read())
    json_str = json.dumps(json_response)
    return json_str