"""
Created on Sat Jul  4 14:01:44 2020
@author: Amogh Gupta agupta@gainsight.com
Script was written for learning purposes only.
This script logs into the servers programatically and gets the secure cookies for 
development purpose.
This script is for GS users only.
just configure url,password and username thats it and run it and BOOOOOM!!!:D 
"""

import requests
import json
from bs4 import BeautifulSoup
import re
import urllib.parse as urlparse
from urllib.parse import parse_qs
from urllib.parse import urlsplit


#CONFIGURABLE VARIABLES (url, password and username)

#ENV1
# url = "https://deltadev2-cotephoenix.develgs.com:8463/"
# password= "Gainsight@123"
# username= "cotephoenix@gainsight.com"

#ENV2
url = "https://demo-cotecmt443.develgs.com:9003/"
password= "Gainsight@1991!"
username= "psambaraju@gainsight.com"


#GLOBAL SETTINGS (DO NOT CHANGE- THESE WILL REMAIN UNCHANGED FOR DEV AND DEMO SERVERS)
authClient = 'eyJuYW1lIjoibG9jay5qcyIsInZlcnNpb24iOiIxMS4xLjMiLCJsaWJfdmVyc2lvbiI6IjkuMS4zIn0='
authenicate_url='https://secured.develgs.com/co/authenticate'
authorizeURL = "https://secured.develgs.com/authorize"
credential_type= 'http://auth0.com/oauth/grant-type/password-realm'
origin = "https://auth.develgs.com:9092"
referer= "https://auth.develgs.com:9092/login"



with requests.Session() as s:
    
    authorityURL = "{0.scheme}://{0.netloc}/".format(urlsplit(url))

    #ALL CODE BELOW IS GENERIC ENOUGH TO PERFORM THE WORK
    headers = {
        "authority":authorityURL,
        "upgrade-insecure-requests":"1",
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site":"none",
        "sec-fetch-mode":"navigate",
        "sec-fetch-dest":"document",
        "accept-language":"en-GB,en-US;q=0.9,en;q=0.8",
        "origin": origin,
        "referer":referer 
    }
    
    print('-------------TRYING TO LOG INTO URL-----------------------')
    s.headers.update(headers)
    r= s.get(url)
    
    soup = BeautifulSoup(r.content,'html5lib')
    jsdata= str(soup.find_all('script')[1])
    start = jsdata.find('= {')+3
    end = jsdata.find('};')

    
    extracteddata= jsdata[start:end]
    #remove all spaces
    trimmeddata=  "".join(extracteddata.split())
    
    trimmeddata= re.sub("[,]", " ", trimmeddata)
    print('-------------GENERATING INFO TO BE USED IN LOGIN-----------------------')
    
    print(trimmeddata)         

    print('--------------EXTRACTING REQUIRED INFO----------------------')                        
    
    mydict = dict(s.split(':', 1) for s in trimmeddata.split())
    client_id= str(mydict['clientId'][1:-1])
    print("client_id :"+client_id)
   
    allowedConnetions= mydict['allowedConnections'][2:-2] 
    
    print('allowedConnections :'+allowedConnetions)
    
    state = mydict['state'][1:-1]
    print('state :'+state)
    
    redirectUrl = mydict['redirectUrl'][1:-1]
    print('redirectUrl :'+redirectUrl)
    
    
    print('\n')
    decodedURL= urlparse.urlparse(redirectUrl)
    #print("decodedURL: "+decodedURL)
    decodeQueryParams = parse_qs(decodedURL.query)
    print(decodeQueryParams)
    
    print('---------------LOGGING IN---------------------')
    
    
    
    login_data = {
        'password': password,
        'username': username,
        'client_id':client_id,
        'credential_type' : credential_type,
        'realm':allowedConnetions
    }
    
    print('---------------AUTHENTICATE CALL WITH REQUEST OPTIONS---------------------')
    
   
    login_response= s.options(authenicate_url)    
    print('---------------AUTHENTICATE CALL WITH WITH LOGIN DATA AND EXTRACTED INFO---------------------')


    login_response2= s.post(authenicate_url,data=login_data, cookies=login_response.cookies)
    
    print('\n')
    print('------CONTENT 2------------')
    
    jsonresp2=json.loads(login_response2.text)
    #print(jsonresp2)
    
    print('---------------LOGGED IN USING AUTHENTICATE CALL---------------------')    
    
    print('\n')
    print('--------HEADERS2----------')
    #print(login_response2.headers)
 
    print('---------------AUTHENTICATED NOW, GETTING LOGIN TICKET---------------------')    
    login_ticket = jsonresp2['login_ticket']
    print(login_ticket)
    
    print('---------------AUTHORIZE CALL WITH QUERY PARAMS---------------------')    
    queryparams1 = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': redirectUrl,
        'connection': allowedConnetions,
        'state': state,
        'scope': 'openid profile',
        'impersonatee_id': '',
        'prompt': 'select_account',
        'realm': allowedConnetions,
        'login_ticket': login_ticket,
        'auth0Client': authClient
    }
    
    response3= s.get(authorizeURL,params=queryparams1,cookies=login_response2.cookies)
    
    print('\n')
    print('------SESSION COOKIES------------')
    cookie_dict = s.cookies.get_dict()
    print(cookie_dict['sid'])
    
    '''
    print('\n')
    print('------CONTENT 3------------')
    print(response3.content)
    
    print('------HEADERS 3------------')
    print(response3.headers)
    
    print('------COOKIES 3------------')
    print(response3.cookies)
   '''
  
    