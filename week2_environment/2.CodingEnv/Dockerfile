FROM python
MAINTAINER Yidan Chen
ENV RESEARCH_PATH=/Users/chenyidan/homework_dft/week2_environment/2.CodingEnv
COPY . $RESEARCH_PATH
COPY . /app
WORKDIR /app
ADD Code_Script.py /
RUN pip install matplotlib
RUN pip install os.path2
RUN pip install pandas
CMD ["python", "./Code_Script.py"]



