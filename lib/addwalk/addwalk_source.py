from addwalk import Addwalk

class AddwalkSource(Addwalk):
  def __init__(self, api_host_url = None, api_key = None, api_secret = None):
    super(self.__class__, self).__init__(api_host_url, api_key, api_secret)

  def get(self, params):
    print '[AddwalkSource::get]'
    ret = {}
    url = '%s/1/sources.json'%self.api_host_url # hier 1 means API version 1 

    if 'status' in params is False:
      params['status'] = 'all' 
    if 'page' in params is False:
      params['page'] = 1 

    headers = {'Accept':'application/json'}

    ret = self.sendRequest(url, 'GET', params, headers)
    return ret

  def write(self):
    pass

  def create(self):
    pass

  def hoge(self, params): # write??
    pass
