# Employee Management Kubernetes Project

This project demonstrates a production-style Kubernetes deployment using:


step-1
#kubectl apply -f namespace.yaml

step-2
#kubectl apply -f storage/pv.yaml
#kubectl apply -f storage/pvc.yaml

step-3
#kubectl apply -f configmap.yaml
#kubectl apply -f secret.yaml

step-4
#kubectl apply -f database/mariadb-deployment.yaml
#kubectl apply -f database/mariadb-service.yaml

step-5
#kubectl apply -f employee-service.yaml
#kubectl apply -f employee-deployment.yaml

step-6
#kubectl apply -f ingress/employee-ingress.yaml


