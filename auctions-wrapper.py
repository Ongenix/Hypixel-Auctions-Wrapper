import requests # I'll make this more explicit later.
from json import loads

class Hypixel:
  def __init__(self, api_key: (str | None), uuid: (str | None)):
    self.api_key = api_key
    self.uuid = uuid
    
    self.auctions_url = f'https://api.hypixel.net/skyblock/auctions?key={api_key}&uuid=uuid'

  def get_auctions(self, item_name, allow_bin, allow_auctions, allowed_tier):
    global allow_bin_pass
    global allow_auctions_pass
    global allowed_tier_pass
    
    allow_bin_pass = allow_bin
    allow_auctions_pass = allow_auctions
    allowed_tier_pass = allowed_tier
    
    def actual_decorator(func):
      data = requests.get(url=self.auctions_url)
      new_data = []

      if data and data.status_code == 200:
        data = loads(data.text)
        
        if data and data.get('auctions'):
          data = data.get('auctions')

          for i in data:
            if type(i) == dict:
              found_name = i.get('item_name')
              found_bin = i.get('bin')

              if found_name and item_name in found_name.lower() or item_name == 'all':
                if (found_bin is False and allow_auctions_pass) or (found_bin and allow_bin_pass):
                  if allowed_tier_pass == i.get('tier') or allowed_tier_pass == 'all':
                    new_data.append(i)
      else:
        match data.status_code:
          case 400:
            new_data = '400 - Data is missing'
          case 403:
            new_data = '403 - Access is forbidden, did you input correct API key?'
          case 429:
            new_data = '429 - Request limit has been reached, try again in a few minutes.'

      func(new_data)
      
    return actual_decorator

  def get_uuid(self, context):
    uuids = []
    
    for i, value in enumerate(context):
      if value.get('uuid'):
        uuids.append(value.get('uuid'))
    return uuids

  def get_prices(self, context):
    prices = []

    for i, value in enumerate(context):
      if value.get('bin') is False:
        prices.append(value.get('highest_bid_amount'))
      else:
        prices.append(value.get('starting_bid'))
    return prices

  def get_names(self, context, lowercase: bool):
    names = []

    for i, value in enumerate(context):
      name = value.get('item_name')
      if name:
        if lowercase:
          names.append(name.lower())
        else:
          names.append(name)
    return names

  def get_tiers(self, context):
    tiers = []
    
    for i, value in enumerate(context):
      if value.get('tier'):
        tiers.append(value.get('tier'))
    return tiers

  def substandard_price(self, context, item_number):
    prices = Hypixel.get_prices(self=self, context=context)
    item = prices[item_number]
  
    del prices[item_number]
    price_mean = int(sum(prices))
    
    if price_mean != 0 and len(prices) != 0 and price_mean / len(prices) > int(item):
      return True
    return False
