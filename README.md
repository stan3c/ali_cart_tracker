# ali_cart_tracker

Open a webbrowser. Logon to your ali account first. Make sure webpage is in english, dollars (or any other language, currency, but keep the things consistent each time you save the json data.
I do not know how to logon to ali account from python, hence this step has to be done manually.
Plece the following link in another cart of your webbrowser. The link below placed in your webbrowser will download your ali cart in json format.
Save it from your webbrowser to a local file under a name ali_cart_2020_12_04.json

https://shoppingcart.aliexpress.com/api/1.0/cart/items.do?currentPage=0&uniqueId=10234

Run the script. It will read all files named 'ali_cart_*.json', sort them according to the date in the file name and calculate the average price, the lowest price in the the data.

The script will print the contents of your ali shopping cart on the screen.
nr      Product name                             Current price  Avg price  Min price
1        VANSOALL Video Intercom Wired           47.44   USD     47.44   47.44

Products priced higher than the lowest price ever recorded are printed in black
Products priced at the lowest price ever recorded are printed in red
Products priced lower than the lowest price ever recorded are printed in purple
