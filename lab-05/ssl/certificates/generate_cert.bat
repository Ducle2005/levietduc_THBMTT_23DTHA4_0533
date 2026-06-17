@echo off
setlocal enabledelayedexpansion

echo Checking if OpenSSL is available...
openssl version >nul 2>&1
if !errorlevel! equ 0 (
    echo OpenSSL found. Generating certificate using OpenSSL...
    openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt -subj "/CN=127.0.0.1"
) else (
    echo OpenSSL is not found in PATH.
    echo Trying to fallback to Python cryptography library...
    python generate_cert.py >nul 2>&1
    if !errorlevel! equ 0 (
        echo [SUCCESS] Certificate and Key generated successfully using Python cryptography library!
    ) else (
        echo [ERROR] Failed to generate certificate. Please install OpenSSL or python cryptography library.
    )
)
