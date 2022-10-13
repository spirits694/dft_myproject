FROM python
MAINTAINER Yidan Chen
ENV RESEARCH_PATH=/Users/chenyidan/DFTProject/Wk02_Ex/CodingEnv
COPY . $RESEARCH_PATH
ADD Code_Script.py /
RUN pip install matplotlib
RUN pip install os.path2
RUN pip install pandas
CMD ["python", "./Code_Script.py"]



