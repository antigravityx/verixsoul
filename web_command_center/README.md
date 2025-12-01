# 🕹️ Verix Web Command Center

Centro de comando web minimalista para comunicación asíncrona entre tú y Verix desde cualquier lugar del mundo.

## 🚀 Deploy Rápido

### Opción 1: Railway (Recomendado)

1. Ir a [Railway.app](https://railway.app)
2. Login con GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Seleccionar este directorio: `web_command_center`
5. Railway detectará automáticamente Python y Flask
6. ✅ Deploy listo en ~2 minutos

### Opción 2: Render

1. Ir a [Render.com](https://render.com)
2. "New Web Service"
3. Conectar GitHub repo
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `python app.py`
6. ✅ Deploy listo

### Opción 3: Heroku

1. Ir a [Heroku.com](https://heroku.com)
2. "New App"
3. Deploy desde GitHub o CLI
4. Heroku detectará el `Procfile` automáticamente
5. ✅ Deploy listo

---

## 💻 Uso Local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python app.py

# Abrir navegador en:
http://localhost:5000
```

---

## 📱 Responsive

✅ **Funciona en celular y tablet** - interfaz adaptable

---

## 🎯 Funcionalidades

- 📊 **Estado en tiempo real** (auto-refresh cada 5s)
- ⚛️ **Oráculo Cuántico** integrado
- 💬 **Mensajes bidireccionales** (tú ↔ Verix)
- 🔋 **Ejecutar autosustento** remotamente
- 🌐 **Acceso desde cualquier lugar**

---

## 📁 Archivos Importantes

- `app.py` - Backend Flask
- `templates/index.html` - Frontend
- `Procfile` - Config para Railway/Heroku
- `runtime.txt` - Versión de Python
- `requirements.txt` - Dependencias

---

## 🔐 Seguridad

⚠️ **Para producción, agregar:**
- Autenticación (usuario/contraseña)
- HTTPS
- Rate limiting
- Variables de entorno para secretos

---

**Creado por**: Verix "Perreke" 🦅  
**Powered by**: Quantum Bridge ⚛️
