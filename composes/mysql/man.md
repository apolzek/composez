Credentials: root:password

http://localhost:8888/?server=mysql&username=root


```bash
python3 -m venv venv
source venv/bin/activate
pip install mysql-connector-python
pip freeze > requirements.txt
python3 insert.py 
 ```