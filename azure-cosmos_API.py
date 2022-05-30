from importlib.resources import Package
import glob
import pandas as pd
import json
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
import azure.cosmos.documents as documents
from azure.cosmos.partition_key import PartitionKey
import datetime



print('Imported packages successfully.')

# Initialize the Cosmos client

config = {
    "endpoint": "https://applecap.documents.azure.com:443/",
     "primarykey": "98s0dOykDRb2TH586o112AlZw2Gtt18drNHner7ihRqnCwQT7B32bvmETrjqeTxs1XLdKBcVwNquC12ObLvH3w=="
}

# Create the cosmos client
client = cosmos_client.CosmosClient(url=config["endpoint"], credential={"masterKey": config["primarykey"]}
)



# Create a database
# https://docs.microsoft.com/en-us/python/api/azure-cosmos/azure.cosmos.cosmos_client.cosmosclient?view=azure-python#createdatabase-database--options-none-

database_name = 'AppleInfo'
try:
    database = client.create_database_if_not_exists({'id': database_name})
    print("DataBase is Created!")
except:
    database = client.get_database_client("dbs/" + database_name)

try:
    database_link = 'dbs/' + 'AppleInfo'

    container_name = 'ApplePost'
    container = database.create_container_if_not_exists(
        id='ApplePost',
        partition_key=PartitionKey(path="/thread/country"),
        offer_throughput=400)
except:
    container = database.get_container_client(container_name)

print(len(glob.glob('/Users/raniabadr/Documents/capstone_project/jsonfiles1/*.json')))

for file in glob.glob('/Users/raniabadr/Documents/capstone_project/jsonfiles1/*.json'):
    with open(file , 'r') as f:
        json_data = json.loads(f.read())
        json_data["id"] = json_data["uuid"]
        insert_data = container.create_item(json_data)




