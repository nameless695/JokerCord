echo "Proceeding with the installation"
echo "Don't forget to add Python to the PATH (It is in a checkbox)
echo "Checking architecture:"

@echo OFF

reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && set OS=32BIT || set OS=64BIT
if %OS%==32BIT (wget "https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe"; START /WAIT "python-3.8.1.exe")
if %OS%==64BIT (wget "https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe-amd64"; START /WAIT "python-3.8.1.exe-amd64")
python -V > set VERSION
echo %VERSION%
echo "Python 3.8 has been installed succesfully" 
pip3 install discord.py requests pillow flask
START 
