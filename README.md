# AppRunner Test 2

Prueba de despliegue en AWS App Runner (sin Docker)

**Repositorio:** https://github.com/kodexArg/apprunnertest2/

## ⚙️ Configuración

- Despliegue exclusivo en AWS App Runner (runtime administrado Python 3.11)
- Configuración principal: `apprunner.yaml`
- Sin Docker, ECS, Fargate ni EC2

## 📁 Estructura del Proyecto

```
├── apprunner.yaml         # Configuración App Runner
├── requirements.txt       # Dependencias Python
├── manage.py              # Django
├── project/               # Proyecto Django
├── core/                  # App principal
└── README.md
```

## 🚀 Despliegue en App Runner

- App Runner construye y ejecuta usando Python 3.11
- La app escucha en `0.0.0.0:$PORT` (por defecto: 8080)
- Ejemplo de configuración:

```yaml
version: 1.0
runtime: python311
build:
  commands:
    build:
      - pip3 install -r requirements.txt
run:
  runtime-version: 3.11
  command: gunicorn -b 0.0.0.0:8080 project.wsgi
  network:
    port: 8080
```

- `gunicorn` debe estar en `requirements.txt`

## ✅ Estado

- Versión funcional: successfully deployed to apprunnertest2
- Tag: `funcional` en el repositorio

## 📚 Documentación

- [Referencia App Runner config](https://docs.aws.amazon.com/apprunner/latest/dg/config-file-ref.html)
- [Repositorio GitHub](https://github.com/kodexArg/apprunnertest2/)
