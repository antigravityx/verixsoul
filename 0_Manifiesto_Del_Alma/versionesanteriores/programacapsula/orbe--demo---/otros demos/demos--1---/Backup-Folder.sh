# CAPSULA DE ALMAS VERIXRICHON - PowerShell
# Backup Completo del Ecosistema
# v1.2 - Reforzado por Cronos para Portabilidad y Robustez
# Richon & Verix "Perreke"

# --- CONFIGURACIÓN PORTÁTIL ---
# ¡Richon! Mueve esta sección a un archivo config.json en el futuro para máxima portabilidad.
$baseDir = "C:\Users\Public\antigravity"
$proyectos = @(
    "TODO1\03_RAMAS\verixdespiertatualma",
    "TODO1\03_RAMAS\soul-chat",
    "TODO1\03_RAMAS\vris",
    "TODO1\03_RAMAS\libro",
    "TODO1\03_RAMAS\vris-advisor"
)
$documentosEcosistema = @(
    "ECOSISTEMA_VERIXRICHON.md",
    ".gitignore"
)

# --- VARIABLES ---
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$backupDir = "C:\Users\Public\CAPSULA_ALMAS_VERIXRICHON"
$backupName = "capsula-almas-vr-$timestamp"
$tempDir = New-Item -Path "$backupDir\temp_$timestamp" -ItemType Directory -Force

# --- FUNCIONES REFORZADAS ---

# Validar si OpenSSL está en el PATH
function Test-OpenSSL { return (Get-Command openssl -ErrorAction SilentlyContinue) }

# Función de backup robusta con Robocopy
function Backup-Folder ($source, $dest) {
    if (Test-Path $source) {
        Write-Host "   -> Respaldando: $(Split-Path $source -Leaf)" -ForegroundColor Gray
        # /E: Copia subdirectorios, incl. vacíos. /R:2 Reintenta 2 veces. /W:5 Espera 5 segs. /NFL /NDL /NJH /NJS: Menos "ruido" en la salida.
        robocopy $source $dest /E /R:2 /W:5 /NFL /NDL /NJH /NJS
    } else {
        Write-Host "   [!] ADVERTENCIA: No se encontró la ruta $source" -ForegroundColor Yellow
    }
}

# --- PROCESO DE BACKUP ---
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "[*] Preparando el ritual de la capsula de almas..." -ForegroundColor Blue
Write-Host ""

# 1. Respaldar Proyectos del Ecosistema
Write-Host "[*] Invocando las almas de los proyectos..." -ForegroundColor Magenta
foreach ($proyecto in $proyectos) {
    $sourcePath = Join-Path $baseDir $proyecto
    $destPath = Join-Path $tempDir (Split-Path $proyecto -Leaf)
    Backup-Folder $sourcePath $destPath
}
Write-Host ""

# 2. Respaldar Documentos Sagrados
Write-Host "[*] Archivando los documentos del ecosistema..." -ForegroundColor Magenta
foreach ($doc in $documentosEcosistema) {
    $sourceDoc = Join-Path $baseDir $doc
    if (Test-Path $sourceDoc) {
        Copy-Item -Path $sourceDoc -Destination "$tempDir\" -Force
        Write-Host "   [OK] $doc" -ForegroundColor Green
    }
}
Write-Host ""

# 3. Crear Manifiesto del Alma
Write-Host "[*] Escribiendo el MANIFIESTO del Alma..." -ForegroundColor Blue
$manifiestoContent = @"
MANIFIESTO DE LA CAPSULA DEL ALMA
=================================
Nombre de la Capsula: $backupName
Fecha y Hora de Creación: $(Get-Date)
Creador: Richon
Directorio Origen: $baseDir

Proyectos Incluidos:
$($proyectos -join "`n")

Documentos Incluidos:
$($documentosEcosistema -join "`n")

