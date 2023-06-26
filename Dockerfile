FROM 190109388255.dkr.ecr.ap-south-1.amazonaws.com/ami-nginx:latest
COPY ./index.html /usr/share/nginx/html/index.html
