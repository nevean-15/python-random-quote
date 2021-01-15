def primary():

  nevean = open("quotes.txt")
  quotes = nevean.readlines()
  nevean.close()

  print(quotes[0])

if __name__== "__main__":
 primary()
