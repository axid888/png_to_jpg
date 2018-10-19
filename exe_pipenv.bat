@echo off
rem 本batファイルを置いたフォルダにある*.pyファイルをpipenvで実行する。
rem 複数の*.pyファイルがある場合、一つのみ実行する。

cd /d %~dp0
for /f "usebackq tokens=*" %%a in (`dir /b *.py`) do @set PY_FILE_NAME=%%a&goto :exit_for
:exit_for

echo 続行すると%PY_FILE_NAME%を実行します。
echo.

pause

pipenv run python %PY_FILE_NAME%

echo.
echo %PY_FILE_NAME%の実行が完了しました。
pause