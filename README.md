TestsAtYourService
==================

A presentation and the companion code made at VodQA Pune 2013

Presentation is located at 
http://prezi.com/03uflnb_kjti/tests-at-your-service/?utm_campaign=share&utm_medium=copy

Companion Demo
==============

cURL to make HTTP request to a webservice
==========================================

The curl commands for fetching the album list are from:
https://developers.google.com/gdata/articles/using_cURL#authenticating

To get the Auth token:
curl https://www.google.com/accounts/ClientLogin --data-urlencode Email=<EMAIL> --data-urlencode Passwd=<PASSWORD> -d service=lh2 -d accountType=GOOGLE

Using Auth Token fetch the list of albums for a user
curl --silent --header "Authorization: GoogleLogin auth=<AUTH>" "http://picasaweb.google.com/data/feed/api/user/default"

Code for comparing UI and Services layer automation
====================================================
1. PicasaUIDemo

2. PicasaServicesDemo

Presentation
=============
Launch prezi.exe for the readonly presentation
