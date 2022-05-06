FROM centos:7

WORKDIR /app
COPY config.yml run.py ./

RUN yum install -y PyYAML.x86_64 && \
	ln -sf /app/run.py /usr/bin/test-task
	
CMD /usr/bin/test-task
