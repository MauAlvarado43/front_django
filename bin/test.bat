@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

for /f "delims=" %%i in ('docker-compose -f bin/docker/docker-compose-dev.yml ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" echo ERROR: Before executing bin/test.bat, start server with bin/start.bat
IF "%RUNNING%" == "" exit 1

echo == Executing test cases
docker-compose -f bin/docker/docker-compose-dev.yml exec front_django /bin/sh -c "python manage.py test"