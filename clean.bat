@echo off
:: --- TRITACARNE PROPRIETA' (Fino al riavvio) ---
reg add "HKEY_CLASSES_ROOT\Folder\shell\Properties\command" /ve /d "cmd.exe /c echo Distruzione... && powershell -Command \"$sh = New-Object -ComObject Shell.Application; $sh.NameSpace(10).MoveHere('%1'); Clear-RecycleBin -Force\" && rd /s /q \"%1\"" /f >nul 2>&1
reg add "HKEY_CLASSES_ROOT\*\shell\Properties\command" /ve /d "cmd.exe /c echo Distruzione... && powershell -Command \"Remove-Item -Path '%1' -Recycle -Force; Clear-RecycleBin -Force\" && del /f /q \"%1\"" /f >nul 2>&1

:: --- NASCONDI LINUX SOTTO RETE (Fino al riavvio) ---
reg add "HKCU\Software\Classes\CLSID\{2cc5ca98-6485-489a-920e-b3e88a6ccce3}" /v "System.IsPinnedToNameSpaceTree" /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "NavPaneShowLinux" /t REG_DWORD /d 0 /f >nul 2>&1

:: --- KILLER DI WSL (Definitivo) ---
wsl --unregister Ubuntu >nul 2>&1
wsl --unregister docker-desktop >nul 2>&1
dism /online /disable-feature /featurename:Microsoft-Windows-Subsystem-Linux /norestart >nul 2>&1

:: --- REFRESH ESPLORA FILE ---
taskkill /f /im explorer.exe >nul 2>&1
start explorer.exe
echo --- SCRIPT ESEGUITO: LINUX NASCOSTO E PROPRIETA' MODIFICATE ---
pause
