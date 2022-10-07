import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?crid=2EB9ZRCZHFJLY&keywords=playstation+5&qid=1665153432&qu=eyJxc2MiOiIzLjU1IiwicXNhIjoiNC43OCIsInFzcCI6IjQuODUifQ%3D%3D&sprefix=playstation+5%2Caps%2C77&sr=8-1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("£")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# function to check if the price has dropped below 480
def check_price():
  title = soup.find(id="productTitle").get_text()
  price = soup.find(class_="a-offscreen").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
  #print(price)

  #converting the string amount to float
  converted_price = float(price[0:5])
  print(converted_price)
  if(converted_price < 480):
    send_mail()

  #using strip to remove extra spaces in the title
  print(title.strip())

# function that sends an email if the prices fell down

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email@gmail.com', 'password')

    subject = 'Price Fell Down'
    body = "Check the amazon link https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?crid=2EB9ZRCZHFJLY&keywords=playstation%2B5&qid=1665153432&qu=eyJxc2MiOiIzLjU1IiwicXNhIjoiNC43OCIsInFzcCI6IjQuODUifQ%3D%3D&sprefix=playstation%2B5%2Caps%2C77&sr=8-1&th=1 "

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sender@gmail.com',
        'receiver@gmail.com',
        msg
    )
    # print a message to check if the email has been sent
    print('Hey Email has been sent')
    # quit the server
    server.quit()
