from smartup.smartdance import dance

def hey():
  return f'Hello'

name = "Marcelo"
country = "Chile"

# Output: Hello Marcelo from Chile
print(dance("{{hey()}} {{name}} from {{country}}", locals()))
