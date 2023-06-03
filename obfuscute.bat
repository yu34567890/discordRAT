@echo off
echo obfuscate write by https://github.com/syntheticlol/Discord-RAT/commits?author=syntheticlol
echo Start build before obfuscate
echo Starting obfuscate in
echo 3
timeout /t 1 >nul
echo 2
timeout /t 1 >nul
echo 1
timeout /t 1 >nul

upx --best --force dist/source.exe

echo.
echo Press any key to exit...
pause >nul
