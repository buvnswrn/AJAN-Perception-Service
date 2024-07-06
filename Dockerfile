FROM python:3.10.14
LABEL authors="bhuvan"

WORKDIR /service
COPY ./tests/copy_image_string_server.py /service/copy_image_string_server.py
COPY requirements.txt /service/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8501
#CMD ["streamlit", "run", "copy_image_string_server.py"]
ENTRYPOINT ["streamlit", "run","copy_image_string_server.py","--server.port=8501","--server.enableCORS=false"]