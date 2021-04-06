# About this Repo

This repo illustrates the basics of running a FastAPI application on Azure Functions.

Much of the code here has been borrowed/copied from:  https://github.com/tonybaloney/ants-azure-demos/tree/master/fastapi-functions

# To Deploy To Azure Functions

These steps assume that you are using the [Azure Functions VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions).

Step 1:  Create an [Azure Account](https://azure.microsoft.com/en-us/).

Step 2:  Install the [Azure Functions VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions).

Step 3:  Open your project in VSCode.  VSCode will automatically create a virtual environment for you and install all dependencies.

Step 4:  Run your Azure Function locally:

  * Just press F5!

Verify that your app is running by going to:  http://localhost:7071/user/1.  You should see a JSON response with some fake data.  For example:
    
    {
        "user_id":1,
        "username":"AdianaRestrict_1858",
        "firstname":"Beau",
        "lastname":"Lancaster"
    }

Step 5:  Deploy your function to Azure:

  * Open the VSCode Command Pallette.
  * Run "Azure Functions:  Deploy to Function App.
  * Follow the promps and wait a few minutes for everything to deploy.

Verify that your app is running by going to:  https://<APP_NAME>.azurewebsites.net/user/1.  You should see similar fake data as shown in Step 4.