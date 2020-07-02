# My serverless app on Azure Functios

## Install serverless and init project

Install serverless
```
npm install serverless --global
```

Install azure dependence
```
npm i --save serverless-azure-functions
```

Initialize project with template for python azure-functios
```
sls create -t azure-python -p serverless-app
cd serverless-app/
```

## Install azure-cli and configure subscription

1 - Install azure-cli
```
sudo apt install azure-cli
```

Configure subscriptions
```
# 2 - Login to Azure
az login
# Set Azure Subscription for which to create Service Principal
az account set -s <subscription-id>

# 3 - Create SP with unique name
az ad sp create-for-rbac --name <my-unique-name>
```

4 - Edite deploy.sh with output following the reference
```
export AZURE_SUBSCRIPTION_ID='<subscriptionId (see above, step 2)>'
export AZURE_TENANT_ID='<tenantId>'
export AZURE_CLIENT_ID='<servicePrincipalId>'
export AZURE_CLIENT_SECRET='<password>'
```
## Testing locally

```
sls offline
```

## Deploy
```
./deploy.sh
```