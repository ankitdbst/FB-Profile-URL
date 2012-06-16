import urllib2, cookielib, re, os, sys
from bs4 import BeautifulSoup

class Facebook():
    def __init__(self, email, password):
        self.email = email
        self.password = password

        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('Referer', 'http://login.facebook.com/login.php'),
                            ('Content-Type', 'application/x-www-form-urlencoded'),
                            ('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729)')]
        self.opener = opener

    def login(self):
        url = 'https://login.facebook.com/login.php?login_attempt=1'
        data = "locale=en_US&non_com_login=&email="+self.email+"&pass="+self.password+"&lsd=20TOl"

        usock = self.opener.open('http://www.facebook.com')
        usock = self.opener.open(url, data)
        a = usock.read()
        if "logout" in a:
            print "Logged into facebook using", self.email
            return a
        else:
            print "failed login"
            sys.exit(1)

    def profile(self, email):
        """
            Scrapes the search page of facebook for the email
            First match or no match
        """
        url = 'http://www.facebook.com/search/results.php?q=' + urllib2.quote(email)
        usock = self.opener.open(url)
        # Reads in the raw html
        html = usock.read()
        # Creates a BS instance with the soup html
        soup = BeautifulSoup(html)
        hidden = soup.find("code")
        # Get the hidden code block containing the profile data
        r = BeautifulSoup(hidden.string)
        # Use the search result first block to get the profile url
        markup =  r.find("div", "instant_search_title")
        if markup == None:
            print "couldn't locate user!"
            sys.exit(1)
        link = markup.find('a', href=True)

        return link['href']
