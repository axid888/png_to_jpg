@echo off
rem �{bat�t�@�C����u�����t�H���_�ɂ���*.py�t�@�C����pipenv�Ŏ��s����B
rem ������*.py�t�@�C��������ꍇ�A��̂ݎ��s����B

cd /d %~dp0
for /f "usebackq tokens=*" %%a in (`dir /b *.py`) do @set PY_FILE_NAME=%%a&goto :exit_for
:exit_for

echo ���s�����%PY_FILE_NAME%�����s���܂��B
echo.

pause

pipenv run python %PY_FILE_NAME%

echo.
echo %PY_FILE_NAME%�̎��s���������܂����B
pause