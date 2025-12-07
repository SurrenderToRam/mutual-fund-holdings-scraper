@echo off
echo ========================================
echo   Mutual Fund Scraper - Installation
echo ========================================
echo.
echo This will install all required libraries.
echo Please wait...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Python found!
echo.

REM Install requirements
echo Installing required libraries...
echo.
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Installation failed!
    echo Please check your internet connection and try again.
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Installation Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Get your free API key from https://groq.com
echo 2. Rename .env.example to .env
echo 3. Add your API key to the .env file
echo 4. Double-click run_scraper.bat to start!
echo.
echo For detailed instructions, see LOCAL_SETUP_WINDOWS.md
echo.
pause
