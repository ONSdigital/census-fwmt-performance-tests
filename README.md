
census-fwmt-performance-testing toolset is split into 

1) FWMTG-perf-tests : Python programs to publish messages onto RM.Field Rabbit MQ and track the message consumption by JobserviceV4 service.

2) fwmtg-locust     : Locust deployment with python program to simulate load on outcomeservice ( TM -> Outcomeservice -> Rabbit preprocessign queue) 



FWMTG-perf-tests: Message simulator and load generator for performance testing of JobserviceV4.


This python toolset does the following :

1) Creates sample messages with unique caseIds without any database or datastores.
2) The number of messages to create is configured (Config.CASES_TO_FETCH).
3) The fixed number of messages are published onto RM.Field queue on RabbitMQ instance configured in (Config.RABBITMQ_HOST).
4) Publish messages onto RM.Field queue on RabbitMQ. 
5) Tracks the message consumption by Jobservice V4. 
6) Calculate and reports the message consumption rate.
''

Python programs :

1) publish_create.py  : Generates 'Create' type messages and simulates the behaviour.
2) publish_cancel.py  : Simulates the behaviour of 'Create' followed by 'Cancel' . Generates 'Create' type messages followed by 'Cancel' messages .
3) publish_update.py  : Simulates the behaviour of 'Create' followed by 'Update'. Generates 'Create' type messages followed by 'Update' messages . 
4) testFiles.py 	  : Tracks message consumption and reports message consumption / processing rate.


GCP Deployment:

Dockerfile to build the docker image
create-perftests-pod.yml to create fwmtg-perf-test are included in the Python folder

How to run :

1) fwmtg-perf-tests deployment includes all the python scripts listed above.
2) Download the Makefile locally (local pc).
	make python 	  : Creates fixed number of 'Create' messages and publishes onto the RabbitMQ.
	make consume      : Tracks the message consumption by JObservicev4.
	make report 	  : Creates report with caseIds and message consumption rate.
	make clean		  : Removes all the txt files ( does not remove scripts).

Expected results :

Total processing time for 10000 number of requests is 157.970s.
Average processing time for 10000 number of requests is 75170.003ms  / 75.170s.
Number of requests per second are 63.


fwmtg-locust : Locust tests simulating TM outcomes.

This tool set includes :

1) Locust : distributed deployment of locust master and worker mode.
2) Load_test.py : Generates 'Outcome' messages and posts to outcome service endpoint.

GCP Deployment:

Dockerfile to build locust images with test script.
fwmtg-locust-deployment.yml to deploy locust master and worker nodes.

How to run (locally):

1) Build the docker image using Dockerfile in fwmtg-locust/Docker.
2) Docker run locust image.
3) Execute "locust -f load_test.py --no-web -t 10s"

In GCP

1) Connect to locust master pod
2) Execute 'locust -f load_test.py --no-web -t 10s'

Expected results :

In test duration of 60s Total 11624 requests sent with 257.00 requests per second 

 Name                                                          # reqs      # fails     Avg     Min     Max  |  Median   req/s
--------------------------------------------------------------------------------------------------------------------------------------------
 POST /spgOutcome                                               11624     0(0.00%)     309       4    1469  |     300  257.20
--------------------------------------------------------------------------------------------------------------------------------------------

Alternatively way to run the performance tests 

1. Connect the terminal to envirnonment that you want to run the tests by using the following command. This example is for Greylodge

gcloud container clusters get-credentials fwmt-gateway-k8s-cluster --region europe-west2 --project census-fwmt-gateway-test

2. connect to the kubernates cluster and play the following comand and get the pod in which test are running
Kubectl get pods

3. connect to the pod by the follwoing command where fwmtg-perf-test-66b9746fd4-5z7n7 is the test pod
kubectl exec --stdin --tty fwmtg-perf-test-66b9746fd4-5z7n7  -- /bin/bash

4. view the config.py file and change the number 
change the value of CASES_TO_FETCH = 1000000 by following commad.
sed -i 's/old-text/new-text/g' config.py

5. Run the following command to run the tests
python publish_create.py 



