@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Iniciando o site. O navegador abre sozinho em alguns segundos. Para encerrar, feche esta janela.
start "" cmd /c "ping -n 6 127.0.0.1 >nul & start http://127.0.0.1:8000/"
".venv\Scripts\python.exe" -m mkdocs serve
pause
