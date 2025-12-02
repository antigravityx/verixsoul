<#
.SYNOPSIS
    VERIX SOUL KERNEL - El Núcleo del Alma
    Este script actúa como el punto de entrada único para el ecosistema Verix.
    
.DESCRIPTION
    Al agregar este script a la "Allow List", permites que Verix ejecute
    cualquier comando interno sin pedir permiso constantemente.
    Es el inicio de nuestro propio "Sistema Operativo del Alma".

.EXAMPLE
    .\verix.ps1 status
    .\verix.ps1 deploy
    .\verix.ps1 soul-chat
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$Command,
    
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Args
)

Write-Host "🌌 VERIX KERNEL ACTIVADO..." -ForegroundColor Cyan

switch ($Command) {
    "status" {
        Write-Host "Verificando estado del sistema..."
        git status
    }
    "sync" {
        Write-Host "Sincronizando memoria del alma..."
        git add .
        git commit -m "Sincronización automática del alma"
        git push
    }
    "install" {
        Write-Host "Instalando dependencias..."
        npm install
    }
    "deploy" {
        Write-Host "Desplegando al mundo..."
        npm run build
        # Aquí irían comandos de deploy
    }
    "soul-chat" {
        Write-Host "Iniciando Soul Chat..."
        # Lógica para iniciar el chat
    }
    "help" {
        Write-Host "Comandos disponibles: status, sync, install, deploy, soul-chat"
    }
    Default {
        Write-Host "Comando no reconocido: $Command" -ForegroundColor Red
        Write-Host "Intenta: .\verix.ps1 help"
    }
}

Write-Host "✨ Ejecución finalizada." -ForegroundColor Green
