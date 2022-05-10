docker stop binpackage
docker container rm binpackage
docker build . -t glaciersg/binpackage_api:v1.0.0
docker run -d -p 8080:8080 --name=binpackage glaciersg/binpackage_api:v1.0.0
