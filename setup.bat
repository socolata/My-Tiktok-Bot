@echo off
:: TIKBOT - Professional Setup & Runner
:: Created by @socolata | © 2026

title TIKBOT v4.2 - Initializing...
setlocal enabledelayedexpansion
color 0b

echo ======================================================
echo           TIKBOT - AUTOMATED SETUP ENGINE
echo                Created by @socolata
echo ======================================================
echo.
echo [NEWS] Reposts service is now available in v4.2!
echo.

:: Step 1: Check for Python
echo [1/4] Checking system environment...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0c
    echo [ERROR] Python is not installed or not in your PATH.
    echo Please install Python 3.11 or higher from python.org.
    pause
    exit
)
echo [SUCCESS] Python detected.

:: Step 2: Update PIP
echo [2/4] Optimizing package manager...
python -m pip install --upgrade pip --quiet
echo [SUCCESS] Pip is up to date.

:: Step 3: Install Dependencies
echo [3/4] Installing required libraries...
echo Please wait, this might take a minute...

:: Primary installation from file
pip install -r requirements.txt --quiet

:: Fallback installation in case requirements.txt is missing or corrupted
if %errorlevel% neq 0 (
    echo [WARNING] Problem with requirements.txt. Attempting manual install...
    python -m pip install colorama==0.4.6 selenium==4.10.0 webdriver-manager==4.0.2 certifi requests urllib3 packaging python-dotenv setuptools --quiet
)

if %errorlevel% neq 0 (
    color 0c
    echo [CRITICAL ERROR] Failed to install dependencies. 
    echo Please check your internet connection.
    pause
    exit
)
echo [SUCCESS] Environment is ready.

:: Step 4: Launch Bot
echo [4/4] Starting TIKBOT Engine...
echo.
echo ------------------------------------------------------
echo    TIP: Solve the CAPTCHA in the browser to start.
echo    Choose Option 8 for REPOSTS!
echo ------------------------------------------------------
timeout /t 3 >nul

cls
python main.py

if %errorlevel% neq 0 (
    echo.
    echo [INFO] Process finished.
    pause
)