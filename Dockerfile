FROM python:3.9
WORKDIR /Users/sam/florishing-flora
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./flipcap_project.py" ]
#an attempt to resolve the collections error
ENTRYPOINT ["python", "-c", "from collections.abc import Mapping"]