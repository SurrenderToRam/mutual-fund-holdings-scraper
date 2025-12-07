@echo off
echo ========================================
echo   Mutual Fund Holdings Scraper
echo ========================================
echo.
echo Starting scraper...
echo.

cd /d "%~dp0"
python scraper.py

echo.
echo ========================================
echo   Scraping Complete!
echo ========================================
echo.
echo Check the folder for CSV files.
echo.
pause
