def bank():
  Greetings = input("Greetings ").strip().lower()
  if Greetings.startswith("hello"):
    return 0
  elif Greetings.startswith("h"):
    return 20
  else:
    return 100

for i in range(50):
  print("$",bank())