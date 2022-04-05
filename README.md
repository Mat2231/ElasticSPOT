# ElasticSPOT
Automatic keyword search in exposed Elasticsearch DB

A Crawler written in python to search for keywords within Elastic databases exposed on the internet. 
Searching with "/_all/_search?q=" and keyword does not provide any interesting information because it does not search within the headers. So the script first looks at the existing tables and then downloads a small part of the tables to search for the keyword.

"/_cat/indices?v" query tables

"/nametable/_search?pretty=true&size=25" download of a part of the db

Download from shodan.io the list of ip's and ports and put in the file servers.txt. 

Have fun

For information write to blackholetechnlogies@protonmail.com

