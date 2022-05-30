build:
	docker build . -t binpackage_api
run:
	docker run -d -p 8080:8080 --name=binpackage binpackage_api
stop:
	docker stop binpackage
	docker container rm binpackage
