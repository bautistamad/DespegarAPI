FROM python:3.10-slim-bullseye

# Esto hace que los errores vayan al CLI del Docker
# Utilizado para trabajar real-time
ENV PYTHONUNBUFFERED=1

# Especificamos que la carpeta de trabajo sera django
WORKDIR /django

# Copiamos los requerimientos de este directorio al directorio del container
COPY requirements.txt requirements.txt

# Corremos esto en el cli del container
RUN pip3 install -r requirements.txt
