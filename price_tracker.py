import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Enter the url of the item you want to track for

item_url = input("Enter the url")
URL = item_url

# Enter the user agent to let the servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent.
# You can find user agent by going to:
 # 1. Go to google.com and search for my user agent
 # 2. Copy the user agent in the input box

user_agent_info = input("Enter the user agent")


headers = {'User-Agent': user_agent_info}

def check_price():
    
    # To fetch the page details of the item.

    page = requests.get(URL, headers=headers)

    # To fetch it in a neat way using beautifulsoup.

    soup = BeautifulSoup(page.content)

    # You can find the id of the price and the title by copying the price going to view page source in google and do CTRL+F and paste the price in the find box and then the id will be given on the first search item of the span.
    # By default for most of the items it is "priceblock_ourprice"
    
    # title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    # As the price will be a string so convert it into a float value.

    converted_price = float(price[1:6].replace(",",""))


    # Checking the price to send the email when the price of the item drops.

    if(converted_price < 1700):
        send_mail()

    
def send_mail():
    # Using the SMTP to send the mail.

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Type the email and password below.

    sender_email = input("Enter your email.")

    password = input("Enter your password.")
    
    server.login(sender_email, password)
    
    subject = "Price fell down!"

    body = 'Check the amazon link -> (and give the url of the item here to redirect directly to the item page)'
    
    msg = f"Subject: {subject}\n\n{body}"

    # You can give the same email id.

    receiver_email = input("Enter the email id where you want to recieve the email when the price drops")

    
    server.sendmail(
        sender_email,
        receiver_email,
        msg
    )
    print("Hey email has been sent")
    server.quit()

# You can use the below loop when you want to check the price and send email daily. 

#while(True):
check_price()
    #time.sleep(60*60)