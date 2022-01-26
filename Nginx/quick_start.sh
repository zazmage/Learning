apt-get update
apt-get install python3 pip systemctl wget unzip vim curl -y
apt-get install python-is-python3 -y
pip install uwsgi
wget https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip
unzip web2py_src.zip
printf "1234/2/105/us/new york city/testcompany/software/testname/testemail@domain.com" | ./setup-web2py-nginx-uwsgi-ubuntu.sh
