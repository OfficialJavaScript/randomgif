# Random Gif
This random gif website is programmed in Python using Flask, with the usual HTML And CSS Front end.

Quick warning, if you click links here, they will change to that page (exiting this page) not opening in a new tab, so (CTRL + Left Click) - that will open in a new tab.

# Setup
## Get and add API Key 
1. Go to [Giphy Developers](https://developers.giphy.com/)
2. Press Create an Account (even if you have an account this is where you can log in), and create your account/login
3. After that press Dashboard, or click this [link](https://developers.giphy.com/dashboard)
4. Press Create App
5. Select API, not SDK (Well, it probably doesn't matter, it should work either way)
6. Press next step, here you need to enter your App Name (Doesn't matter what it is), and check the tick box to agree to the [GIPHY API Terms](https://support.giphy.com/hc/en-us/articles/360028134111-GIPHY-API-Terms-of-Service)
7. Now select and copy your API key (You can double click it, this will copy to your Clipboard.)
8. Now make sure you have downloaded the file, Windows, Linux, or Mac - (<> Code) -> Download ZIP, Linux via terminal - `git clone https://github.com/OfficialJavaScript/randomgif.git`
9. Unzip this folder however you usually do it, else google it 😂
10. Next Open apikey.txt in a text editor, select everything (with CTRL + A ("CONTROL A")) and paste your API Key in. Warning, make sure that it's the only thing there, no spaces, no new lines, no nothing, else it will trip the error prevention.

## Setup App
1. Make sure you have Python3 installed, I'm not going to give instructions for that here, Google it. To check just run `python3 -h` in a terminal (Next step will show you how to open a terminal if you don't know how to)
2. Open a terminal in the folder, On Windows: Click the NAV bar (next to the search bar) and type PowerShell or CMD, Linux - You should know this, if not google it, Mac - You are gonna have to google it sorry 😂
3. Run `pip install -r requirements.txt`
4. Now run the file, either double-click it or run `python3 main.py` this should star the program, and look something like this:
![image](https://github.com/OfficialJavaScript/randomgif/assets/51689500/87dc7bc1-bafd-4222-9f06-937637a72027)
5. Open http://localhost/ in your browser, that should work, for any reason it doesn't go to the third ip mentioned in your terminal.
6. And your all set to go! - If you get a error about API key try the get and add API key steps again, else open a issue about it and I'll see what I can do (DON'T INCLUDE YOUR API KEY IN THERE - IT'S PRIVATE)

# What API is this built of? 

This uses the [Giphy API](https://developers.giphy.com/)

