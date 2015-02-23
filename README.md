#####Usage for plus11.py:
`./plus11.py oldfile > newfile`

#####Format it expects:
`1424649600.208370 api.geo.kontagent.net /api/v1/xyz
1424649601.115421 api.geo.kontagent.net /api/v1/abc`

#####Outputs
`2015-02-23_11:00:00 api.geo.kontagent.net /api/v1/xyz
2015-02-23_11:00:01 api.geo.kontagent.net /api/v1/abc`




#####Usage for plus11ChromeHistoryDB.py
######This expects a csv from a Chrome history file, see http://www.forensicswiki.org/wiki/Google_Chrome#History
`./plus11ChromeHistoryDB.py oldfile.csv > newfile.csv`

#####Format it expects:
`"2014-09-10 05:42:05",http://tools.google.com/chrome/intl/en/welcome.html,"Getting Started"
"2014-09-10 05:42:05",https://www.google.com/intl/en/chrome/browser/welcome.html,"Getting Started"`

#####Outputs:
`2014-09-10 16:42:05,http://tools.google.com/chrome/intl/en/welcome.html,"Getting Started"
2014-09-10 16:42:05,https://www.google.com/intl/en/chrome/browser/welcome.html,"Getting Started"`