<h3 align="center">
  <br>
  <a href="https://github.com/Ongenix/Hypixel-Auctions-Wrapper"><img src="https://github.com/Ongenix/Hypixel-Auctions-Wrapper/blob/main/Hypixel_Auctions_Wrapper.png?raw=true" alt="hypixel auctions wrapper"></a>
  <br>
  A simple to use wrapper for Hypixel built in Python
  <br>
</h3>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a>
</p>

<br><br>

<h1 align="center" id="features">
  Features
</h1>

```python
# Get auction ID's
uuids = x.get_uuid(context=ctx)
# Get auction prices
prices = x.get_prices(context=ctx)
# Get auction names
names = x.get_names(context=ctx, lowercase=True)
# Get auction tiers
tiers = x.get_tiers(context=ctx)
# Check if your item is substandard (cheaper)
substandard = x.substandard_price(context=ctx, item_number=1)
```

<br>

<h1 align="center" id="how-to-use">
  How To Use
  in progress
</h1>

<h1 align="center" id="download">
  Download
</h1>

```bash
# Download the repository
$ git clone https://github.com/Ongenix/Hypixel-Auctions-Wrapper/
# Go into the repository
cd Hypixel-Auctions-Wrapper
# Add enviroment variables
$ export [variable_name]=[variable_value]
# Import the wrapper and run your main file
$ python3 'main.py'
```



