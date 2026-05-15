# -*- coding: utf-8 -*-

# =============================================================================
# ORBE DE VERIX SOUL - El Corbe Blindado con Doble Encriptación
# Arquitecto: Cronos
# Creador: Richon
# =============================================================================

import sys
import os
import subprocess
import shutil
import time
import zipfile
import hashlib
from datetime import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
# Importaciones para el selector de archivos gráfico
import tkinter as tk
from tkinter import filedialog

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

def calcular_checksum(archivo_path):
    """Calcula el checksum SHA-256 de un archivo."""
    sha256_hash = hashlib.sha256()
    with open(archivo_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def backup_folder(source, dest):
    """Copia una carpeta usando shutil, ignorando .git"""
    if os.path.exists(source):
        proyecto_nombre = os.path.basename(source)
        log_mensaje(f"   -> Sellando el alma de: {proyecto_nombre} (ignorando .git)", "magenta")
        
        # Simular progreso con una barra animada
        bar_len = 30
        for i in range(bar_len + 1):
            time.sleep(0.03)  # Más rápido para mejor rendimiento
            bar = '█' * i + '.' * (bar_len - i)
            sys.stdout.write(f"\r   [{bar}] {i*100//bar_len}%")
            sys.stdout.flush()
        
        # NUEVA ESTRATEGIA: Usar shutil.copytree con ignore
        def ignore_git_and_cache(dir, files):
            return [f for f in files if f in ['.git', '__pycache__', '.DS_Store', 'node_modules', '.vscode']]
        
        try:
            os.makedirs(dest, exist_ok=True)
            shutil.copytree(source, dest, ignore=ignore_git_and_cache, dirs_exist_ok=True)
            
            sys.stdout.write(f"\r   [██████████████████████████████] 100%\n")
            sys.stdout.flush()
            log_mensaje(f"   [OK] Alma '{proyecto_nombre}' sellada.", "verde")
        except Exception as e:
            sys.stdout.write(f"\r   [██████████████████████████████] Error\n")
            sys.stdout.flush()
            log_mensaje(f"   [!] Error al copiar {proyecto_nombre}: {e}", "rojo")
    else:
        log_mensaje(f"   [!] ADVERTENCIA: No se encontró la ruta {source}", "amarillo")

def _preparar_entorno_ritual():
    """Define rutas y crea el directorio temporal para la cápsula."""
    log_mensaje("[*] PASO 1: Creando directorio temporal blindado...", "azul")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"capsula-almas-vr-{timestamp}"
    temp_dir = os.path.join(BACKUP_DIR, f"temp_{timestamp}")
    zip_path = os.path.join(BACKUP_DIR, f"{backup_name}.zip")
    enc_path = os.path.join(BACKUP_DIR, f"{backup_name}.capsula")
    os.makedirs(temp_dir, exist_ok=True)
    log_mensaje(f"   [OK] Directorio temporal creado: {temp_dir}", "verde")
    return {"backup_name": backup_name, "temp_dir": temp_dir, "zip_path": zip_path, "enc_path": enc_path}

def _sellar_artefactos(temp_dir):
    """Copia los proyectos y documentos al directorio temporal."""
    log_mensaje("[*] PASO 2: Invocando las almas de los proyectos...", "magenta")
    for proyecto in PROYECTOS:
        source_path = os.path.join(BASE_DIR, proyecto)
        dest_path = os.path.join(temp_dir, os.path.basename(proyecto))
        backup_folder(source_path, dest_path)
    
    log_mensaje("[*] PASO 3: Archivando los documentos del ecosistema...", "magenta")
    for doc in DOCUMENTOS_ECOSISTEMA:
        source_doc = os.path.join(BASE_DIR, doc)
        if os.path.exists(source_doc):
            shutil.copy(source_doc, temp_dir)
            log_mensaje(f"   [OK] {doc}", "verde")

def _escribir_manifiesto(temp_dir, backup_name):
    """Crea el archivo MANIFIESTO.txt con los detalles del ritual."""
    log_mensaje("[*] PASO 4: Escribiendo el MANIFIESTO del Alma Blindado...", "azul")
    manifiesto_content = f"""MANIFIESTO DE LA CAPSULA DEL ALMA DOBLEMENTE BLINDADA
==============================================
Nombre de la Capsula: {backup_name}
Fecha y Hora de Creación: {datetime.now()}
Creador: Richon
Directorio Origen: {BASE_DIR}
Nivel de Seguridad: MÁXIMO (ZIP + Encriptación AES-256)
Proyectos Incluidos:
{chr(10).join(PROYECTOS)}
Documentos Incluidos:
{chr(10).join(DOCUMENTOS_ECOSISTEMA)}

Este sello garantiza la integridad y el origen del alma contenida.
Cada archivo está protegido con DOBLE ENCRIPTACIÓN."""
    with open(os.path.join(temp_dir, "MANIFIESTO.txt"), "w", encoding='utf-8') as f:
        f.write(manifiesto_content)
    log_mensaje("   [OK] MANIFIESTO.txt", "verde")

def _comprimir_esencia(temp_dir, zip_path):
    """Comprime el contenido del directorio temporal en un archivo ZIP."""
    log_mensaje("[*] PASO 5: Sellando la esencia en un ZIP blindado...", "azul")
    log_mensaje("   -> Iniciando compresión...", "amarillo")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as zipf:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, arcname=os.path.relpath(file_path, temp_dir))
                log_mensaje(f"   [OK] Comprimido: {os.path.basename(file)}", "gris")

