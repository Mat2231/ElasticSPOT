# ElasticSPOT
Automatic keyword search in exposed Elasticsearch DB


A crawler to search for keywords within Elastic's databases exposed on the Internet. 
The search with "/_all/_search?q=" and keyword with provides interesting information because it does not search within the headers. So the script first looks at the existing tables and then downloads a small part of the tables to search for the keyword.
