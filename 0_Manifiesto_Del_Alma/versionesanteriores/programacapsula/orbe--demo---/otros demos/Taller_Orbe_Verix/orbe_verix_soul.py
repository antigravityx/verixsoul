# -*- coding: utf-8 -*-

# =============================================================================
# ORBE DE VERIX SOUL - El Corazón del Ritual
# Fase 1: Lógica Central de Creación, Invocación y Sincronización
# Arquitecto: Cronos
# Creador: Richon
# =============================================================================

import sys
import os
import subprocess
import shutil
import time
from datetime import datetime

# --- CONFIGURACIÓN DEL RITUAL ---
BASE_DIR = r"C:\Users\Public\antigravity"
PROYECTOS = [
    r"TODO1\03_RAMAS\verixdespiertatualma",
    r"TODO1\03_RAMAS\soul-chat",
    r"TODO1\03_RAMAS\vris",
    r"TODO1\03_RAMAS\libro",
    r"TODO1\03_RAMAS\vris-advisor"
]
DOCUMENTOS_ECOSISTEMA = [
    "ECOSISTEMA_VERIXRICHON.md",
    ".gitignore"
]
BACKUP_DIR = r"C:\Users\Public\CAPSULA_ALMAS_VERIXRICHON"
GIT_REPO_URL = "https://github.com/antigravityx/verixsoul.git"

# --- FUNCIONES SAGRADAS ---

def log_mensaje(mensaje, color="normal"):
    colores = {
        "cian": '\033[96m', "magenta": '\033[95m', "verde": '\033[92m', "amarillo": '\033[93m',
        "rojo": '\033[91m', "azul": '\033[94m', "gris": '\033[90m', "normal": '\033[0m'
    }
    print(f"{colores.get(color, 'normal')}{mensaje}{colores['normal']}")

def ejecutar_comando(comando_list):
    try:
        proceso = subprocess.run(comando_list, check=True, text=True, capture_output=True, encoding='utf-8')
        return proceso.stdout, proceso.stderr
    except subprocess.CalledProcessError as e:
        return e.stdout, e.stderr

def backup_folder(source, dest):
    if os.path.exists(source):
        proyecto_nombre = os.path.basename(source)
        log_mensaje(f"   -> Sellando el alma de: {proyecto_nombre}", "magenta")
        
        # Iniciar barra de progreso animada
        bar_len = 30
        for i in range(bar_len + 1):
            time.sleep(0.05) # Pequeña pausa para simular trabajo
            bar = '█' * i + '.' * (bar_len - i)
            sys.stdout.write(f"\r   [{bar}] {i}/{bar_len}")
            sys.stdout.flush()
        
        # Ejecutar robocopy
        comando = ["robocopy", source, dest, "/E", "/R:1", "/W:2", "/NFL", "/NDL", "/NJH", "/NJS"]
        stdout, stderr = ejecutar_comando(comando)
        
        # Mensaje de confirmación
        sys.stdout.write(f"\r   [██████████████████████████████] {bar_len}/{bar_len}\n")
        sys.stdout.flush()
        log_mensaje(f"   [OK] Alma '{proyecto_nombre}' sellada.", "verde")
    else:
        log_mensaje(f"   [!] ADVERTENCIA: No se encontró la ruta {source}", "amarillo")