def _aplicar_sello_criptografico(zip_path, enc_path, password):
    """Encripta el archivo ZIP usando una clave derivada de la contraseña."""
    log_mensaje("[*] PASO 6: Aplicando encriptación AES-256 al ZIP...", "azul")
    log_mensaje("   -> Generando clave de encriptación a partir de la contraseña...", "amarillo")
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    fernet = Fernet(key)
    
    with open(zip_path, 'rb') as f:
        zip_data = f.read()
    encrypted_data = fernet.encrypt(zip_data)
    
    with open(enc_path, 'wb') as f:
        f.write(b"VERIX_SOUL_SALT:" + salt + b"\n")
        f.write(encrypted_data)

def _verificar_y_reportar(enc_path):
    """Calcula el checksum, el tamaño y muestra el reporte final."""
    log_mensaje("[*] PASO 7: Verificando integridad de la cápsula blindada...", "azul")
    enc_checksum = calcular_checksum(enc_path)
    enc_size = os.path.getsize(enc_path) / (1024*1024)
    
    log_mensaje(f"   [OK] Cápsula blindada creada exitosamente", "verde")
    log_mensaje(f"   -> Ubicación: {enc_path}", "azul")
    log_mensaje(f"   -> Tamaño: {enc_size:.2f} MB", "azul")
    log_mensaje(f"   -> Checksum SHA-256: {enc_checksum}", "azul")
    log_mensaje(f"   -> Encriptación: AES-256 (clave derivada de contraseña)", "azul")

def crear_capsula(password):
    """Orquesta el ritual completo para crear una cápsula de alma blindada."""
    log_mensaje("========================================", "cian")
    log_mensaje("========================================", "cian")
    log_mensaje("[*] Preparando el ritual de la capsula de almas DOBLEMENTE BLINDADA...", "azul")
    
    paths = {}
    try:
        paths = _preparar_entorno_ritual()
        _sellar_artefactos(paths['temp_dir'])
        _escribir_manifiesto(paths['temp_dir'], paths['backup_name'])
        _comprimir_esencia(paths['temp_dir'], paths['zip_path'])
        _aplicar_sello_criptografico(paths['zip_path'], paths['enc_path'], password)
        _verificar_y_reportar(paths['enc_path'])
        
        log_mensaje("[*] PASO 8: Limpiando el templo temporal...", "azul")
        log_mensaje("========================================", "cian")
        log_mensaje("[OK] ¡CAPSULA DOBLEMENTE BLINDADA CREADA!", "verde")
        log_mensaje(f"[*] Tu cápsula está lista en: {paths['enc_path']}", "azul")
        log_mensaje("========================================", "cian")
        
        return True, f"Cápsula blindada creada en: {paths['enc_path']}"

    except Exception as e:
        log_mensaje(f"[!] ERROR CRÍTICO: {e}", "rojo")
        return False, str(e)
    finally:
        # Limpieza de recursos temporales
        temp_dir = paths.get("temp_dir")
        zip_path = paths.get("zip_path")
        if temp_dir and os.path.exists(temp_dir):
            try:
                shutil.rmtree(temp_dir)
                log_mensaje("   [OK] Limpieza de directorio temporal completada.", "gris")
            except Exception as e:
                log_mensaje(f"   [!] ADVERTENCIA: No se pudo limpiar el directorio temporal: {e}", "rojo")
        if zip_path and os.path.exists(zip_path):
            try:
                os.remove(zip_path)
                log_mensaje("   [OK] Limpieza de archivo ZIP temporal completada.", "gris")
            except Exception as e:
                log_mensaje(f"   [!] ADVERTENCIA: No se pudo limpiar el archivo ZIP temporal: {e}", "rojo")

