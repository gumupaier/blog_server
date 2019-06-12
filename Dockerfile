FROM python:3.6
ARG BUILD_VERSION=0.0.1.1

ENV LANG=C.UTF-8

COPY . /work
WORKDIR /work

RUN pip install -r requirements.txt -i https://pypi.douban.com/simple

RUN cp prod_entrypoint.sh /usr/bin/ && chmod +x /usr/bin/prod_entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["prod_entrypoint.sh"]

CMD ["blog-server-starter"]