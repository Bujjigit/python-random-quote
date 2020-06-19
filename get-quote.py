def Test():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  new_quotes=[x[:-1] for x in quotes]
  f.close()

  print(new_quotes[0:2])

if __name__== "__main__":
  Test()
