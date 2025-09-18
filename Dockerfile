#Usa imagen de python  
FROM python:3.7.11-slim
#Crea directorio de trabajo
WORKDIR  /python-api
#copia el archivo
COPY requirements.txt requirements.txt
#Instala dependencias 
RUN pip install -r requirements.txt
#Copia el archivo 
COPY . .
#Comando que ejecuta la app 
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]




