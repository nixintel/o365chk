FROM python:3

RUN pip install --upgrade pip

COPY o365chk.py ./
COPY requirements.txt ./

RUN pip install -r requirements.txt
CMD ["python", "o365chk.py -d"]
