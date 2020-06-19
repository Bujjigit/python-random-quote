def Test():
  #print("Keep it logically awesome.")
  quote = input("Enter new quote: ") 
  f = open("quotes.txt", "a")
  f.write(quote)
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  new_quotes=[x[:-1] for x in quotes]
  f.close()

  print(new_quotes[-1])

if __name__== "__main__":
  Test()
