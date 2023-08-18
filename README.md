# container_apps_demo

## backendflask
<br>This folder container python file which returns "hello" generating each alphabet in either capital or small randomly.</br>
<br> Container a Dockerfile which containerizes the app.</br>
<br> Requirements.txt for all the dependencies needed.

## frontendflask
<br>This folder container python file which fetches "hello" generating each alphabet in either capital or small randomly from backendflask app</br>
<br> Container a Dockerfile which containerizes the app.</br>
<br> Requirements.txt for all the dependencies needed.

## STEPS TO DEPLOY THE APPS IN AZURE PORTAL FROM UI

### Build and push Docker image into ACR
<br> az login </br>
<br> az acr login --name <acr_name> </br>
<br> docker build -t <acr_name>.azurecr.io/<image_name>:<tag> . </br>
<br> docker push <acr_name>.azurecr.io/<image_name>:<tag> </br>

### Create container app from docker image in azure portal
<br> Navigate to container apps service. </br>
<br> Create container apps->select container app environment </br>
<br> Navigate to container tab-> disable quickstart option-> select image from acr->add required enviroment variables.</br>
<br> Navigate to ingress.Configure the ingress as per your requirement.</br>
<br> Review+create</br>

### Environment variables used in this code:
    backapp: HELLO_SERVICE_PORT=80
    frontapp: PORT=8090
              HELLO_SERVICE_HOST_PREFIX=<backapp's application URL>
