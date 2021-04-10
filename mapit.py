import webbrowser
import pyperclip

response = input('Introduce una dirección: ')
if response:
    address = response
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/search/' + address)

