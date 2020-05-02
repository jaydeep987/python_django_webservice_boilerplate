FROM nginx:stable-alpine

ARG ECR_REPOSITORY_APP

COPY nginx.template.conf /home/

RUN echo "ssss".$ECR_REPOSITORY_APP

# Parse template file and will generate new file with replaced values
RUN sed -e "s/\${ECR_APP_SERVER}/$ECR_REPOSITORY_APP/" /home/nginx.template.conf > /home/nginx.conf

# Setup nginx
RUN rm /etc/nginx/conf.d/default.conf
RUN mv /home/nginx.conf /etc/nginx/nginx.conf
# RUN service nginx start
