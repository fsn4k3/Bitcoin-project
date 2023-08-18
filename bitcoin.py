investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

#write a function to calculate bitcoin to usd

def bitcoinToUSD(bitcoin_amount, bitcoin_to_usd ):
  usd_value = bitcoin_amount * bitcoin_to_usd
  return usd_value

investment_in_usd = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)
if investment_in_usd <= 40000:
  print("Investment below $30,000! SELL!")
else:
  print("Investment above $30,000")