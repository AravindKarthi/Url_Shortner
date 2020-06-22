#URL SHORTNER VIA COMMAND PROMPT#
import pyshorteners

link=input("Enter the url ")
shortener=pyshorteners.Shortener()
x=shortener.tinyurl.short(link)
print("Your Shornter url", x)
