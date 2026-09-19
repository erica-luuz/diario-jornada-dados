@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Abrindo o site no navegador. Para encerrar, feche esta janela.
start "" "http://127.0.0.1:8000/"
".venv\Scripts\python.exe" -m mkdocs serve
pause
