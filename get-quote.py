def Test():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0:2])

if __name__== "__main__":
  Test()
