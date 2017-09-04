import pandas as pd

crawldf = pd.read_csv('crawlerror.csv')  #create crawl error file from whatever service you have. Mine came from GWT.
tempfile = open('apache_redirect.txt','w')

for item in crawldf['URL']:

    if item.strip('http://your_target_URL'):
        pass
    else:
        tempfile.write('Redirect 301 ' + '/' + item.strip('http://target_URL.com') +  ' http://www.target_URL.com\n')

tempfile.close()
