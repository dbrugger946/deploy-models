# deploy-models



curl -X POST -H "Content-Type: application/json" -d  '{"rate":5, "sales_in_first_month":200, "sales_in_second_month":400}' https://predict-serverless-knative-sandbox.apps.cluster-hhdnz.hhdnz.sandbox1353.opentlc.com/results

kn service update predict-serverless --image quay.io/dbrugger946/predict:1.3
