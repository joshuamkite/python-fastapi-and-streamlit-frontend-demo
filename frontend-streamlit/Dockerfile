FROM python:3.12.8-slim AS build

WORKDIR /opt

COPY app.py .
COPY requirements.txt .


RUN python -m venv /venv \
    && /venv/bin/pip install --upgrade pip
RUN /venv/bin/pip install -r /opt/requirements.txt


FROM python:3.12.8-slim AS streamlitapp

WORKDIR /opt

COPY --from=build /venv/ /venv/
ENV PATH=/venv/bin:$PATH

COPY app.py .
COPY requirements.txt .

RUN useradd -m -d /home/nonroot -s /usr/sbin/nologin nonroot
USER nonroot

EXPOSE 8000
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]