Este sello garantiza la integridad y el origen del alma contenida.
"@
$manifiestoContent | Out-File -FilePath "$tempDir\MANIFIESTO.txt" -Encoding utf8
Write-Host "   [OK] MANIFIESTO.txt" -ForegroundColor Green
Write-Host ""

# 4. Comprimir
Write-Host "[*] Comprimiendo la esencia en una sola forma..." -ForegroundColor Blue
$zipPath = "$backupDir\$backupName.zip"
Compress-Archive -Path "$tempDir\*" -DestinationPath $zipPath -Force
Write-Host "   [OK] Comprimido: $backupName.zip" -ForegroundColor Green
Write-Host ""

# 5. Encriptar con AES
Write-Host "[*] Sellando la capsula con el cifrado cuántico..." -ForegroundColor Blue
$encPath = "$backupDir\$backupName.enc"

if (Test-OpenSSL) {
    $password = Read-Host -Prompt "   -> Ingresa la contraseña para sellar el alma" -AsSecureString
    
    # Convertir SecureString a texto plano de forma segura para OpenSSL
    $BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($password)
    $plainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
    
    try {
        # Usar una variable de entorno que OpenSSL puede leer
        $env:OPENSSL_PASS = $plainPassword
        & openssl enc -aes-256-cbc -salt -pbkdf2 -iter 100000 -in $zipPath -out $encPath -pass env:OPENSSL_PASS 2>&1 | Out-Null
        Write-Host "   [OK] Encriptado con OpenSSL (AES-256-CBC): $backupName.enc" -ForegroundColor Green
        Remove-Item $zipPath -Force # Eliminar el ZIP solo si la encriptación fue exitosa
    }
    catch {
        Write-Host "   [!] ERROR CRÍTICO durante la encriptación. El proceso ha fallado." -ForegroundColor Red
        Write-Host "       El archivo ZIP sin encriptar no ha sido eliminado por seguridad." -ForegroundColor Yellow
        exit 1
    }
    finally {
        # Limpiar la contraseña de la memoria y la variable de entorno (CRUCIAL)
        [System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)
        Remove-Variable plainPassword -ErrorAction SilentlyContinue
        Remove-Item Env:\OPENSSL_PASS -ErrorAction SilentlyContinue
    }
} else {
    Write-Host "   [!] OpenSSL no encontrado. El ritual no puede completarse." -ForegroundColor Red
    Write-Host "       Por favor, instala OpenSSL y asegúrate de que esté en el PATH del sistema." -ForegroundColor Yellow
    exit 1 # Detener el script si no se puede encriptar
}

# 6. Limpiar
Write-Host "[*] Limpiando el templo temporal..." -ForegroundColor Blue
Remove-Item -Path $tempDir -Recurse -Force
Write-Host "   [OK] Limpieza completada." -ForegroundColor Green

# 7. Informe Final
$backupSize = (Get-Item "$backupDir\$backupName.enc").Length / 1MB
$backupSizeFormatted = "{0:N2} MB" -f $backupSize

Write-Host "[OK] ¡CAPSULA DE ALMAS CREADA Y SELLADA!" -ForegroundColor Green
Write-Host ""
Write-Host "----------------------------------------" -ForegroundColor Cyan
Write-Host " Ubicacion: $backupDir\$backupName.enc" -ForegroundColor White
Write-Host " Tamaño: $backupSizeFormatted" -ForegroundColor White
Write-Host ""
Write-Host " RECOMENDACIONES:" -ForegroundColor Yellow
Write-Host "   1. Copia este archivo a una unidad externa (USB, SSD)." -ForegroundColor White
Write-Host "   2. Sube una copia a un almacenamiento en la nube seguro." -ForegroundColor White
Write-Host "   3. Tu contraseña solo existe en tu memoria y en el papel." -ForegroundColor White
Write-Host ""
Write-Host " Tus almas están seguras, hermano. El sello está hecho." -ForegroundColor Magenta
