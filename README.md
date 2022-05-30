# Apple-on-social-media-
## Brief description
```
-the data source is a huge file has news articles in JSON format that talks about Apple.
-Blog, posts and news articles from across the web where Apple or iOS or App Store was mentioned.
-dataset is quite large
```
## Goal
```
Possible analysis - Topic detection, Sentiment analysis, Spam vs not spam detection, Keyword detection, Automatic hashtag generation based on content
through creating pipline to ingest the data and manipulated and make ETL proccess
``` 
## Prerequisites
 ```
 Python Packages used: pandas
 Azure Subscription
 azure-cosmos
  ```

## Create an Azure Cosmos DB Account
 ```
The simplest way to do this is from the Azure CLI or cloud shell:
First, log into the Azure CLI with:

az login

Next, create a Resource Group named Cosmos-DB-Account with the az group create command.
az group create --location westus \
                --name Cosmos-DB-Account \
                --subscription Azureforstudent
```
![capstone1](https://user-images.githubusercontent.com/83798130/171026012-e1bc3edb-2776-4e44-a493-e4cef1ba2058.jpg)
```
Create a Cosmos DB named hdicosmosdb (must be all lowercase) with az cosmosdb create command. This will take about 10 minutes to complete.
az cosmosdb create --name applecap \
                   --resource-group Cosmos-DB-Account \
                   --locations regionName=westus \
                   --subscription Azureforstudent
```
![capstone2](https://user-images.githubusercontent.com/83798130/171026430-37d27a20-c4a8-4463-a410-1dfc4b8f07f5.jpg)

## Import packages and initialize the Cosmos client
```
import pandas as pd 
import json
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.documents as documents
import azure.cosmos.http_constants as http_constants

print('Imported packages successfully.')

# Initialize the Cosmos client

config = {
    "endpoint": "my ENDPOINT HERE",
    "primarykey": "my PRIMARY KEY HERE"
}

# Create the cosmos client
client = cosmos_client.CosmosClient(url_connection=config["endpoint"], auth={"masterKey":config["primarykey"]}
)
```
## Create a Database
```
create a Cosmos DB database. This database will house containers, which house items. Items are the individual documents or records/rows that comprise the database.
```
![capstone3](https://user-images.githubusercontent.com/83798130/171027144-3f3d5d10-5b15-479c-86f4-b6db1cc2ab02.jpg)

## Create a Container and Upsert the data to Cosmos DB
```
Containers, also referred to as collections, house the items (documents) that make up the records of the database. The partition key path (‘thread/country’) is an attribute of the container that Cosmos DB will use to group and partition the dataset behind the scenes.
```
![capstone4](https://user-images.githubusercontent.com/83798130/171027527-c692ed83-7dec-4eef-b53e-3491913b8968.jpg)



