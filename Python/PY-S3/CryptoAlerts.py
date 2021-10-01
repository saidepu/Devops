from coinmarketcap import Market

coinmarketcap = Market()
alllistings = coinmarketcap.listings()
#print(alllistings)
getbtcprice = coinmarketcap.ticker(start=1,limit=1,convert='INR')
#print(getbtcprice)
getpricebyid = coinmarketcap.ticker(1, convert = 'INR')
#print(getpricebyid)
getoverallstats = coinmarketcap.stats(convert = 'INR')
#print(getoverallstats)
