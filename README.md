# deploy-models



curl -X POST -H "Content-Type: application/json" -d  '{"rate":5, "sales_in_first_month":200, "sales_in_second_month":400}' https://predict-deploy-models.apps.elm.optimalpath.xyz/results

curl -X POST -H "Content-Type: application/json" -d  '{"rate":5, "sales_in_first_month":200, "sales_in_second_month":400}' https://predict-fast-deploy-models.apps.elm.optimalpath.xyz/results


kn service update predict-fast --image quay.io/dbrugger946/predict:1.3

for s2i
oc set env deployment deploy-models-git  APP_FILE=app/app.py
