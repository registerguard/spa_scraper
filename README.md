Selenium & BeautifulSoup-powered single-page application scraper
===============================

A basic working model of scraping that which doesn't lend itself to scraping, that is, the single-page application sort of page, in this case, a Firebase and ReactJS-powered deal, [http://trialsresults.usatf.org](http://trialsresults.usatf.org), from U.S. Track & Field for the 2016 U.S. Olympic Track & Field Trials held in Eugene, Ore., June 30 - Jul 10.

`usatf.p` is a Python pickled selenium webdriver-generated page for using with `bs.py` to tweak the `BeautifulSoup` munging separately, so you don't have to request and wait the live page every time.

## Installation

A rather bare bones how to makes it work on OS X (10.11.6):  

    1. `$ git clone   git@github.com:registerguard/spa_scraper.git`
    2. `$ cd spa_scraper`  
    3. `$ pip install -r requirements.txt`  
    4. Install geckodriver:  
        * Download   [geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.13.0)  
        * Unzip `tar.gz` file  
        * `$ mv /location/of/unzipped/geckodriver   /usr/local/bin/` or somewhere else on your `$PATH`  
    3. `$ python script.py`  
