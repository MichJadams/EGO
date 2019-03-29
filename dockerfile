FROM python:3.7-alpine

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY src/ /src
WORKDIR /src

CMD ["cd"," convexHullNaive","python","-m","unittest","convex_hull_test.py","-v"]
