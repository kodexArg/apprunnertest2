## AppRunner Test (2)

Proyecto de prueba de AWS App Runner sin Docker - Configuración basada en código fuente

**Repositorio**: https://github.com/kodexArg/apprunnertest2/

### ⚙️ Configuración

Este proyecto utiliza **exclusivamente AWS App Runner** con código fuente (sin Docker).

**Archivo principal de configuración**: `apprunner.yaml`

### 💻 Entorno de Desarrollo

- **OS**: Windows
- **Shell**: PowerShell 7+
- **Python**: Virtual environment en `.venv/` (activo)

### 📁 Estructura del Proyecto

```
.
├── .venv/                       # Entorno virtual Python (desarrollo local)
├── apprunner.yaml               # Configuración de AWS App Runner (REQUERIDO)
├── requirements.txt             # Dependencias de Python (Django)
├── manage.py                    # Script principal de Django
├── project/                     # Proyecto Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                        # App principal de Django
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── README.md
```

### 🚀 Despliegue

1. El archivo `apprunner.yaml` contiene toda la configuración necesaria
2. App Runner construye automáticamente usando Python 3.11
3. La aplicación se ejecuta en el puerto 8080
4. Configuración actual:
   ```yaml
   version: 1.0
   runtime: python311
   build:
     commands:
       build:
         - pip3 install uv
         - uv venv .venv
         - uv pip install -r requirements.txt
   run:
     runtime-version: 3.11
     pre-run:
       - pip3 install uv
     command: .venv/bin/gunicorn -b 0.0.0.0:8080 project.wsgi
     network:
       port: 8080
   ```

### 📋 Reglas del Proyecto

- ✅ **SÍ**: Usar y modificar `apprunner.yaml`
- ✅ **SÍ**: Managed runtimes de App Runner
- ✅ **SÍ**: Despliegue desde código fuente
- ❌ **NO**: Docker, Dockerfile, ECS, Fargate
- ❌ **NO**: Imágenes de contenedor

### 📚 Documentación

Basado en la documentación oficial: https://docs.aws.amazon.com/apprunner/latest/dg/config-file-ref.html

### 🔗 Enlaces

- **GitHub**: https://github.com/kodexArg/apprunnertest2/
- **Usuario**: kodexArg
