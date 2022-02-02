How to Find the Next Big NFT Drop on Polygon?
============

As NFTs have taken off on mainnet Ethereum in the past year, many projects have also turned to Layer 2 solutions, like Polygon, for its low transaction costs and faster confirmation times. In turn, NFT marketplaces like OpenSea have reported tremendous growth in their Polygon NFT trading volume. With so many new projects on Polygon, it can often be difficult to cut through the noise and know which up-and-coming NFTs are most popular.

With Alchemy Transfers API on Polygon, we can easily find NFT mints and build wallet-specific trading tools.

In this tutorial, we’ll look at an example of how, with just a few lines of code, your dApp can integrate the 🔋 power of Alchemy Transfers.
***
For ease of user experience, we configured this particular tutorial to run on Heroku, but you are more than welcome to use other service providers!
***

### Problem Statement:  ###

Many NFT collectors want to be notified whenever notable NFT collectors mint an NFT from a new project so that they can also mint or buy into the same collection. Traditionally, building historical queries into dApps have traditionally been complicated and time-consuming. This feature normally requires developers to spin up, manage, and index across their own nodes to build databases. However, with the Alchemy Transfers API on Polygon, we can now search and look up historical wallet activity without a hassle.

In our example dashboard, we’ll be using the Transfers API to create a simple Heroku dashboard that tracks the Polygon minting activity of NFT collector Cozomo de’ Medici who is rumored to be none other than Snoop Dogg himself!

The Heroku dashboard that we create performs two main functions. Upon refreshing the page or whenever the user clicks “Refresh”, the webapp fires off a request to Alchemy to query for the latest ERC721 mints. After receiving the response, the dashboard parses the JSON object and pushes the information to the frontend.

### 🚀 Launching with Heroku ###

 1. Get the repo!

      * `git clone https://github.com/alchemyplatform/polygon-nft-finder.git`

For all Heroku dependent documentation, refer to:
https://devcenter.heroku.com/articles/getting-started-with-nodejs?singlepage=true
for more detailed instructions.  The Heroku instructions included below are abridged.

 2. Install Heroku-CLI and verify/install dependencies.

      * Download Heroku-CLI based on your OS [https://devcenter.heroku.com/articles/heroku-cli]
      * After installation, open your terminal and run `heroku login`; follow the commands that follow to login to your Heroku account.  If you don't have a Heroku account, you can [sign up for one](https://dashboard.heroku.com/apps)!
      * Run `node --version`.  You may have any version of Node greater than 10.  If you don’t have it or have an older version, install a more recent version of Node.
      * Run `npm --version`.  `npm` is installed with Node, so check that it’s there. If you don’t have it, install a more recent version of Node:
      * Run `git --version`   Check to make sure you have git installed.  

 3. Initiate Heroku.

      * Run `heroku create` to create your heroku app. Take note of the info that pops up in the terminal, especially the URL that looks like  http://xxxxxxxxx.herokuapp.com/ That's the URL for your dashboard!

 3. Add in your Alchemy API Key.

      > Change the Alchemy API Key in `main.py` to reflect your particular Alchemy auth token!

![keyß](/alchemy_key.png)

Don't forget to sign into your Alchemy account to use the Transfers API.  See https://docs.alchemy.com/alchemy/documentation/apis/enhanced-apis/transfers-api for more specific documentation.  

If you don’t already have an Alchemy account, [you’ll first need to create one](https://alchemy.com/?r=affiliate:ba2189be-b27d-4ce9-9d52-78ce131fdc2d). The free version will work fine for getting started.  First, we create an App for our Dashboard by clicking “Create App” under the Apps dropdown menu.

![create_app](/create_app.png)

Once we have created the app and pointed it towards the appropriate network, we're ready to go and can paste in our key.

 4. Deploy Heroku.

      * Run `git add .`
      * Run `git commit -m "added Alchemy keys"`
      * Run `git push heroku master` to push and deploy your heroku app.
 
 Your site should look like this! 
 
 ![app](/nft-finder-background.png)

🎉 Congratulations on your dApp deployment! Feel free to edit your app, change its behavior, or make the frontend more spiffy!
