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

![capstone1](https://user-images.githubusercontent.com/83798130/171025830-626c376e-60b7-42fa-b6c2-598e7586b850.jpg)