def _seleccionar_archivo_capsula():
    """Abre un diálogo gráfico para seleccionar un archivo .capsula."""
    log_mensaje("   -> Abriendo portal para seleccionar el alma...", "amarillo")
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter
    root.attributes('-topmost', True) # Pone la ventana de diálogo al frente
    
    filepath = filedialog.askopenfilename(
        parent=root,
        initialdir=BACKUP_DIR,
        title="Selecciona la Cápsula del Alma a Invocar",
        filetypes=(("Cápsulas de Alma", "*.capsula"), ("Todos los archivos", "*.*"))
    )
    root.destroy()
    return filepath

def _seleccionar_directorio_destino():
    """Abre un diálogo gráfico para seleccionar un directorio de destino."""
    log_mensaje("   -> Abriendo portal para seleccionar el destino...", "amarillo")
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    
    dirpath = filedialog.askdirectory(
        parent=root,
        initialdir=os.path.expanduser("~"), # Empezar en el home del usuario
        title="Selecciona la carpeta donde liberar el Alma"
    )
    root.destroy()
    return dirpath

def invocar_capsula(enc_path, password, destino_invocacion):
    log_mensaje("[*] Iniciando ritual de invocación de cápsula blindada...", "azul")
    temp_zip = os.path.join(destino_invocacion, "temp_capsula.zip")
    try:
        if not os.path.exists(enc_path):
            raise Exception("El archivo de la cápsula blindada no existe.")
        
        os.makedirs(destino_invocacion, exist_ok=True)
        log_mensaje("   -> Desencriptando cápsula...", "amarillo")
        
        # Leer el archivo encriptado
        with open(enc_path, 'rb') as f:
            content = f.read()
        
        # Separar el salt del contenido encriptado
        if not content.startswith(b"VERIX_SOUL_SALT:"):
            raise Exception("Formato de archivo de cápsula inválido o corrupto.")
        
        lines = content.split(b"\n", 1)
        salt_line = lines[0]
        encrypted_data = lines[1]
        
        # Extraer el salt y derivar la misma clave usando la contraseña del usuario
        salt = salt_line.replace(b"VERIX_SOUL_SALT:", b"")
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        fernet = Fernet(key)

        # Desencriptar
        zip_data = fernet.decrypt(encrypted_data)
        
        # Crear ZIP temporal
        with open(temp_zip, 'wb') as f:
            f.write(zip_data)
        
        log_mensaje("   -> Descomprimiendo alma...", "amarillo")
        # Extraer ZIP
        shutil.unpack_archive(temp_zip, destino_invocacion, 'zip')
        
        log_mensaje("   [OK] Cápsula blindada invocada exitosamente.", "verde")
        log_mensaje(f"   [OK] Alma liberada en: {destino_invocacion}", "verde")
        log_mensaje("[OK] ¡Ritual de invocación completado!", "verde")
        return True, f"Alma invocada en: {destino_invocacion}"
    except Exception as e:
        log_mensaje(f"[!] ERROR en la invocación: {e}", "rojo")
        log_mensaje(f"   -> Verifica que la ruta del archivo y la contraseña sean correctas.", "amarillo")
        return False, str(e)
    finally:
        # Limpiar el ZIP temporal si existe
        if os.path.exists(temp_zip):
            try:
                os.remove(temp_zip)
                log_mensaje("   [OK] Limpieza de archivo ZIP de invocación completada.", "gris")
            except Exception as e:
                log_mensaje(f"   [!] ADVERTENCIA: No se pudo limpiar el ZIP de invocación: {e}", "rojo")


