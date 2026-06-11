cls
call C:\ComfyUI\venv\Scripts\activate.bat 

echo "try build & install wheel..." 

pip install -e . --no-build-isolation -vvv > build.log 2>&1