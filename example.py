#from lib.addwalk.addwalk import Addwalk
from lib.addwalk.addwalk_source import AddwalkSource
import example_conf as conf

if __name__ == '__main__':

  api_host_url = conf.api_host_url
  api_key = conf.api_key
  api_secret = conf.api_secret
  widget_token = conf.widget_token

  # create instance
  addwalkSource = AddwalkSource(api_host_url, api_key, api_secret)

  # get sources
  params = { 
    'token': widget_token, 
    'status':'all',
    'page': 1 } 
  ret = addwalkSource.get(params)
  print ret

  # add tag info(called from visual_technology??)
  params = { 
    'source_id': 1} 
  ret = addwalkSource.hoge(params)
  print ret