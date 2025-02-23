:: Path-Variable
@Echo off
Set "VIRTUAL_ENV=.venv"


:: Create virtual environment if not exists
If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" (
    python.exe -m pip install --upgrade pip
    pip.exe install virtualenv
    python.exe -m venv %VIRTUAL_ENV%
)


:: Break
If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" Exit /B 1


:: Calling activate in .venv and installing requirements
Call "%VIRTUAL_ENV%\Scripts\activate.bat"
pip.exe install -r requirements.txt

Pause
Exit /B 0