User these steps to install env 

pip install virtualenv
virtualenv venv

cd .\venv
 .\Scripts\activate.ps1  (for power shell, if any issue  use  Set-ExecutionPolicy unrestricted (use in power shell as admin))
cd ..            
pip install -r .\requirements.txt


pip install flask-sqlalchemy