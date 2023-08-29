# deploy-models

- predict-sales is the context dir for the model creation/serving  
- sales-event-emitter is under construction (gen random events to kafka, then use camelk / serverless to feed predict-sales)  

## example ocp invocations
curl -X POST -H "Content-Type: application/json" -d  '{"rate":5, "sales_in_first_month":200, "sales_in_second_month":400}' https://predict-deploy-models.apps.somecluster.com/results

curl -X POST -H "Content-Type: application/json" -d  '{"rate":5, "sales_in_first_month":200, "sales_in_second_month":400}' https://predict-fast-deploy-models.apps.somecluster.com/results


kn service update predict-fast --image quay.io/dbrugger946/predict:1.3

### for s2i  -- may not be needed depending upon location of python files
oc set env deployment deploy-models-git  APP_FILE=app/app.py
### build a container from deploy-models
podman build -t active-model .  
podman run  -p 5000:5000  --name mod localhost/active-model  
### running command line deploy-models
- move to deploy-models directory
- pip install --upgrade pip
- pip install -r requirements.txt
- python model.py
- python app.py

## Source article for original idea for using linear regression and python approach

https://towardsdatascience.com/how-to-easily-deploy-machine-learning-models-using-flask-b95af8fe34d4



