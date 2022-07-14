# event emitter
A Python source-to-image application for emitting to an Apache Kafka topic

## Launching on OpenShift

oc get all --selector app=sales-emitter -o name
oc delete all --selector app=sales-emitter



oc new-app python:3.9-ubi8~https://github.com/dbrugger946/deploy-models\\  
  --context-dir=sales-event-emitter \\  
  --name=sales-emitter  

// orig version new-app showing some additioanl settings
oc new-app centos/python-36-centos7~https://github.com/dbrugger946/bank-events \\  
  --context-dir=event-emitter \\  
  -e KAFKA_BROKERS=my-cluster-kafka-bootstrap:9092 \\  
  -e KAFKA_TOPIC=event-input-stream \\  
  -e RATE=1 \\  
  --name=emitter  
```

You will need to adjust the `KAFKA_BROKERS` and `KAFKA_TOPICS` variables to
match your configured Kafka deployment and desired topic. The `RATE` variable
controls how many messages per second the emitter will send, by default this
is set to 3.
