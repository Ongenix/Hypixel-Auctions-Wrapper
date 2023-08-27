from functions import Hypixel
from os import getenv

def main():
  hy = Hypixel(api_key=getenv('KEY'), uuid=getenv('UUID'))
  # This initializes the Hypixel api with your api key and Minecraft UUID.

  @hy.get_auctions(item_name='goblin', allow_bin=True, allow_auctions=True, allowed_tier='all') # You can provide search choices here.
  def auctions(ctx):
    uuids = x.get_uuid(context=ctx) # Gets the auction id. You can view it with /viewauction [uuid]
    print(uuids)
    prices = x.get_prices(context=ctx) # Gets the starting price if its a BIN, or the highest price if it's a auction.
    print(prices)
    names = x.get_names(context=ctx, lowercase=True) # Lowercase will automatically convert the name to lowercase
    print(names)
    tiers = x.get_tiers(context=ctx) # Simply gets the tier (Common, Uncommon, etc.)
    print(tiers)

    for i in range(len(prices)):
      substandard = x.substandard_price(context=ctx, item_number=i) # This checks if the price is lower then average (substandard)
      if prices[i] < 100000:
        print(f'{names[i]}, ({uuids[i]}) is underpriced: {substandard}. Price: {prices[i]:,}')

  

if __name__ == '__main__':
  main()
