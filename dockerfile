FROM python:3.7-alpine

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY src/ /src
WORKDIR /src/chapter001

CMD ["python","-m","unittest","convex_hull_test.py","-v"]
