
#!/usr/bin/env python

#import the BeautifulSoup4 and urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


#Parse RSS feed items
def news(xml_news_url):

    parse_xml_url = urlopen(xml_news_url)
    xml_page = parse_xml_url.read()
    parse_xml_url.close()

    soup_page = BeautifulSoup(xml_page, "xml")
    news_list = soup_page.findAll("item")

    for getfeed in news_list:

        print("\n")
        print('\033[1;33m %s \033[1;m' %getfeed.title.text)
        print('\033[1;32m %s \033[1;m' %getfeed.link.text)
        print('\033[1;35m %s \033[1;m' %getfeed.pubDate.text)
        print("\n")


#Add RSS Feed URL
#you can add 'xml' URL here from any websites/blog
NEWS_URL=input("Enter the RSS url of the news outlet or blog you want to see: ")



#now call news function
news(NEWS_URL)

