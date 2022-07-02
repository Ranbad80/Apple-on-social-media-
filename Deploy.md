# Deploy My Code
## using Function App 
```
1-Login into the portal and click on Create Resource or you can search for Function app from the search bar to create and give required fields such as app name, storage account, and resource group, runtime stack, etc.
```
![first function](https://user-images.githubusercontent.com/83798130/176980467-76a83f47-2d82-4852-b5ec-e4b700549830.jpg)
```
in the next step we will use Visual Studio to deploy our code to function app. 
open Visual studio and sign in with an account having Azure Subscription.
Now for ease of use install the Azure functions extension from extensions menu on the left.
```
![Picture6](https://user-images.githubusercontent.com/83798130/176981030-bbf44439-4b85-4dc4-952c-c39a8b5a1c0f.jpg)
```
Choose the Azure icon in the Activity bar, then in the Azure: Functions area, select the Create new project icon.
```
![Picture7-1](https://user-images.githubusercontent.com/83798130/176981096-0878447a-38c8-4ad7-b180-ba6824fab9a7.jpg)
```
after that we will provide the name of the func and the trigger and we can update the time of the trigger from function.json file
and we Add the names of all the libraries that is needed to run the code under requirements.txt file
then publish the Function to Azure.
you can check your code in code+test
```

![thirdfuncti](https://user-images.githubusercontent.com/83798130/176981430-2194dd42-60c0-4c4e-8a1f-2b7273cf1c28.jpg)


## using  Azure DevOps project
```
To deploy to Azure App Service from Azure Pipelines, you need to establish a service connection between the two services.
In a browser, go to dev.azure.com. If you don't yet have an account on Azure DevOps, select Start free and get a free account.
```
![pipeline](https://user-images.githubusercontent.com/83798130/176981551-702e0cb5-975d-47f5-ad37-ce06a70b96ca.jpg)

