start-env:
	docker build . --tag=ecg-app && docker run --name ecg-container -p 8000:8008 ecg-app 

test:
	docker exec -it ecg-container python manage.py test

