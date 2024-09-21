from smartup.smartdance import dance
from smartup import SmartUp

def hey():
  return f'Hello'

name = "Marcelo"
country = "Chile"

# Output: Hello Marcelo from Chile
print(dance("{{hey()}} {{name}} from {{country}}", locals()))

response = SmartUp.chat.create(
    agent="moishele",
    messages=[{
        "role": "user",
        "content": "Hola Moishele, ¿cómo estás?"
    }]
)

# Output (stochastic):
print(response)
# "¡Shalom y un montón de alegrías para ti! Estoy tan bien como un bagel en un brunch dominical 😄."
