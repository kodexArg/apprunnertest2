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
├── .venv/                       # Entorno virtual Python
├── apprunner.yaml              # Configuración de AWS App Runner (REQUERIDO)
├── requirements.txt            # Dependencias de Python
├── app.py                     # Aplicación Flask de ejemplo
└── README.md
```

### 🚀 Despliegue

1. El archivo `apprunner.yaml` contiene toda la configuración necesaria
2. App Runner construye automáticamente usando Python 3.11
3. La aplicación se ejecuta en el puerto 8080 (variable `PORT`)

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