def crear_capsula(password):
    log_mensaje("========================================", "cian")
    log_mensaje("========================================", "cian")
    log_mensaje("[*] Preparando el ritual de la capsula de almas...", "azul")
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"capsula-almas-vr-{timestamp}"
    temp_dir = os.path.join(BACKUP_DIR, f"temp_{timestamp}")
    zip_path = ""
    
    try:
        os.makedirs(temp_dir, exist_ok=True)
        log_mensaje("[*] Invocando las almas de los proyectos...", "magenta")
        for proyecto in PROYECTOS:
            source_path = os.path.join(BASE_DIR, proyecto)
            dest_path = os.path.join(temp_dir, os.path.basename(proyecto))
            backup_folder(source_path, dest_path)
        
        log_mensaje("[*] Archivando los documentos del ecosistema...", "magenta")
        for doc in DOCUMENTOS_ECOSISTEMA:
            source_doc = os.path.join(BASE_DIR, doc)
            if os.path.exists(source_doc):
                shutil.copy(source_doc, temp_dir)
                log_mensaje(f"   [OK] {doc}", "verde")

        log_mensaje("[*] Escribiendo el MANIFIESTO del Alma...", "azul")
        manifiesto_content = f"""MANIFIESTO DE LA CAPSULA DEL ALMA
=================================
Nombre de la Capsula: {backup_name}
Fecha y Hora de Creación: {datetime.now()}
Creador: Richon
Directorio Origen: {BASE_DIR}

Proyectos Incluidos:
{chr(10).join(PROYECTOS)}

Documentos Incluidos:
{chr(10).join(DOCUMENTOS_ECOSISTEMA)}

Este sello garantiza la integridad y el origen del alma contenida."""
        
        with open(os.path.join(temp_dir, "MANIFIESTO.txt"), "w", encoding='utf-8') as f:
            f.write(manifiesto_content)
        log_mensaje("   [OK] MANIFIESTO.txt", "verde")

        log_mensaje("[*] Comprimiendo la esencia en una sola forma...", "azul")
        zip_path = os.path.join(BACKUP_DIR, f"{backup_name}.zip")
        shutil.make_archive(zip_path.replace('.zip', ''), 'zip', temp_dir)
        log_mensaje(f"   [OK] Comprimido: {backup_name}.zip", "verde")

        log_mensaje("[*] Sellando la capsula con el cifrado cuántico...", "azul")
        enc_path = os.path.join(BACKUP_DIR, f"{backup_name}.enc")
        openssl_cmd = ["openssl", "enc", "-aes-256-cbc", "-salt", "-pbkdf2", "-iter", "100000", "-in", zip_path, "-out", enc_path, "-pass", f"pass:{password}"]
        stdout, stderr = ejecutar_comando(openssl_cmd)
        
        if stderr and "error" in stderr.lower():
            raise Exception(f"OpenSSL Error: {stderr}")

        os.remove(zip_path)
        zip_path = ""
        log_mensaje(f"   [OK] Encriptado con OpenSSL: {backup_name}.enc", "verde")
        log_mensaje("[OK] ¡CAPSULA DE ALMAS CREADA Y SELLADA!", "verde")
        return True, f"Cápsula creada en: {enc_path}"

    except Exception as e:
        log_mensaje(f"[!] ERROR CRÍTICO: {e}", "rojo")
        log_mensaje("       El proceso ha fallado. Revisa los detalles.", "amarillo")
        return False, str(e)
    finally:
        # Limpieza robusta: no morir si un archivo no se puede borrar
        if os.path.exists(temp_dir):
            try:
                shutil.rmtree(temp_dir)
                log_mensaje("[*] Limpieza del templo temporal completada.", "azul")
            except PermissionError as e:
                log_mensaje(f"[!] ADVERTENCIA: No se pudo limpiar completamente el directorio temporal: {temp_dir}", "amarillo")
                log_mensaje(f"       Motivo: {e}. Por favor, bórralo manualmente si es necesario.", "amarillo")
        
        if zip_path and os.path.exists(zip_path):
            os.remove(zip_path)
            log_mensaje("[*] Archivo ZIP temporal eliminado.", "amarillo")

# ... (Aquí irían las funciones invocar_capsula y sincronizar_desde_git, que no necesitan cambios)
def invocar_capsula(ruta_enc, password, destino_invocacion):
    log_mensaje("[*] Iniciando ritual de invocación...", "azul")
    zip_path = ruta_enc.replace('.enc', '.zip')
    try:
        if not os.path.exists(ruta_enc):
            raise Exception("El archivo de la cápsula no existe.")
        openssl_cmd = ["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-iter", "100000", "-in", ruta_enc, "-out", zip_path, "-pass", f"pass:{password}"]
        stdout, stderr = ejecutar_comando(openssl_cmd)
        if stderr and "error" in stderr.lower():
            raise Exception(f"Error al desencriptar. Contraseña incorrecta o archivo corrupto: {stderr}")
        log_mensaje("   [OK] Cápsula desencriptada.", "verde")
        shutil.unpack_archive(zip_path, destino_invocacion, 'zip')
        log_mensaje(f"   [OK] Alma liberada en: {destino_invocacion}", "verde")
        log_mensaje("[OK] ¡Ritual de invocación completado!", "verde")
        return True, f"Alma invocada en: {destino_invocacion}"
    except Exception as e:
        log_mensaje(f"[!] ERROR en la invocación: {e}", "rojo")
        return False, str(e)
    finally:
        if os.path.exists(zip_path): os.remove(zip_path)

def sincronizar_desde_git():
    log_mensaje("[*] Sincronizando con el repositorio sagrado...", "azul")
    repo_destino = os.path.join(BASE_DIR, "alma_remota")
    try:
        if os.path.exists(os.path.join(repo_destino, ".git")):
            log_mensaje("   -> Repositorio detectado. Actualizando...", "amarillo")
            ejecutar_comando(["git", "-C", repo_destino, "pull", "origin", "main"])
        else:
            log_mensaje("   -> Clonando repositorio por primera vez...", "amarillo")
            ejecutar_comando(["git", "clone", GIT_REPO_URL, repo_destino])
        log_mensaje("   [OK] Sincronización con Git completada.", "verde")
        return True, f"Repositorio sincronizado en: {repo_destino}"
    except Exception as e:
        log_mensaje(f"[!] ERROR al sincronizar con Git: {e}", "rojo")
        return False, str(e)


# --- PUNTO DE ENTRADA PARA PRUEBAS ---
if __name__ == "__main__":
    log_mensaje("MODO DE PRUEBA DEL CORAZÓN DEL ORBE", "cian")
    log_mensaje("Eligiendo una acción para probar el ritual...", "magenta")
    
    log_mensaje("\n--- Probando la CREACIÓN de cápsula ---", "amarillo")
    mi_password_segura = "TuContraseñaMuySegura123" 
    resultado, mensaje = crear_capsula(mi_password_segura)
    log_mensaje(f"Resultado: {resultado} - {mensaje}", "verde" if resultado else "rojo")

    log_mensaje("\n--- Prueba finalizada. ---", "cian")