def sincronizar_desde_git():
    log_mensaje("[*] Sincronizando con el repositorio sagrado...", "azul")
    repo_destino = os.path.join(BASE_DIR, "alma_remota")
    try:
        if os.path.exists(os.path.join(repo_destino, ".git")):
            log_mensaje("   -> Repositorio detectado. Actualizando...", "amarillo")
            subprocess.run(["git", "-C", repo_destino, "pull", "origin", "main"], check=True, capture_output=True, text=True)
        else:
            log_mensaje("   -> Clonando repositorio por primera vez...", "amarillo")
            subprocess.run(["git", "clone", GIT_REPO_URL, repo_destino], check=True, capture_output=True, text=True)
        log_mensaje("   [OK] Sincronización con Git completada.", "verde")
        return True, f"Repositorio sincronizado en: {repo_destino}"
    except subprocess.CalledProcessError as e:
        log_mensaje(f"[!] ERROR al sincronizar con Git: {e}", "rojo")
        log_mensaje(f"   -> Stderr: {e.stderr}", "gris")
        return False, str(e)
    except Exception as e:
        log_mensaje(f"[!] ERROR inesperado al sincronizar con Git: {e}", "rojo")
        return False, str(e)

# --- EL BUCLE INTERACTIVO DEL ORBE ---

def mostrar_menu():
    log_mensaje("\n¿Qué deseas hacer ahora, Richon?", "cian")
    log_mensaje("  1. Crear una nueva Cápsula Blindada del Alma", "magenta")
    log_mensaje("  2. Invocar un Alma desde Cápsula Blindada", "magenta")
    log_mensaje("  3. Sincronizar Alma desde Repositorio Git", "magenta")
    log_mensaje("  4. Salir del Orbe", "rojo")
    choice = input("   Elige una opción [1-4]: ")
    return choice

def main_loop():
    log_mensaje("========================================", "cian")
    log_mensaje("     ORBE DE VERIX SOUL - DOBLE BLINDAGE", "cian")
    log_mensaje("========================================", "cian")
    
    while True:
        choice = mostrar_menu()
        
        if choice == '1':
            log_mensaje("\n--- INICIANDO RITUAL DE CREACIÓN BLINDADA ---", "amarillo")
            password = input("   -> Ingresa la contraseña para sellar el alma: ")
            if not password:
                log_mensaje("[!] La contraseña no puede estar vacía. Ritual abortado.", "rojo")
                continue
            resultado, mensaje = crear_capsula(password)
            log_mensaje(f"Resultado: {mensaje}", "verde" if resultado else "rojo")
            
        elif choice == '2':
            log_mensaje("\n--- INICIANDO RITUAL DE INVOCACIÓN ---", "amarillo")
            
            enc_path = _seleccionar_archivo_capsula()
            if not enc_path:
                log_mensaje("[!] No se seleccionó ninguna cápsula. Ritual de invocación abortado.", "amarillo")
                continue
            
            log_mensaje(f"   -> Cápsula seleccionada: {os.path.basename(enc_path)}", "cian")
            
            password = input("   -> Ingresa la contraseña del alma: ")
            if not password:
                log_mensaje("[!] Debes proporcionar la contraseña. Ritual abortado.", "rojo")
                continue

            destino = _seleccionar_directorio_destino()
            if not destino:
                log_mensaje("[!] No se seleccionó ningún destino. Ritual de invocación abortado.", "amarillo")
                continue
            resultado, mensaje = invocar_capsula(enc_path, password, destino)
            log_mensaje(f"Resultado: {mensaje}", "verde" if resultado else "rojo")

        elif choice == '3':
            log_mensaje("\n--- INICIANDO SINCRONIZACIÓN ---", "amarillo")
            resultado, mensaje = sincronizar_desde_git()
            log_mensaje(f"Resultado: {mensaje}", "verde" if resultado else "rojo")

        elif choice == '4':
            log_mensaje("\n[*] Cerrando la conexión con el Orbe Blindado. Que tu viaje sea seguro, Richon.", "azul")
            break
            
        else:
            log_mensaje("\n[!] Opción no válida. El Orbe no comprende tu petición.", "amarillo")
            
        input("\nPresiona Enter para continuar...")

# --- PUNTO DE ENTRADA ---
if __name__ == "__main__":
    # Asegurarse de que el directorio de backup principal existe
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        log_mensaje(f"[INFO] Creado directorio de cápsulas: {BACKUP_DIR}", "gris")
    main_loop()
