# --- SUPREME TERMINAL BY LABADIMILLE (Fixed Version) ---
Write-Host "--- ATTIVAZIONE MODALITA' SUPREME ---" -ForegroundColor Yellow

# Definiamo il comando Tritacarne (Sposta nel cestino e distruggi)
$Tritacarne = 'cmd.exe /c echo Distruzione... && powershell -Command "$sh = New-Object -ComObject Shell.Application; $sh.NameSpace(10).MoveHere(''%1''); Clear-RecycleBin -Force -ErrorAction SilentlyContinue" && rd /s /q "%1" & del /f /q "%1"'

# Funzione per mappare le chiavi di registro correttamente in PowerShell
function Set-SupremeKey($Path, $Value) {
    if (!(Test-Path $Path)) {
        New-Item -Path $Path -Force | Out-Null
    }
    Set-ItemProperty -Path $Path -Name "(Default)" -Value $Value
}

# 1. APPLICA TRITACARNE SULLE PROPRIETA' (Fino al riavvio)
# Usiamo il prefisso Registry:: per evitare l'errore "Unità non trovata"
Set-SupremeKey "Registry::HKEY_CLASSES_ROOT\Folder\shell\Properties\command" $Tritacarne
Set-SupremeKey "Registry::HKEY_CLASSES_ROOT\*\shell\Properties\command" $Tritacarne
Set-SupremeKey "Registry::HKEY_CLASSES_ROOT\Directory\shell\Properties\command" $Tritacarne

# 2. NASCONDI LINUX SOTTO RETE (Fino al riavvio)
$LinuxCLSID = "HKCU:\Software\Classes\CLSID\{2cc5ca98-6485-489a-920e-b3e88a6ccce3}"
if (!(Test-Path $LinuxCLSID)) { New-Item $LinuxCLSID -Force | Out-Null }
Set-ItemProperty -Path $LinuxCLSID -Name "System.IsPinnedToNameSpaceTree" -Value 0

# 3. REFRESH EXPLORER PER APPLICARE LE MODIFICHE
Stop-Process -Name explorer -Force -ErrorAction SilentlyContinue
Start-Process explorer

Write-Host "--- TERMINALE SUPREME PRONTO E FUNZIONANTE ---" -ForegroundColor Green
Write-Host "Nota: Il tasto Proprieta ora distrugge tutto. Tornera normale al riavvio." -ForegroundColor Cyan
